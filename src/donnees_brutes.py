"""Manifeste, verification et telechargement de la couche bronze.

data/raw/ est la couche bronze du pipeline : copie exacte des fichiers
sources, jamais modifiee (voir docs/donnees-brutes.md). Ce script prouve
qu'elle est intacte et permet de savoir si les sources ont change.

Trois commandes, depuis la racine du depot :

    python src/donnees_brutes.py telecharger [--comparer]
        Telecharge les saisons de la Meteo des forets absentes de data/raw/
        (licence ouverte). Avec --comparer, telecharge la version actuelle
        de chaque saison dans un dossier temporaire et la compare au
        manifeste, sans toucher a data/raw/. Les exports BDIFF se font a la
        main : procedure dans docs/donnees-brutes.md.

    python src/donnees_brutes.py manifeste
        Decrit chaque fichier present dans data/raw/ (taille, nombre de
        lignes, empreinte SHA-256, date du fichier, criteres d'export) et
        ecrit data/manifeste.csv. A lancer quand un fichier de reference est
        ajoute ; le manifeste est versionne. Un fichier inchange garde la
        date du manifeste precedent.

    python src/donnees_brutes.py verifier
        Compare les fichiers de data/raw/ au manifeste. S'arrete avec un code
        d'erreur si un fichier manque ou differe : les resultats ne seraient
        plus ceux du depot.

L'empreinte SHA-256 change des qu'un seul octet du fichier change : deux
fichiers de meme empreinte ont exactement le meme contenu.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import sys
import tempfile
import urllib.request
from datetime import datetime
from pathlib import Path

DOSSIER = Path("data/raw")
MANIFESTE = Path("data/manifeste.csv")

# Fichiers attendus dans data/raw/ : source, mode d'obtention.
FICHIERS = {
    "bdiff_2A_2006_2025.csv": {
        "source": "BDIFF, Corse-du-Sud",
        "obtention": "export manuel, procedure dans docs/donnees-brutes.md",
    },
    "bdiff_2B_2006_2025.csv": {
        "source": "BDIFF, Haute-Corse",
        "obtention": "export manuel, procedure dans docs/donnees-brutes.md",
    },
    "bdiff_france_2024_2025.csv": {
        "source": "BDIFF, France entiere, 2024-2025",
        "obtention": "export manuel, procedure dans docs/donnees-brutes.md",
    },
    "mdf_2024.csv.gz": {
        "source": "Archives de la Meteo des forets, saison 2024",
        "obtention": "https://www.data.gouv.fr/api/1/datasets/r/"
                     "59f2c103-f8d5-4216-9e46-de2327f4dc5a",
    },
    "mdf_2025.csv.gz": {
        "source": "Archives de la Meteo des forets, saison 2025",
        "obtention": "https://www.data.gouv.fr/api/1/datasets/r/"
                     "c1f8f7c8-e8cc-4d70-9372-43da3c878c81",
    },
    "mdf_2026.csv.gz": {
        "source": "Archives de la Meteo des forets, saison 2026",
        "obtention": "https://www.data.gouv.fr/api/1/datasets/r/"
                     "14f5607c-68b1-4b91-be36-b1265f309c51",
    },
}

COLONNES = ["fichier", "source", "obtention", "date_du_fichier", "octets",
            "lignes_de_donnees", "sha256", "criteres"]


def sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def lire_lignes(chemin: Path) -> list[str]:
    ouvrir = gzip.open if chemin.suffix == ".gz" else open
    with ouvrir(chemin, "rt", encoding="utf-8-sig") as f:
        return f.read().splitlines()


def decrire(nom: str) -> dict:
    """Decrit un fichier brut, sans le modifier."""
    chemin = DOSSIER / nom
    try:
        lignes = [l for l in lire_lignes(chemin) if l.strip()]
    except (OSError, UnicodeDecodeError, EOFError):
        lignes = None
    if lignes is None:
        criteres, donnees = "fichier illisible", "illisible"
    elif nom.startswith("bdiff"):
        # Des lignes d'information (leur nombre depend de l'export), puis
        # l'en-tete, qui commence par "Annee".
        entete = next(i for i, l in enumerate(lignes) if l.startswith("Ann"))
        criteres = next(l for l in lignes[:entete] if l.startswith('"Crit'))
        criteres = criteres.replace('";"', " ; ").strip('"')
        donnees = len(lignes) - entete - 1
    else:
        criteres = ""
        donnees = len(lignes) - 1
    date = datetime.fromtimestamp(chemin.stat().st_mtime).date().isoformat()
    return {"fichier": nom, "source": FICHIERS[nom]["source"],
            "obtention": FICHIERS[nom]["obtention"], "date_du_fichier": date,
            "octets": chemin.stat().st_size, "lignes_de_donnees": donnees,
            "sha256": sha256(chemin), "criteres": criteres}


def telecharger(comparer: bool) -> int:
    DOSSIER.mkdir(parents=True, exist_ok=True)
    references = {}
    if comparer:
        if not MANIFESTE.exists():
            print(f"{MANIFESTE} introuvable.", file=sys.stderr)
            return 1
        with open(MANIFESTE, encoding="utf-8") as f:
            references = {l["fichier"]: l["sha256"]
                          for l in csv.DictReader(f)}
    changes = 0
    for nom, info in FICHIERS.items():
        if not info["obtention"].startswith("https://"):
            continue
        cible = DOSSIER / nom
        if comparer:
            with tempfile.TemporaryDirectory() as dossier:
                tmp = Path(dossier) / nom
                try:
                    urllib.request.urlretrieve(info["obtention"], tmp)
                except OSError as erreur:
                    print(f"ECHEC     {nom} : telechargement impossible "
                          f"({erreur})")
                    changes += 1
                    continue
                if sha256(tmp) == references.get(nom):
                    print(f"IDENTIQUE {nom} : la source n'a pas change")
                else:
                    print(f"CHANGE    {nom} : la version en ligne differe de "
                          "la couche bronze (decision du groupe pour "
                          "l'adopter, voir docs/donnees-brutes.md)")
                    changes += 1
            continue
        if cible.exists():
            print(f"{nom} : deja present, non remplace (la couche bronze "
                  "n'est jamais modifiee)")
            continue
        print(f"{nom} : telechargement...")
        try:
            urllib.request.urlretrieve(info["obtention"], cible)
        except OSError as erreur:
            cible.unlink(missing_ok=True)
            print(f"{nom} : telechargement impossible ({erreur})",
                  file=sys.stderr)
            return 1
        print(f"{nom} : {cible.stat().st_size} octets")
    if comparer:
        return 1 if changes else 0
    if not comparer:
        print("Exports BDIFF : a faire a la main, voir docs/donnees-brutes.md")
    return 0


def ecrire_manifeste() -> int:
    manquants = [n for n in FICHIERS if not (DOSSIER / n).exists()]
    if manquants:
        print("Fichiers absents de data/raw/ : " + ", ".join(manquants),
              file=sys.stderr)
        return 1
    anciennes = {}
    if MANIFESTE.exists():
        with open(MANIFESTE, encoding="utf-8") as f:
            anciennes = {l["fichier"]: l for l in csv.DictReader(f)}
    with open(MANIFESTE, "w", newline="", encoding="utf-8") as f:
        ecrivain = csv.DictWriter(f, fieldnames=COLONNES)
        ecrivain.writeheader()
        for nom in FICHIERS:
            ligne = decrire(nom)
            ancienne = anciennes.get(nom)
            if ancienne and ancienne["sha256"] == ligne["sha256"]:
                # Fichier inchange : la date du disque change a chaque
                # clonage, celle du manifeste reste la date d'origine.
                ligne["date_du_fichier"] = ancienne["date_du_fichier"]
            ecrivain.writerow(ligne)
    print(f"Manifeste ecrit : {MANIFESTE} ({len(FICHIERS)} fichiers)")
    return 0


def verifier() -> int:
    if not MANIFESTE.exists():
        print(f"{MANIFESTE} introuvable : lancer d'abord la commande "
              "manifeste.", file=sys.stderr)
        return 1
    with open(MANIFESTE, encoding="utf-8") as f:
        attendus = list(csv.DictReader(f))
    problemes = 0
    for ligne in attendus:
        nom = ligne["fichier"]
        if not (DOSSIER / nom).exists():
            print(f"MANQUANT  {nom} : {ligne['obtention']}")
            problemes += 1
            continue
        actuel = decrire(nom)
        if actuel["sha256"] == ligne["sha256"]:
            print(f"OK        {nom} ({actuel['lignes_de_donnees']} lignes)")
        else:
            print(f"DIFFERENT {nom} : {actuel['lignes_de_donnees']} "
                  f"lignes (fichier lu) contre {ligne['lignes_de_donnees']} "
                  "dans le manifeste "
                  f"(fichier de reference date du {ligne['date_du_fichier']}). "
                  "La couche bronze doit rester identique : pour revenir "
                  "au fichier du depot, git restore data/raw/" + nom)
            problemes += 1
    if problemes:
        print(f"{problemes} probleme(s) : voir docs/donnees-brutes.md, "
              "section Mises a jour des sources.", file=sys.stderr)
        return 1
    print("Tous les fichiers bruts sont identiques a ceux du manifeste.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = parser.add_subparsers(dest="commande", required=True)
    t = sous.add_parser("telecharger")
    t.add_argument("--comparer", action="store_true")
    sous.add_parser("manifeste")
    sous.add_parser("verifier")
    args = parser.parse_args()
    if args.commande == "telecharger":
        return telecharger(args.comparer)
    if args.commande == "manifeste":
        return ecrire_manifeste()
    return verifier()


if __name__ == "__main__":
    sys.exit(main())