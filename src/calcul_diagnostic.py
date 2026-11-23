"""Calculs du diagnostic et de l'objectif KPI (UE01.B, seance 1).

Le script recalcule, a partir des fichiers bruts, tous les chiffres cites
dans kpi/diagnostic-strategique.md et kpi/objectif-arouna-toure.md :

1. Croisement Meteo des forets x BDIFF (volet seuil) : pour la Corse-du-Sud
   et la Haute-Corse, jours par niveau, jours avec feu, jours de danger
   eleve sans feu, feux des jours de danger faible, et comparaison de
   plusieurs regles de declenchement.
2. Concentration et stabilite des feux par commune (volet zones), pour la
   Corse-du-Sud.

Il ne modifie jamais les fichiers bruts.

Methode du croisement :
- la colonne `date` de la Meteo des forets est l'heure de publication du
  bulletin, en UTC ; elle est convertie a l'heure de Paris ;
- `niveau_j1` est la prevision pour le lendemain de la publication : le
  jour vise est donc le jour de publication + 1 ;
- `niveau_j2` est la prevision pour le surlendemain (jour de publication + 2) ;
- un feu est rattache au jour de sa `Date de premiere alerte` (BDIFF) ;
- la periode est celle des jours vises par `niveau_j1` en 2024 et 2025
  (du 4 juin au 1er octobre), communs aux deux sources ; le script donne
  aussi le nombre de feux sur juin-septembre calendaire, periode citee dans
  la matrice.

Feux retenus : l'export BDIFF ne contient pas de colonne de type de feu ;
le filtre "Type de feu : F" (feux de foret) est applique a l'export par le
site de la BDIFF et ecrit dans la troisieme ligne du fichier. Le script lit
cette ligne et s'arrete si le filtre, le departement ou la periode attendus
n'y figurent pas.

Utilisation (depuis la racine du depot) :

    python src/calcul_diagnostic.py
        --mdf data/raw/mdf_2024.csv.gz data/raw/mdf_2025.csv.gz data/raw/mdf_2026.csv.gz
        --bdiff-2a data/raw/bdiff_2A_2006_2025.csv
        --bdiff-2b data/raw/bdiff_2B_2006_2025.csv
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

SAISONS_COMMUNES = (2024, 2025)


# ---------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------

def lire_mdf(chemins: list[Path]) -> pd.DataFrame:
    """Empile les fichiers de saison et calcule les jours vises."""
    morceaux = [pd.read_csv(c, dtype=str, sep=None, engine="python")
                .rename(columns={"dep_nom": "nom_dep"}) for c in chemins]
    df = pd.concat(morceaux, ignore_index=True)
    df["dep"] = df["num_dep"].str.zfill(2)
    publication = (pd.to_datetime(df["date"], utc=True)
                   .dt.tz_convert("Europe/Paris").dt.tz_localize(None)
                   .dt.normalize())
    df["publication"] = publication
    df["jour"] = publication + pd.Timedelta(days=1)
    df["n1"] = df["niveau_j1"].astype(int)
    df["n2"] = df["niveau_j2"].astype(int)
    return df


def lire_bdiff(chemin: Path, departement: str) -> tuple[pd.DataFrame, str]:
    """Lit un export BDIFF (trois lignes d'information avant l'en-tete).

    Verifie dans la troisieme ligne que l'export porte bien sur les feux de
    foret (type F), sur le departement attendu et sur 2006-2025.
    """
    with open(chemin, encoding="utf-8-sig") as f:
        criteres = [f.readline() for _ in range(3)][2]
    attendus = ["Type de feu : F", f"Département(s) : {departement}",
                "2006-01-01", "2025-12-31"]
    manquants = [a for a in attendus if a not in criteres]
    if manquants:
        raise SystemExit(f"{chemin} : criteres d'export inattendus, absents : "
                         f"{manquants}")
    df = pd.read_csv(chemin, sep=";", skiprows=3, dtype=str,
                     encoding="utf-8-sig")
    df["alerte"] = pd.to_datetime(df["Date de première alerte"])
    df["jour"] = df["alerte"].dt.normalize()
    df["annee"] = df["Année"].astype(int)
    criteres = criteres.strip().replace('";"', " ; ").strip('"')
    return df, criteres


# ---------------------------------------------------------------------------
# Volet seuil
# ---------------------------------------------------------------------------

def table_jours(mdf: pd.DataFrame, feux: pd.DataFrame, dep: str) -> pd.DataFrame:
    """Une ligne par jour vise des saisons communes, avec le nombre de feux."""
    bulletins = mdf[mdf["dep"] == dep]
    j = (bulletins[bulletins["jour"].dt.year.isin(SAISONS_COMMUNES)]
         [["jour", "n1"]].reset_index(drop=True))
    j2 = bulletins[["publication", "n2"]].copy()
    j2["jour"] = j2["publication"] + pd.Timedelta(days=2)
    j = j.merge(j2[["jour", "n2"]], on="jour", how="left")
    j["feux"] = j["jour"].map(feux.groupby("jour").size()).fillna(0).astype(int)
    return j


def pct(a: float, b: float) -> str:
    return f"{100 * a / b:.1f} %" if b else "sans objet"


def rapport_seuil(j: pd.DataFrame, nom: str, mdf_dep: pd.DataFrame,
                  feux: pd.DataFrame, criteres: str) -> list[str]:
    total_feux = int(j["feux"].sum())
    calendaire = int((feux["alerte"].dt.year.isin(SAISONS_COMMUNES)
                      & feux["alerte"].dt.month.between(6, 9)).sum())
    r = [f"### {nom}", "",
         f"- Jours vises : {len(j)} (du {j['jour'].min().date()} au "
         f"{j['jour'].max().date()}, saisons {SAISONS_COMMUNES[0]} et "
         f"{SAISONS_COMMUNES[1]})",
         f"- Criteres de l'export BDIFF : {criteres}",
         f"- Feux ces jours-la : {total_feux}",
         f"- Feux sur juin-septembre calendaire {SAISONS_COMMUNES[0]} et "
         f"{SAISONS_COMMUNES[1]} (periode de la matrice) : {calendaire}", "",
         "| Niveau niveau_j1 | Jours | Jours avec au moins un feu | "
         "Part des jours avec feu | Feux |",
         "|---|---|---|---|---|"]
    for niveau in (1, 2, 3, 4):
        b = j[j["n1"] == niveau]
        avec = int((b["feux"] > 0).sum())
        r.append(f"| {niveau} | {len(b)} | {avec} | {pct(avec, len(b))} | "
                 f"{int(b['feux'].sum())} |")

    eleve = j[j["n1"] >= 3]
    sans = int((eleve["feux"] == 0).sum())
    faible = int(j.loc[j["n1"] == 1, "feux"].sum())
    r += ["",
          f"- Jours de danger eleve (niveau_j1 >= 3) : {len(eleve)}, dont "
          f"sans aucun feu : {sans} ({pct(sans, len(eleve))}) ; avec un jour "
          f"sans feu de moins ou de plus : {pct(sans - 1, len(eleve))} ou "
          f"{pct(sans + 1, len(eleve))}",
          f"- Feux partis un jour de danger faible (niveau_j1 = 1) : "
          f"{faible} sur {total_feux} ({pct(faible, total_feux)})", "",
          "| Regle de declenchement | Jours declenches | Dont sans feu | "
          "Feux hors declenchement |",
          "|---|---|---|---|"]
    regles = {
        "niveau_j1 >= 2": j["n1"] >= 2,
        "niveau_j1 >= 3": j["n1"] >= 3,
        "niveau_j1 >= 3 et niveau_j2 de la veille >= 3":
            (j["n1"] >= 3) & (j["n2"] >= 3),
        "niveau_j1 >= 4": j["n1"] >= 4,
    }
    for libelle, masque in regles.items():
        d = j[masque]
        sans_d = int((d["feux"] == 0).sum())
        hors = int(j.loc[~masque, "feux"].sum())
        r.append(f"| {libelle} | {len(d)} | {sans_d} ({pct(sans_d, len(d))}) | "
                 f"{hors} ({pct(hors, total_feux)}) |")

    r += ["", "Jours declenches par ete (saisons communes) :", "",
          "| Regle de declenchement | " + " | ".join(
              str(a) for a in SAISONS_COMMUNES)
          + " | Moyenne par ete | Part des jours |",
          "|---|" + "---|" * (len(SAISONS_COMMUNES) + 2)]
    for libelle, niveau in (("niveau_j1 >= 1 (tous les jours)", 1),
                            ("niveau_j1 >= 2", 2), ("niveau_j1 >= 3", 3),
                            ("niveau_j1 >= 4", 4)):
        masque = j["n1"] >= niveau
        par_an = [int((masque & (j["jour"].dt.year == a)).sum())
                  for a in SAISONS_COMMUNES]
        moyenne = sum(par_an) / len(SAISONS_COMMUNES)
        r.append(f"| {libelle} | " + " | ".join(str(n) for n in par_an)
                 + f" | {moyenne:.1f} | {pct(sum(par_an), len(j))} |")

    par_saison = (mdf_dep[mdf_dep["n1"] >= 3]
                  .groupby(mdf_dep["jour"].dt.year).size())
    r += ["", "- Jours de danger eleve par saison (toutes saisons de l'indice) : "
          + ", ".join(f"{a} : {n}" for a, n in par_saison.items()), ""]

    r += ["Detail par saison (feux et jours declenches) :", "",
          "| Seuil | Saison | Jours declenches | Feux couverts | Part des feux couverts |",
          "|---|---|---|---|---|"]
    for niveau in (2, 3):
        for annee in sorted(mdf_dep["jour"].dt.year.unique()):
            jours = int(((mdf_dep["jour"].dt.year == annee)
                         & (mdf_dep["n1"] >= niveau)).sum())
            saison = j[j["jour"].dt.year == annee]
            if len(saison):
                couverts = int(saison.loc[saison["n1"] >= niveau, "feux"].sum())
                total = int(saison["feux"].sum())
                r.append(f"| niveau_j1 >= {niveau} | {annee} | {jours} | "
                         f"{couverts} sur {total} | {pct(couverts, total)} |")
            else:
                r.append(f"| niveau_j1 >= {niveau} | {annee} | {jours} | "
                         "feux exclus (ticket #61) | sans objet |")
    r.append("")
    return r


def rapport_hors_saison(feux: pd.DataFrame) -> list[str]:
    """Part des feux qui partent hors de juin a septembre (hors fenetre de l'indice)."""
    mois = feux["alerte"].dt.month
    hors = int((~mois.between(6, 9)).sum())
    return ["### Feux hors de juin a septembre (Corse-du-Sud)", "",
            f"- Feux {feux['annee'].min()}-{feux['annee'].max()} : {len(feux)}, "
            f"dont hors de juin a septembre : {hors} ({pct(hors, len(feux))})",
            ""]


# ---------------------------------------------------------------------------
# Volet zones
# ---------------------------------------------------------------------------

def rapport_zones(feux: pd.DataFrame) -> list[str]:
    n = len(feux)
    par_commune = feux["Code INSEE"].value_counts()
    noms = feux.drop_duplicates("Code INSEE").set_index("Code INSEE")[
        "Nom de la commune"]
    cumul = par_commune.cumsum() / n
    pour_moitie = int((cumul < 0.5).sum()) + 1
    top3 = par_commune.head(3)

    p1 = feux.loc[feux["annee"] <= 2015, "Code INSEE"].value_counts()
    p2 = feux.loc[feux["annee"] >= 2016, "Code INSEE"].value_counts()
    communs = [c for c in p1.head(10).index if c in set(p2.head(10).index)]
    rangs = pd.concat([p1, p2], axis=1).fillna(0)
    surface = (pd.to_numeric(feux["Surface parcourue (m2)"]) / 10000).groupby(
        feux["Code INSEE"]).sum().sort_values(ascending=False)
    surf_top3 = surface.head(3)
    top20_feux = set(par_commune.head(20).index)
    hors_top20 = [c for c in surf_top3.index if c not in top20_feux]
    spearman = rangs.corr(method="spearman").iloc[0, 1]

    return [
        "### Concentration et stabilite des feux par commune (Corse-du-Sud)", "",
        f"- Feux : {n} ({feux['annee'].min()}-{feux['annee'].max()}), "
        f"communes touchees : {par_commune.size}",
        "- Trois premieres communes : " + ", ".join(
            f"{noms[c]} {k}" for c, k in top3.items())
        + f", soit {int(top3.sum())} feux ({pct(top3.sum(), n)})",
        f"- Part des feux dans les 10 premieres communes : "
        f"{pct(par_commune.head(10).sum(), n)}",
        f"- Nombre de communes pour atteindre la moitie des feux : "
        f"{pour_moitie} sur {par_commune.size} "
        f"({pct(pour_moitie, par_commune.size)})",
        f"- Feux 2006-2015 : {int(p1.sum())} ; feux 2016-2025 : {int(p2.sum())}",
        f"- Communes presentes dans les 10 premieres des deux periodes : "
        f"{len(communs)} (" + ", ".join(noms[c] for c in communs) + ")",
        "- Correlation de rang de Spearman entre les deux periodes "
        f"(toutes communes, nombre de feux par commune) : {spearman:.2f}",
        "- Surface brulee : trois premieres communes : " + ", ".join(
            f"{noms[c]} {h:.0f} ha" for c, h in surf_top3.items())
        + f", soit {surf_top3.sum():.0f} ha sur {surface.sum():.0f} "
        f"({pct(surf_top3.sum(), surface.sum())}) ; hors des 20 communes "
        f"qui ont le plus de feux : " + (", ".join(noms[c] for c in hors_top20)
                                          if hors_top20 else "aucune"),
        "",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--mdf", nargs="+", type=Path, required=True)
    parser.add_argument("--bdiff-2a", type=Path, required=True)
    parser.add_argument("--bdiff-2b", type=Path, required=True)
    parser.add_argument("--sortie", type=Path)
    args = parser.parse_args()

    for p in [*args.mdf, args.bdiff_2a, args.bdiff_2b]:
        if not p.exists():
            print(f"Fichier introuvable : {p}", file=sys.stderr)
            return 1

    mdf = lire_mdf(args.mdf)
    feux_2a, criteres_2a = lire_bdiff(args.bdiff_2a, "2A")
    feux_2b, criteres_2b = lire_bdiff(args.bdiff_2b, "2B")

    lignes = ["# Calculs du diagnostic et de l'objectif KPI", "",
              "Genere par `src/calcul_diagnostic.py` a partir des fichiers "
              "bruts de `data/raw/`.", "",
              "## Volet seuil : Meteo des forets x BDIFF", ""]
    eleves = 0
    for dep, nom, feux, crit in (("2A", "Corse-du-Sud (2A)", feux_2a, criteres_2a),
                                 ("2B", "Haute-Corse (2B)", feux_2b, criteres_2b)):
        j = table_jours(mdf, feux, dep)
        eleves += int((j["n1"] >= 3).sum())
        lignes += rapport_seuil(j, nom, mdf[mdf["dep"] == dep], feux, crit)
    lignes += [f"- Jours de danger eleve, Corse-du-Sud et Haute-Corse "
               f"ensemble (saisons communes) : {eleves}", ""]
    lignes += rapport_hors_saison(feux_2a)
    lignes += ["## Volet zones : BDIFF par commune", ""]
    lignes += rapport_zones(feux_2a)

    texte = "\n".join(lignes)
    if args.sortie:
        args.sortie.parent.mkdir(parents=True, exist_ok=True)
        args.sortie.write_text(texte, encoding="utf-8")
        print(f"Resultats ecrits : {args.sortie}")
    else:
        print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
