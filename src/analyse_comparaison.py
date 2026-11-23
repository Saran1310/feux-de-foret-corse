"""Compare, par niveau de la Météo des forêts, la part des jours avec au moins un feu
en Corse-du-Sud (2A), en Haute-Corse (2B) et dans les autres départements.

Usage : python src/analyse_comparaison.py bdiff_france.csv mdf_2024.csv mdf_2025.csv
Règles : jour d'un bulletin = date de publication (heure de Paris) + 1 jour ; niveau = niveau_j1 ;
feux de type F ; un jour-département compte s'il a au moins un feu (date de première alerte).
"""
import sys
import pandas as pd

MEDITERRANEE = ["04", "05", "06", "07", "11", "13", "26", "30", "34", "48", "66", "83", "84"]


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((c - r) / d * 100, (c + r) / d * 100)


def newcombe(k1, n1, k2, n2):
    """Intervalle à 95 % de la différence p1 - p2 (méthode de Newcombe, jours supposés indépendants)."""
    p1, p2 = k1 / n1 * 100, k2 / n2 * 100
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    return (p1 - p2 - ((p1 - l1) ** 2 + (u2 - p2) ** 2) ** 0.5,
            p1 - p2 + ((u1 - p1) ** 2 + (p2 - l2) ** 2) ** 0.5)


def lire_bdiff(chemin):
    with open(chemin, encoding="utf-8-sig") as f:
        ligne = next(i for i, t in enumerate(f) if t.startswith("Année"))
    d = pd.read_csv(chemin, sep=";", skiprows=ligne, encoding="utf-8-sig",
                    dtype={"Département": str}, low_memory=False)
    d["num_dep"] = d["Département"].str.zfill(2)
    d["jour"] = pd.to_datetime(d["Date de première alerte"]).dt.normalize()
    return d


def lire_mdf(chemins):
    m = pd.concat([pd.read_csv(c, sep=None, engine="python", dtype=str) for c in chemins])
    m["num_dep"] = m["num_dep"].str.zfill(2)
    pub = pd.to_datetime(m["date"], utc=True).dt.tz_convert("Europe/Paris").dt.normalize().dt.tz_localize(None)
    m["jour"] = pub + pd.Timedelta(days=1)
    m["niveau"] = m["niveau_j1"].astype(int)
    return m[["num_dep", "jour", "niveau"]]


bdiff = lire_bdiff(sys.argv[1])
mdf = lire_mdf(sys.argv[2:])
feux = bdiff.groupby(["num_dep", "jour"]).size().rename("feux").reset_index()
x = mdf.merge(feux, on=["num_dep", "jour"], how="left").fillna({"feux": 0})
x["groupe"] = x.num_dep.map(lambda v: "2A" if v == "2A" else "2B" if v == "2B" else "Autres")
x["annee"] = x.jour.dt.year

print("Jours-départements :", len(x), "| départements :", x.num_dep.nunique())
print("Jours par saison :", x[x.num_dep == "2A"].groupby("annee").size().to_dict())
print("Premier et dernier jour :", x.jour.min().date(), x.jour.max().date())
print("Feux BDIFF lus :", len(bdiff), "| dans la fenêtre :", int(x.feux.sum()),
      "| par groupe :", x.groupby("groupe").feux.sum().astype(int).to_dict())


def tableau(df, titre):
    print("\n==", titre)
    for g, sg in df.groupby("groupe"):
        for n, s in sg.groupby("niveau"):
            k = int((s.feux > 0).sum())
            lo, hi = wilson(k, len(s))
            print(f"{g:7s} niveau {n}: {len(s):6d} jours, {k:5d} avec feu = {100*k/len(s):5.1f} % "
                  f"[{lo:4.1f} - {hi:4.1f}], feux/jour {s.feux.sum()/len(s):.2f}")


tableau(x, "Part des jours avec au moins un feu, par niveau (2024-2025)")
tableau(x[x.annee == 2024], "2024 seul")
tableau(x[x.annee == 2025], "2025 seul")
y = x[x.num_dep.isin(MEDITERRANEE)].copy()
y["groupe"] = "Mediterr."
tableau(y, "Contrôle : 13 départements méditerranéens " + ",".join(MEDITERRANEE))

print("\n== Écarts du 2A (points de pourcentage)")
ref = {}
for g, sg in x.groupby("groupe"):
    for n, s in sg.groupby("niveau"):
        ref[(g, n)] = 100 * (s.feux > 0).mean()
for n in (1, 2, 3):
    print(f"niveau {n}: 2A-2B {ref[('2A', n)]-ref[('2B', n)]:+.1f} | 2A-Autres {ref[('2A', n)]-ref[('Autres', n)]:+.1f}")

print("\n== Règle 'niveau >= seuil'")
for g, sg in x.groupby("groupe"):
    for s in (2, 3):
        a = sg[sg.niveau >= s]
        print(f"{g:7s} seuil {s}: {len(a)/len(sg)*100:5.1f} % des jours déclenchés, "
              f"{a.feux.sum()/sg.feux.sum()*100:5.1f} % des feux couverts, "
              f"{(a.feux==0).mean()*100:5.1f} % des jours déclenchés sans feu")


def comptes(df, n):
    s = df[df.niveau == n]
    return int((s.feux > 0).sum()), len(s)


print("\n== Écart du 2A avec chaque groupe, avec l'intervalle à 95 % de la différence (points)")
x_med = x[x.num_dep.isin(MEDITERRANEE)]
groupes = {"2B": x[x.groupe == "2B"], "Autres": x[x.groupe == "Autres"], "Mediterr.": x_med}
for n in (1, 2, 3):
    k1, n1 = comptes(x[x.groupe == "2A"], n)
    for nom, g in groupes.items():
        k2, n2 = comptes(g, n)
        lo, hi = newcombe(k1, n1, k2, n2)
        print(f"niveau {n}: 2A - {nom:9s} {100*k1/n1-100*k2/n2:+5.1f}  [{lo:+5.1f} ; {hi:+5.1f}]")

print("\n== Autres départements : proportion globale ou moyenne des proportions par département")
for n in (1, 2, 3):
    a = x[(x.groupe == "Autres") & (x.niveau == n)]
    glob = 100 * (a.feux > 0).mean()
    par_dep = a.groupby("num_dep").apply(lambda t: (t.feux > 0).mean() * 100, include_groups=False)
    print(f"niveau {n}: globale {glob:.1f} % | moyenne de {len(par_dep)} départements {par_dep.mean():.1f} % | médiane {par_dep.median():.1f} %")

print("\n== Sensibilité : dates BDIFF lues en UTC puis converties à l'heure de Paris")
b = bdiff.copy()
b["jour"] = (pd.to_datetime(b["Date de première alerte"]).dt.tz_localize("UTC")
             .dt.tz_convert("Europe/Paris").dt.normalize().dt.tz_localize(None))
f2 = b.groupby(["num_dep", "jour"]).size().rename("feux").reset_index()
x2 = mdf.merge(f2, on=["num_dep", "jour"], how="left").fillna({"feux": 0})
x2["groupe"] = x2.num_dep.map(lambda v: "2A" if v == "2A" else "2B" if v == "2B" else "Autres")
for g, sg in x2.groupby("groupe"):
    print(g, {int(n): round(100 * (t.feux > 0).mean(), 1) for n, t in sg.groupby("niveau") if n < 4})

# ---------------------------------------------------------------------------
# Fiche d'indicateurs S2 (kpi/fiche-indicateurs-saran-diabagate.md)
# ---------------------------------------------------------------------------
print("\n\n######## Fiche d'indicateurs S2 ########")

print("\n== Faisabilité : champs utilisés et lignes utilisables")
n_feux = len(bdiff)
for c in ["Département", "Code INSEE", "Date de première alerte"]:
    print(f"BDIFF {c} : {int(bdiff[c].notna().sum())} renseignés sur {n_feux}")
print("BDIFF dates illisibles :", int(pd.to_datetime(bdiff["Date de première alerte"], errors="coerce").isna().sum()))
brut = pd.concat([pd.read_csv(c, sep=None, engine="python", dtype=str) for c in sys.argv[2:]])
for c in ["date", "num_dep", "niveau_j1"]:
    print(f"Météo des forêts {c} : {int(brut[c].notna().sum())} renseignés sur {len(brut)}")
print("Météo des forêts niveau_j1 hors 1 à 4 :", int((~brut["niveau_j1"].isin(["1", "2", "3", "4"])).sum()))
print("Météo des forêts doublons département et date :", int(brut.duplicated(["num_dep", "date"]).sum()))
print("Départements couverts :", x.num_dep.nunique(), "| jours par département :", sorted(x.groupby("num_dep").size().unique().tolist()))
absents = sorted(set(bdiff.num_dep) - set(x.num_dep))
dans_fenetre = int(x.feux.sum())
hors_dep = int(bdiff.num_dep.isin(absents).sum())
print(f"Feux BDIFF : {n_feux} = {dans_fenetre} dans la fenêtre + {n_feux - dans_fenetre - hors_dep} hors fenêtre (avant le 4 juin ou après le 1er octobre) + {hors_dep} dans des départements absents de la Météo des forêts {absents}")

print("\n== Taille des échantillons : jours du 2A par saison et par niveau")
print(x[x.groupe == "2A"].groupby(["annee", "niveau"]).size().to_dict())

print("\n== Écart du 2A avec chaque référence, par saison (points) : intervalle de la différence et largeur")
references = {"Autres": x[x.groupe == "Autres"], "2B": x[x.groupe == "2B"], "Mediterr.": x_med}
for libelle, sous in [("2024", x[x.annee == 2024]), ("2025", x[x.annee == 2025]), ("2024-2025", x)]:
    for n in (1, 2):
        k1, n1 = comptes(sous[sous.groupe == "2A"], n)
        for nom, g in references.items():
            gs = g[g.jour.isin(sous.jour.unique())]
            k2, n2 = comptes(gs, n)
            lo, hi = newcombe(k1, n1, k2, n2)
            print(f"{libelle:9s} niveau {n} : 2A {k1}/{n1} = {100*k1/n1:4.1f} % | {nom:9s} {k2}/{n2} = {100*k2/n2:4.1f} % "
                  f"| écart {100*k1/n1-100*k2/n2:+5.1f} [{lo:+5.1f} ; {hi:+5.1f}], largeur {hi-lo:4.1f}")