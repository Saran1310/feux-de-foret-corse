"""Règles de qualité de la source commune (BDIFF, Corse-du-Sud), écrites comme des tests.

Chaque règle a un sélecteur, un prédicat, un seuil justifié par le profil
(docs/qualite/profil-bdiff.md) et une décision (bloquer, alerter ou tolérer).
Le script affiche le rapport de qualité puis applique la barrière de qualité :
il s'arrête avec un code d'erreur si une règle bloquante échoue.

Usage :
    python src/regles_qualite.py data/raw/bdiff_2A_2006_2025.csv

Rapport commenté : docs/qualite/regles-et-rapport-qualite.md
"""

import sys

import pandas as pd

SOUS_SURFACES = [
    "Surface forêt (m2)",
    "Surface maquis garrigues (m2)",
    "Autres surfaces naturelles hors forêt (m2)",
    "Surfaces agricoles (m2)",
    "Autres surfaces (m2)",
    "Surface autres terres boisées (m2)",
    "Surfaces non boisées naturelles (m2)",
    "Surfaces non boisées artificialisées (m2)",
    "Surfaces non boisées (m2)",
]
SEUIL_ALERTES_SIMULTANEES = 2.0   # % par année, maximum observé de 2006 à 2023 (2016)
SEUIL_VOLUME = 40.0               # % de la moyenne des 5 années précédentes, minimum observé 47 % (2018)


def lire_bdiff(chemin):
    """Lit l'export BDIFF : trois lignes descriptives avant les noms de colonnes."""
    df = pd.read_csv(chemin, sep=";", skiprows=3, dtype={"Code INSEE": str}, encoding="utf-8-sig")
    df["date"] = pd.to_datetime(df["Date de première alerte"])
    return df


def r1_alertes_simultanees(df):
    """R1, unicité : deux feux de la même commune ont-ils la même date et heure d'alerte ?"""
    en_trop = df.duplicated(["Code INSEE", "Date de première alerte"])
    parts = (en_trop.groupby(df["Année"]).mean() * 100).round(1)
    hors = parts[parts > SEUIL_ALERTES_SIMULTANEES]
    detail = ", ".join(f"{a} : {p} %" for a, p in hors.items()) or "aucune année"
    return {
        "regle": "R1 alertes simultanées (unicité)",
        "portee": "tous les feux, par année",
        "seuil": f"au plus {SEUIL_ALERTES_SIMULTANEES} % de feux en trop par année",
        "resultat": f"{int(en_trop.sum())} feux en trop sur {len(df)} ; années au-dessus : {detail}",
        "echec": not hors.empty,
        "severite": "alerter",
    }


def r2_volume(df):
    """R2, complétude des périodes : une année est-elle présente, avec un volume plausible ?"""
    par_an = df.groupby("Année").size().reindex(range(2006, 2026), fill_value=0)
    absentes = [a for a, n in par_an.items() if n == 0]
    faibles = []
    for annee in range(2011, 2026):
        moyenne = par_an.loc[annee - 5:annee - 1].mean()
        part = 100 * par_an[annee] / moyenne
        if part < SEUIL_VOLUME:
            faibles.append(f"{annee} : {part:.0f} %")
    resultats = [{
        "regle": "R2a année absente (complétude des périodes)",
        "portee": "années 2006 à 2025",
        "seuil": "0 année sans feu",
        "resultat": f"{len(absentes)} année sans feu",
        "echec": bool(absentes),
        "severite": "bloquer",
    }, {
        "regle": "R2b volume annuel (complétude des périodes)",
        "portee": "années 2011 à 2025",
        "seuil": f"au moins {SEUIL_VOLUME:.0f} % de la moyenne des 5 années précédentes",
        "resultat": ", ".join(faibles) or f"aucune année sous {SEUIL_VOLUME:.0f} %",
        "echec": bool(faibles),
        "severite": "alerter",
    }]
    return resultats


def r3_surfaces(df):
    """R3, cohérence dans la ligne : la surface parcourue égale-t-elle la somme de son détail ?"""
    detail = df[SOUS_SURFACES].sum(axis=1, min_count=1)
    avec_detail = detail.notna()
    ecart = (detail - df["Surface parcourue (m2)"]).abs() > 0
    fautives = int((avec_detail & ecart).sum())
    return {
        "regle": "R3 surfaces cohérentes (cohérence)",
        "portee": f"feux avec détail des surfaces ({int(avec_detail.sum())} lignes)",
        "seuil": "0 ligne où le détail diffère du total",
        "resultat": f"{fautives} ligne fautive",
        "echec": fautives > 0,
        "severite": "bloquer",
    }


def main(chemin):
    df = lire_bdiff(chemin)
    regles = [r1_alertes_simultanees(df), *r2_volume(df), r3_surfaces(df)]
    print("| Règle | Portée | Seuil | Résultat | Statut | Sévérité |")
    print("|---|---|---|---|---|---|")
    for r in regles:
        statut = "échec" if r["echec"] else "réussite"
        print(f"| {r['regle']} | {r['portee']} | {r['seuil']} | {r['resultat']} | {statut} | {r['severite']} |")

    # Sensibilité de l'indicateur I1 (Q1) à R1 : feux comptés une fois par commune et par minute
    ete = df[df["date"].dt.month.between(6, 9) & df["Année"].isin([2024, 2025])]
    liste = (df[df["Année"].between(2014, 2023)].groupby("Code INSEE").size()
             .sort_values(ascending=False, kind="stable").index[:20])
    evenements = ete.drop_duplicates(["Code INSEE", "Date de première alerte"])
    for libelle, sel in (("feux", ete), ("alertes distinctes", evenements)):
        n = int(sel["Code INSEE"].isin(liste).sum())
        print(f"I1 (étés 2024-2025, 20 communes) en {libelle} : {n} sur {len(sel)} = {100 * n / len(sel):.1f} %")

    bloquantes = [r["regle"] for r in regles if r["echec"] and r["severite"] == "bloquer"]
    alertes = [r["regle"] for r in regles if r["echec"] and r["severite"] == "alerter"]
    if alertes:
        print("Alertes (le chargement continue) : " + " ; ".join(alertes))
    if bloquantes:
        sys.exit("Règles bloquantes en échec : " + " ; ".join(bloquantes))
    print("Barrière de qualité : aucune règle bloquante en échec.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
