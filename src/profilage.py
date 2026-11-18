"""Profilage des sources brutes du projet feux-de-foret-corse.

Le script lit un fichier brut, decrit chaque colonne (type, valeurs vides,
valeurs distinctes, minimum, maximum, valeurs les plus frequentes), lance des
controles propres a la source et ecrit un rapport Markdown.

Il ne modifie jamais les fichiers bruts : il les lit seulement.

Utilisation (depuis la racine du depot) :

    python src/profilage.py bdiff data/raw/bdiff_2A_2006_2025.csv
    python src/profilage.py mdf data/raw/mdf_2024.csv.gz data/raw/mdf_2025.csv.gz data/raw/mdf_2026.csv.gz

Le rapport est ecrit dans docs/qualite/profil-<source>.md (option --sortie
pour changer le chemin).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import pandas as pd

# Motifs pour reperer des donnees personnelles dans les colonnes de texte.
MOTIF_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
MOTIF_TELEPHONE = re.compile(r"(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}")

# Mots qui, dans un nom de colonne, signalent une donnee a examiner.
MOTS_SENSIBLES = ("nom", "prenom", "adresse", "telephone", "mail", "email", "deces",
                  "victime", "batiment", "coordonnee", "latitude", "longitude",
                  "x_", "y_")


# ---------------------------------------------------------------------------
# Lecture des sources
# ---------------------------------------------------------------------------

def lire_bdiff(chemin: Path) -> tuple[pd.DataFrame, list[str]]:
    """Lit un export de la consultation publique de la BDIFF.

    L'export commence par trois lignes d'information avant l'en-tete.
    Toutes les colonnes sont lues comme du texte pour ne rien perdre
    (les zeros en tete des codes, par exemple).
    """
    with open(chemin, encoding="utf-8-sig") as f:
        entete_info = [f.readline().strip().strip('"').replace('";"', " ; ")
                       for _ in range(3)]
    df = pd.read_csv(chemin, sep=";", skiprows=3, dtype=str,
                     keep_default_na=False, encoding="utf-8-sig")
    df = df.replace("", pd.NA)
    return df, entete_info


def lire_mdf(chemins: list[Path]) -> tuple[pd.DataFrame, list[str]]:
    """Lit et empile les fichiers de saison de la Meteo des forets.

    Les fichiers n'ont pas tous le meme schema (nom_dep ou dep_nom) : le
    schema de chaque fichier est note dans le rapport, puis les colonnes
    sont harmonisees uniquement pour pouvoir les empiler.
    """
    morceaux, notes = [], []
    for chemin in chemins:
        df = pd.read_csv(chemin, dtype=str, keep_default_na=False,
                         sep=None, engine="python")
        notes.append(f"`{chemin.name}` : {len(df)} lignes, colonnes "
                     + ", ".join(f"`{c}`" for c in df.columns))
        df = df.rename(columns={"dep_nom": "nom_dep"})
        df["fichier"] = chemin.name
        morceaux.append(df)
    df = pd.concat(morceaux, ignore_index=True).replace("", pd.NA)
    return df, notes


# ---------------------------------------------------------------------------
# Profil generique d'une colonne
# ---------------------------------------------------------------------------

def lire_dates(valeurs: pd.Series) -> pd.Series:
    """Convertit en dates. Les dates avec fuseau (Meteo des forets) sont
    ramenees a l'heure de Paris ; les dates sans fuseau (BDIFF) sont
    gardees telles quelles."""
    avec_fuseau = valeurs.dropna().str.contains(r"(?:[+-]\d{2}:\d{2}|Z)$")
    if len(avec_fuseau) and avec_fuseau.all():
        d = pd.to_datetime(valeurs, errors="coerce", utc=True, format="mixed")
        return d.dt.tz_convert("Europe/Paris").dt.tz_localize(None)
    return pd.to_datetime(valeurs, errors="coerce", format="mixed")


def type_observe(serie: pd.Series) -> str:
    """Devine le type d'une colonne lue en texte."""
    valeurs = serie.dropna()
    if valeurs.empty:
        return "vide"
    if pd.to_numeric(valeurs, errors="coerce").notna().all():
        entiers = valeurs.str.fullmatch(r"-?\d+").all()
        return "entier" if entiers else "decimal"
    forme_date = valeurs.str.match(r"\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}")
    if forme_date.all():
        if lire_dates(valeurs).notna().all():
            return "date"
    return "texte"


def nombre(x: float) -> str:
    """Ecrit un nombre lisible : 32 210 000 plutot que 3.221e+07."""
    if pd.isna(x):
        return ""
    if float(x).is_integer():
        return f"{int(x):,}".replace(",", " ") if abs(x) >= 10000 else str(int(x))
    return f"{x:,.2f}".replace(",", " ")


def profil_colonne(nom: str, serie: pd.Series) -> dict:
    total = len(serie)
    vides = int(serie.isna().sum())
    valeurs = serie.dropna()
    t = type_observe(serie)
    mini = maxi = ""
    if t in ("entier", "decimal"):
        num = pd.to_numeric(valeurs)
        mini, maxi = nombre(num.min()), nombre(num.max())
    elif t == "date":
        d = lire_dates(valeurs)
        mini, maxi = str(d.min())[:16], str(d.max())[:16]
    frequentes = ", ".join(f"{v} ({n})" for v, n
                           in valeurs.value_counts().head(3).items())
    return {
        "Colonne": nom,
        "Type observe": t,
        "Non vides": total - vides,
        "Vides (%)": f"{100 * vides / total:.2f}" if total else "",
        "Distinctes": valeurs.nunique(),
        "Min": mini,
        "Max": maxi,
        "3 valeurs les plus frequentes": frequentes,
    }


def tableau_markdown(lignes: list[dict]) -> str:
    if not lignes:
        return "_Aucune ligne._\n"
    entetes = list(lignes[0].keys())
    sortie = ["| " + " | ".join(entetes) + " |",
              "|" + "---|" * len(entetes)]
    for ligne in lignes:
        cellules = [str(ligne[e]).replace("|", "/").replace("\n", " ")
                    for e in entetes]
        sortie.append("| " + " | ".join(cellules) + " |")
    return "\n".join(sortie) + "\n"


# ---------------------------------------------------------------------------
# Reperage des donnees personnelles
# ---------------------------------------------------------------------------

def sans_accents(texte: str) -> str:
    table = str.maketrans("éèêëàâäîïôöùûüç", "eeeeaaaiioouuuc")
    return texte.lower().translate(table)


def reperer_donnees_personnelles(df: pd.DataFrame) -> list[dict]:
    lignes = []
    for col in df.columns:
        raisons = []
        mots_colonne = re.findall(r"[a-z0-9]+", sans_accents(col))
        mots = [m for m in MOTS_SENSIBLES
                if any(w == m or w.startswith(m) and m.endswith("_")
                       or (m.rstrip("s") == w.rstrip("s")) for w in mots_colonne)]
        if mots:
            raisons.append("nom de colonne contenant : " + ", ".join(mots))
        valeurs = df[col].dropna().astype(str)
        n_mail = int(valeurs.str.contains(MOTIF_EMAIL).sum())
        n_tel = int(valeurs.str.contains(MOTIF_TELEPHONE).sum())
        if n_mail:
            raisons.append(f"{n_mail} valeurs ressemblant a un e-mail")
        if n_tel:
            raisons.append(f"{n_tel} valeurs ressemblant a un telephone")
        if raisons:
            lignes.append({"Colonne": col, "Signal": "; ".join(raisons)})
    return lignes


# ---------------------------------------------------------------------------
# Controles propres a la BDIFF
# ---------------------------------------------------------------------------

def controles_bdiff(df: pd.DataFrame) -> list[str]:
    r = []
    n = len(df)

    cle = df.duplicated(subset=["Année", "Numéro"], keep=False)
    r.append(f"- Doublons sur la cle (`Année`, `Numéro`) : {int(cle.sum())} "
             f"lignes sur {n}.")
    r.append(f"- Lignes entierement identiques : {int(df.duplicated().sum())}.")
    meme = df.duplicated(subset=["Date de première alerte", "Code INSEE"],
                         keep=False)
    r.append(f"- Feux differents avec la meme commune et la meme date et "
             f"heure d'alerte (doublons possibles a examiner) : "
             f"{int(meme.sum())} lignes.")

    insee = df["Code INSEE"].dropna()
    mauvais = ~insee.str.fullmatch(r"(2[AB]|\d{2})\d{3}")
    r.append(f"- `Code INSEE` au format attendu (5 caracteres, 2A ou 2B "
             f"possibles) : {int((~mauvais).sum())} conformes, "
             f"{int(mauvais.sum())} non conformes, "
             f"{int(df['Code INSEE'].isna().sum())} vides. "
             f"Communes distinctes : {insee.nunique()}.")

    dates = pd.to_datetime(df["Date de première alerte"], errors="coerce")
    r.append(f"- `Date de première alerte` illisible ou vide : "
             f"{int(dates.isna().sum())} lignes. Periode couverte : "
             f"du {dates.min()} au {dates.max()}.")

    annee = pd.to_numeric(df["Année"], errors="coerce")
    ecart = (annee != dates.dt.year) & dates.notna()
    r.append(f"- `Année` differente de l'annee de la date d'alerte : "
             f"{int(ecart.sum())} lignes.")

    futur = dates.dt.date > date.today()
    r.append(f"- Dates d'alerte dans le futur : {int(futur.sum())}.")

    surf = pd.to_numeric(df["Surface parcourue (m2)"], errors="coerce")
    r.append(f"- `Surface parcourue (m2)` : {int(surf.isna().sum())} vides, "
             f"{int((surf < 0).sum())} negatives, {int((surf == 0).sum())} "
             f"egales a 0. Mediane {nombre(surf.median())} m2, maximum "
             f"{nombre(surf.max())} m2 ({nombre(surf.max() / 10000)} ha).")
    for seuil_ha in (1, 50):
        r.append(f"- Feux de plus de {seuil_ha} ha : "
                 f"{int((surf > seuil_ha * 10000).sum())}.")

    saison = dates.dt.month.between(6, 9)
    r.append(f"- Feux hors juin-septembre : {int((~saison & dates.notna()).sum())}"
             f" ({100 * (~saison & dates.notna()).sum() / n:.1f} %).")

    par_an = annee.value_counts().sort_index()
    attendues = set(range(int(annee.min()), int(annee.max()) + 1))
    manquantes = sorted(attendues - set(par_an.index.astype(int)))
    r.append(f"- Annees sans aucun feu entre {int(annee.min())} et "
             f"{int(annee.max())} : {manquantes if manquantes else 'aucune'}.")
    r.append("- Feux par annee : " + ", ".join(
        f"{int(a)} : {c}" for a, c in par_an.items()) + ".")

    nature = df["Nature"]
    r.append(f"- `Nature` (cause) vide : {int(nature.isna().sum())} lignes "
             f"({100 * nature.isna().mean():.1f} %).")
    vide_par_an = nature.isna().groupby(annee).mean().mul(100).round(1)
    r.append("- Part de `Nature` vide par annee (%) : " + ", ".join(
        f"{int(a)} : {v:g}" for a, v in vide_par_an.items()) + ".")
    return r


# ---------------------------------------------------------------------------
# Controles propres a la Meteo des forets
# ---------------------------------------------------------------------------

def controles_mdf(df: pd.DataFrame) -> list[str]:
    r = []
    n = len(df)

    dep = df["num_dep"].astype("string")
    r.append(f"- `num_dep` sur 1 caractere (a normaliser sur 2) : "
             f"{int((dep.str.len() == 1).sum())} lignes.")
    dep_norm = dep.str.zfill(2)
    r.append(f"- Departements distincts apres normalisation : "
             f"{dep_norm.nunique()}. Corse-du-Sud (2A) : "
             f"{int((dep_norm == '2A').sum())} lignes ; Haute-Corse (2B) : "
             f"{int((dep_norm == '2B').sum())} lignes.")

    pub = lire_dates(df["date"])
    r.append(f"- `date` illisible ou vide : {int(pub.isna().sum())} lignes.")
    jour_pub = pub.dt.date

    doublons = pd.DataFrame({"j": jour_pub, "d": dep_norm}).duplicated(keep=False)
    r.append(f"- Doublons sur (jour de publication, departement) : "
             f"{int(doublons.sum())} lignes sur {n}.")

    for col in ("niveau_j1", "niveau_j2"):
        niv = pd.to_numeric(df[col], errors="coerce")
        hors = ~niv.between(1, 4)
        r.append(f"- `{col}` vide ou hors de 1 a 4 : {int(hors.sum())} lignes. "
                 "Repartition : " + ", ".join(
                     f"{int(k)} : {v}" for k, v
                     in niv.value_counts().sort_index().items()) + ".")

    for fichier, bloc in df.assign(j=jour_pub, d=dep_norm).groupby("fichier"):
        jours = pd.to_datetime(pd.Series(bloc["j"].unique()))
        attendus = pd.date_range(jours.min(), jours.max(), freq="D")
        manquants = attendus.difference(jours)
        r.append(f"- `{fichier}` : publications du {jours.min().date()} au "
                 f"{jours.max().date()}, {len(jours)} jours, "
                 f"{len(manquants)} jours sans bulletin dans cet intervalle"
                 + (f" ({', '.join(str(m.date()) for m in manquants[:10])}"
                    f"{' ...' if len(manquants) > 10 else ''})"
                    if len(manquants) else "") + ".")
        par_dep = bloc.groupby("d")["j"].nunique()
        incomplets = par_dep[par_dep < len(jours)]
        r.append(f"  Departements avec moins de bulletins que de jours publies "
                 f": {len(incomplets)}"
                 + (f" ({', '.join(incomplets.index[:10])})"
                    if len(incomplets) else "") + ".")

    noms = df.groupby(dep_norm)["nom_dep"].nunique()
    r.append(f"- Departements avec plusieurs noms differents : "
             f"{int((noms > 1).sum())}.")
    return r


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def ecrire_rapport(source: str, chemins: list[Path], df: pd.DataFrame,
                   notes: list[str], controles: list[str],
                   sortie: Path) -> None:
    profils = [profil_colonne(c, df[c]) for c in df.columns if c != "fichier"]
    perso = reperer_donnees_personnelles(df.drop(columns="fichier",
                                                 errors="ignore"))
    titres = {"bdiff": "BDIFF", "mdf": "Météo des forêts"}
    lignes = [
        f"# Profil de la source : {titres[source]}",
        "",
        f"- **Généré par :** `src/profilage.py` le {date.today().isoformat()}",
        "- **Fichiers lus :** " + ", ".join(f"`{p.as_posix()}`" for p in chemins),
        f"- **Lignes :** {len(df)}",
        f"- **Colonnes :** {len([c for c in df.columns if c != 'fichier'])}",
        "",
        "Ce rapport décrit les données telles qu'elles sont. Il ne décide "
        "rien : les règles de qualité et leurs seuils sont fixés à partir "
        "de ces constats.",
        "",
        "## Informations du fichier",
        "",
        *[f"- {n}" for n in notes],
        "",
        "## Profil des colonnes",
        "",
        tableau_markdown(profils),
        "## Contrôles propres à la source",
        "",
        *controles,
        "",
        "## Repérage des données personnelles",
        "",
        "Colonnes signalées automatiquement (nom de colonne ou contenu). "
        "Un signal n'est pas une conclusion : chaque colonne est à examiner.",
        "",
        tableau_markdown(perso) if perso else "_Aucun signal._\n",
    ]
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text("\n".join(lignes), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", choices=["bdiff", "mdf"])
    parser.add_argument("fichiers", nargs="+", type=Path)
    parser.add_argument("--sortie", type=Path)
    args = parser.parse_args()

    for p in args.fichiers:
        if not p.exists():
            print(f"Fichier introuvable : {p}", file=sys.stderr)
            return 1

    if args.source == "bdiff":
        df, notes = lire_bdiff(args.fichiers[0])
        controles = controles_bdiff(df)
    else:
        df, notes = lire_mdf(args.fichiers)
        controles = controles_mdf(df)

    sortie = args.sortie or Path("docs/qualite") / f"profil-{args.source}.md"
    ecrire_rapport(args.source, args.fichiers, df, notes, controles, sortie)
    print(f"Rapport ecrit : {sortie} ({len(df)} lignes profilees)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
