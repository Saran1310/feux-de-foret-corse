"""Calculs de l'objectif KPI S1 et de la fiche d'indicateurs S2 d'Ahmed Philippe (Q1).

Refait tous les chiffres de kpi/objectif-ahmed-philippe.md et de
kpi/fiche-indicateurs-ahmed-philippe.md à partir de l'export BDIFF
de la Corse-du-Sud (type de feu F, date de première alerte du 2006-01-01 au 2025-12-31,
mêmes critères que docs/qualite/profil-bdiff.md).

Usage :
    python src/objectif_q1.py data/raw/bdiff_2A_2006_2025.csv
"""

import sys

import pandas as pd

TAILLE_LISTE = 20                     # nombre de communes prioritaires de l'objectif
TAILLES_TESTEES = (10, 15, 20, 25, 30)
ANNEES_CLASSEMENT = range(2014, 2024)  # 10 années avant les étés de référence
ANNEES_REFERENCE = (2024, 2025)        # deux derniers étés publiés
MOIS_ETE = range(6, 10)                # juin à septembre


def lire_bdiff(chemin):
    """Lit l'export BDIFF : trois lignes descriptives avant les noms de colonnes."""
    df = pd.read_csv(chemin, sep=";", skiprows=3, dtype={"Code INSEE": str})
    df["date"] = pd.to_datetime(df["Date de première alerte"])
    df["ete"] = df["date"].dt.month.isin(MOIS_ETE)
    df["ha"] = df["Surface parcourue (m2)"] / 10_000
    return df


def classement(df, annees):
    """Communes classées par nombre de feux (années entières), de la plus touchée à la moins touchée."""
    sel = df[df["Année"].isin(annees)]
    return sel.groupby("Code INSEE").size().sort_values(ascending=False, kind="stable")


def part_dans_liste(feux, liste):
    """Nombre de feux dont la commune est dans la liste, et nombre total de feux."""
    return int(feux["Code INSEE"].isin(liste).sum()), len(feux)


def pct(a, b):
    return f"{100 * a / b:.1f} %"


def main(chemin):
    df = lire_bdiff(chemin)
    ete = df[df["ete"]]
    noms = df.drop_duplicates("Code INSEE").set_index("Code INSEE")["Nom de la commune"]
    print(f"Feux lus : {len(df)}, communes : {df['Code INSEE'].nunique()}, "
          f"années {df['Année'].min()}-{df['Année'].max()}")

    # Diagnostic : concentration des feux de l'été et des années entières
    for libelle, sel in (("étés", ete), ("années entières", df)):
        cumul = sel.groupby("Code INSEE").size().sort_values(ascending=False).cumsum() / len(sel)
        print(f"Concentration ({libelle}, {len(sel)} feux) : "
              f"50 % avec {(cumul < 0.5).sum() + 1} communes, 80 % avec {(cumul < 0.8).sum() + 1}")

    # Situation de référence : liste faite sur 2014-2023, feux des étés 2024-2025
    rang = classement(df, ANNEES_CLASSEMENT)
    test = ete[ete["Année"].isin(ANNEES_REFERENCE)]
    print(f"\nSituation de référence (classement {min(ANNEES_CLASSEMENT)}-{max(ANNEES_CLASSEMENT)}, "
          f"étés {ANNEES_REFERENCE[0]}-{ANNEES_REFERENCE[1]})")
    for k in TAILLES_TESTEES:
        a, b = part_dans_liste(test, rang.index[:k])
        print(f"  {k} communes : {a} sur {b} = {pct(a, b)}")
    liste = rang.index[:TAILLE_LISTE]
    print(f"  Ex aequo à la limite : {TAILLE_LISTE}e = {rang.iloc[TAILLE_LISTE - 1]} feux, "
          f"{TAILLE_LISTE + 1}e = {rang.iloc[TAILLE_LISTE]} feux")
    for annee in ANNEES_REFERENCE:
        a, b = part_dans_liste(test[test["Année"] == annee], liste)
        print(f"  Été {annee} : {a} sur {b}")
    print("  Liste : " + ", ".join(noms[liste]))

    # Stabilité : liste des 10 années précédentes, feux de l'été suivant
    print(f"\nStabilité ({TAILLE_LISTE} communes, 10 années précédentes -> été suivant)")
    parts = []
    for annee in range(2016, 2026):
        liste_a = classement(df, range(annee - 10, annee)).index[:TAILLE_LISTE]
        a, b = part_dans_liste(ete[ete["Année"] == annee], liste_a)
        parts.append(a / b)
        print(f"  {annee} : {a} sur {b} = {pct(a, b)}")
    print(f"  Moyenne {100 * sum(parts) / len(parts):.1f} %, "
          f"min {100 * min(parts):.1f} %, max {100 * max(parts):.1f} %")

    # Garde-fou : surfaces brûlées dans la liste
    print("\nSurfaces brûlées des étés de référence dans la liste")
    for libelle, sel in (("2024-2025", test),) + tuple(
            (str(a), test[test["Année"] == a]) for a in ANNEES_REFERENCE):
        dans = sel[sel["Code INSEE"].isin(liste)]["ha"].sum()
        print(f"  {libelle} : {dans:.1f} ha sur {sel['ha'].sum():.1f} ha = {pct(dans, sel['ha'].sum())}")
    print("  Plus grands feux :")
    for _, f in test.nlargest(3, "ha").iterrows():
        print(f"    {f['Date de première alerte']} {f['Nom de la commune']} {f['ha']:.1f} ha"
              f"{'' if f['Code INSEE'] in liste else ' (hors liste)'}")

    # Surfaces 2006-2025 (années entières)
    surf = df.groupby("Code INSEE")["ha"].sum().sort_values(ascending=False)
    print(f"\nSurfaces 2006-2025 : {surf.sum():.0f} ha ; trois premières communes : "
          + ", ".join(f"{noms[c]} {v:.0f} ha" for c, v in surf.head(3).items()))

    fiche_s2(df, ete, test)


def part_surface(feux, liste):
    """Surface brûlée (ha) dans la liste, et surface totale."""
    return feux[feux["Code INSEE"].isin(liste)]["ha"].sum(), feux["ha"].sum()


def fiche_s2(df, ete, test):
    """Chiffres de kpi/fiche-indicateurs-ahmed-philippe.md (séance S2)."""
    print("\n=== Fiche d'indicateurs S2 ===")

    # Un paramètre change : k, puis la fenêtre de classement
    print("\nParamètres (I1 et I2 sur les étés 2024-2025 ; stabilité 2016-2025)")
    variantes = [(k, 10) for k in (15, 20, 25)] + [(20, n) for n in (5, 18)]
    for k, n in variantes:
        liste = classement(df, range(2024 - n, 2024)).index[:k]
        a, b = part_dans_liste(test, liste)
        h, t = part_surface(test, liste)
        ligne = f"  k={k}, fenêtre {n} ans : I1 {pct(a, b)}, I2 {pct(h, t)}"
        if k == TAILLE_LISTE:
            parts = []
            for annee in range(2016, 2026):
                liste_a = classement(df, range(annee - n, annee)).index[:k]
                parts.append(ete[ete["Année"] == annee]["Code INSEE"].isin(liste_a).mean())
            ligne += (f", stabilité moyenne {100 * sum(parts) / len(parts):.1f} %, "
                      f"minimum {100 * min(parts):.1f} %")
        print(ligne)
    print(f"  k=30, fenêtre 10 ans : I1 "
          + pct(*part_dans_liste(test, classement(df, ANNEES_CLASSEMENT).index[:30])))

    # I2 été par été, avec la surface totale (seuil plancher : 20 ha)
    print("\nI2 été par été (liste des 10 années précédentes, 20 communes)")
    for annee in range(2016, 2026):
        liste_a = classement(df, range(annee - 10, annee)).index[:TAILLE_LISTE]
        h, t = part_surface(ete[ete["Année"] == annee], liste_a)
        lu = "" if t >= 20 else " (sous le seuil plancher de 20 ha : non lu)"
        print(f"  {annee} : {pct(h, t) if t else 'sans surface'} de {t:.1f} ha{lu}")

    # KPI secondaire : nombre de communes pour la moitié des feux de l'été
    print("\nCommunes qui font la moitié des feux de l'été")
    for libelle, sel in [(str(a), ete[ete["Année"] == a]) for a in ANNEES_REFERENCE] + \
            [("2006-2025", ete)]:
        cumul = sel.groupby("Code INSEE").size().sort_values(ascending=False).cumsum() / len(sel)
        print(f"  {libelle} : {(cumul < 0.5).sum() + 1} communes ({len(sel)} feux)")

    # Lecture mensuelle : nombre de feux par mois (seuil plancher : 20 feux)
    print("\nFeux par mois, étés 2024-2025 (lecture mensuelle si 20 feux ou plus)")
    mois = test.groupby([test["Année"], test["date"].dt.month]).size()
    for (annee, m), n in mois.items():
        print(f"  {annee}-{m:02d} : {n} feux{'' if n >= 20 else ' (non lu)'}")

    # Détournement 2 : petits feux contre grands feux
    par_commune = df.groupby("Nom de la commune").agg(feux=("ha", "size"), ha=("ha", "sum"))
    for nom in ("Ajaccio", "Fozzano"):
        print(f"  {nom} 2006-2025 : {par_commune.loc[nom, 'feux']} feux, "
              f"{par_commune.loc[nom, 'ha']:.0f} ha")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
