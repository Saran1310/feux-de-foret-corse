"""Visualisations du projet, faites a partir de la couche or.

Lit l'entrepot construit par src/pipeline.py (data/processed/entrepot.duckdb)
et produit, dans dashboard/ :

- quatre graphiques PNG, un par question du decideur (directeur du SDIS 2A) ;
- dashboard/README.md : les graphiques, leur message, le tableau de chiffres
  de chaque graphique et la mention des sources. GitHub l'affiche
  directement.

Tous les chiffres des titres et des tableaux sont calcules ici depuis la
couche or : aucun n'est ecrit a la main.

Utilisation, depuis la racine du depot :

    python src/pipeline.py
    python src/dataviz.py
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import duckdb
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ENTREPOT = Path("data/processed/entrepot.duckdb")
SORTIE = Path("dashboard")

# Palette de reference (skill dataviz) : une teinte pour la serie, une
# seconde pour l'element mis en avant ; textes en encre neutre.
SERIE = "#2a78d6"
MISE_EN_AVANT = "#eb6834"
TEXTE = "#0b0b0b"
TEXTE_2 = "#52514e"
GRILLE = "#e4e3df"
FOND = "#fcfcfb"

SOURCE = ("Fait à partir de la base BDIFF, https://bdiff.agriculture.gouv.fr "
          "(droits de reproduction réservés et strictement limités), et des "
          "Archives de la Météo des forêts, Météo-France, data.gouv.fr "
          "(Licence Ouverte 2.0).")


def fr(x: float, decimales: int = 1) -> str:
    """Nombre au format francais : virgule decimale, espace des milliers."""
    texte = f"{x:,.{decimales}f}".replace(",", " ").replace(".", ",")
    return texte


def style(ax: plt.Axes, axe_valeurs: str = "y") -> None:
    ax.set_facecolor(FOND)
    for cote in ("top", "right", "left"):
        ax.spines[cote].set_visible(False)
    ax.spines["bottom"].set_color(GRILLE)
    ax.tick_params(colors=TEXTE_2, length=0, labelsize=9)
    ax.grid(axis=axe_valeurs, color=GRILLE, linewidth=0.8)
    ax.set_axisbelow(True)


def figure(titre: str, sous_titre: str, hauteur: float = 4.6):
    """Figure avec titre-message et sous-titre, coupes s'ils sont longs."""
    titre_l = textwrap.wrap(titre, 78)
    sous_l = textwrap.wrap(sous_titre, 112)
    fig, ax = plt.subplots(figsize=(9, hauteur), dpi=150)
    fig.patch.set_facecolor(FOND)
    pouce = 1 / (hauteur * 72)  # une unite de taille de police, en fraction
    y = 1 - 10 * pouce
    fig.text(0.01, y, "\n".join(titre_l), fontsize=12.5, fontweight="bold",
             color=TEXTE, va="top", linespacing=1.3)
    y -= (12.5 * 1.3 * len(titre_l) + 6) * pouce
    fig.text(0.01, y, "\n".join(sous_l), fontsize=9.5, color=TEXTE_2,
             va="top", linespacing=1.3)
    y -= (9.5 * 1.3 * len(sous_l) + 18) * pouce
    fig.text(0.01, 0.015, "Source : fait à partir de la base BDIFF "
             "(droits de reproduction réservés et strictement limités) et de "
             "la Météo des forêts (Météo-France).", fontsize=7,
             color=TEXTE_2, va="bottom")
    fig._haut = y
    return fig, ax


def enregistrer(fig: plt.Figure, nom: str) -> str:
    fig.subplots_adjust(left=0.08, right=0.98, top=fig._haut, bottom=0.14)
    chemin = SORTIE / nom
    fig.savefig(chemin, facecolor=FOND, metadata={"Software": None})
    plt.close(fig)
    return nom


def tableau(entetes: list[str], lignes: list[list[str]]) -> list[str]:
    r = ["| " + " | ".join(entetes) + " |",
         "|" + "|".join("---" for _ in entetes) + "|"]
    r += ["| " + " | ".join(l) + " |" for l in lignes]
    return r


# ---------------------------------------------------------------------------
# 1. Synthese : evolution du nombre de feux
# ---------------------------------------------------------------------------

def feux_par_an(con: duckdb.DuckDBPyConnection) -> list[str]:
    rows = con.execute("""
        SELECT d.annee, count(*), sum(f.surface_parcourue_ha)
        FROM gold.fait_feu f JOIN gold.dim_date d USING (id_date)
        WHERE f.departement = '2A' GROUP BY 1 ORDER BY 1
    """).fetchall()
    annees = [r[0] for r in rows]
    feux = {r[0]: r[1] for r in rows}
    ha = {r[0]: r[2] for r in rows}
    ref = [a for a in annees if 2015 <= a <= 2024]
    moyenne = sum(feux[a] for a in ref) / len(ref)
    moyenne_ha = sum(ha[a] for a in ref) / len(ref)
    derniere = annees[-1]
    ecart = 100 * (feux[derniere] - moyenne) / moyenne

    pires = sorted(sorted(annees, key=lambda a: ha[a])[-2:])
    grands = {a: con.execute(f"""
        SELECT 100 * sum(x) / {ha[a]} FROM (
            SELECT f.surface_parcourue_ha AS x
            FROM gold.fait_feu f JOIN gold.dim_date d USING (id_date)
            WHERE f.departement = '2A' AND d.annee = {a}
            ORDER BY 1 DESC LIMIT 3)""").fetchall()[0][0] for a in pires}

    titre = (f"{derniere} : {feux[derniere]} feux de forêt en Corse-du-Sud, "
             f"{fr(abs(ecart), 0)} % de moins que la moyenne 2015-2024 "
             f"({fr(moyenne, 0)})")
    fig, ax = figure(titre, "Nombre de feux par année, 2006-2025 "
                     "(Corse-du-Sud, feux de forêt de la BDIFF)")
    couleurs = [MISE_EN_AVANT if a == derniere else SERIE for a in annees]
    ax.bar(annees, [feux[a] for a in annees], width=0.62, color=couleurs,
           edgecolor=FOND, linewidth=1)
    ax.hlines(moyenne, 2014.6, 2024.4, colors=TEXTE, linestyles="--",
              linewidth=1.2)
    ax.text(2022, moyenne + 10, f"moyenne 2015-2024 : {fr(moyenne, 0)}",
            ha="center", fontsize=8.5, color=TEXTE,
            bbox={"facecolor": FOND, "edgecolor": "none", "pad": 1.5})
    ax.text(derniere, feux[derniere] + 8, str(feux[derniere]), ha="center",
            fontsize=8.5, color=TEXTE, fontweight="bold")
    ax.set_xticks(annees[::2] + ([derniere] if derniere not in annees[::2]
                                 else []))
    style(ax)
    nom = enregistrer(fig, "1-feux-par-an.png")

    md = ["## 1. Synthèse", "", f"**{titre}**", "", f"![{titre}]({nom})", "",
          f"- Moyenne 2015-2024 : {fr(moyenne, 1)} feux par an et "
          f"{fr(moyenne_ha, 0)} ha brûlés par an ; {derniere} : "
          f"{feux[derniere]} feux et {fr(ha[derniere], 0)} ha.",
          "- Le nombre de feux ne dit pas la surface brûlée : "
          + " ; ".join(f"en {a}, les 3 plus grands feux font "
                       f"{fr(grands[a])} % des {fr(ha[a], 0)} ha brûlés"
                       for a in pires) + ".", ""]
    md += tableau(["Année", "Feux", "Surface brûlée (ha)"],
                  [[str(a), str(feux[a]), fr(ha[a], 1)] for a in annees])
    return md + [""]


# ---------------------------------------------------------------------------
# 2. Pourquoi : le niveau de danger prevu et les feux observes
# ---------------------------------------------------------------------------

def danger_et_feux(con: duckdb.DuckDBPyConnection) -> list[str]:
    rows = con.execute("""
        WITH j AS (
            SELECT d.niveau_j1,
                   (SELECT count(*) FROM gold.fait_feu f
                    WHERE f.id_date = d.id_date AND f.departement = '2A')
                       AS feux
            FROM gold.fait_danger_jour d JOIN gold.dim_date USING (id_date)
            WHERE d.departement = '2A' AND annee IN (2024, 2025))
        SELECT niveau_j1, count(*), sum(CAST(feux > 0 AS INTEGER)),
               sum(feux)
        FROM j GROUP BY 1 ORDER BY 1
    """).fetchall()
    niveaux = [r[0] for r in rows]
    jours = {r[0]: r[1] for r in rows}
    avec = {r[0]: r[2] for r in rows}
    feux = {r[0]: r[3] for r in rows}
    part = {n: 100 * avec[n] / jours[n] for n in niveaux}
    eleve_j = sum(jours[n] for n in niveaux if n >= 3)
    eleve_sans = sum(jours[n] - avec[n] for n in niveaux if n >= 3)

    titre = (f"Plus le danger prévu est élevé, plus les feux sont fréquents, "
             f"mais {eleve_sans} des {eleve_j} jours de danger élevé sont "
             f"passés sans feu")
    fig, ax = figure(titre, "Part des jours avec au moins un feu, selon le "
                     "niveau de danger prévu la veille (Corse-du-Sud, étés "
                     "2024 et 2025). En orange : danger élevé.")
    noms = {1: "1 - faible", 2: "2 - modéré", 3: "3 - élevé",
            4: "4 - très élevé"}
    x = list(range(len(niveaux)))
    couleurs = [MISE_EN_AVANT if n >= 3 else SERIE for n in niveaux]
    ax.bar(x, [part[n] for n in niveaux], width=0.5, color=couleurs,
           edgecolor=FOND, linewidth=1)
    for i, n in enumerate(niveaux):
        ax.text(i, part[n] + 1.5, f"{fr(part[n])} %", ha="center",
                fontsize=9.5, color=TEXTE, fontweight="bold")
        ax.text(i, part[n] / 2, f"{avec[n]} jours\nsur {jours[n]}",
                ha="center", va="center", fontsize=8, color="white")
    ax.set_xticks(x, [noms[n] for n in niveaux])
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0f} %")
    style(ax)
    nom = enregistrer(fig, "2-danger-et-feux.png")

    md = ["## 2. Pourquoi", "", f"**{titre}**", "", f"![{titre}]({nom})", "",
          "- Niveau prévu la veille (`niveau_j1` de la Météo des forêts) ; "
          "un feu est rattaché au jour de sa première alerte.",
          f"- Les jours de danger faible ne sont pas sans risque : "
          f"{feux[1]} feux sur {sum(feux.values())} ({fr(100 * feux[1] / sum(feux.values()))} %) "
          "ont éclaté un jour de niveau 1.",
          "- Aucun jour de niveau 4 en Corse-du-Sud sur ces deux étés.", ""]
    md += tableau(["Niveau prévu", "Jours", "Jours avec au moins un feu",
                   "Part des jours avec feu", "Feux"],
                  [[noms[n], str(jours[n]), str(avec[n]), f"{fr(part[n])} %",
                    str(feux[n])] for n in niveaux])
    return md + [""]


# ---------------------------------------------------------------------------
# 3. Detail : ou ont lieu les feux
# ---------------------------------------------------------------------------

def communes(con: duckdb.DuckDBPyConnection) -> list[str]:
    rows = con.execute("""
        SELECT c.nom_commune, count(*) AS feux
        FROM gold.fait_feu f JOIN gold.dim_commune c USING (code_insee)
        WHERE f.departement = '2A' GROUP BY 1 ORDER BY 2 DESC, 1
    """).fetchall()
    total = sum(r[1] for r in rows)
    top = rows[:15]
    part3 = 100 * sum(r[1] for r in rows[:3]) / total
    part10 = 100 * sum(r[1] for r in rows[:10]) / total
    cumul, moitie = 0, 0
    for i, r in enumerate(rows, 1):
        cumul += r[1]
        if cumul >= total / 2:
            moitie = i
            break

    titre = (f"Les feux sont concentrés : {moitie} communes sur {len(rows)} "
             f"ont eu la moitié des feux de 2006 à 2025")
    fig, ax = figure(titre, "Nombre de feux par commune, 15 premières "
                     "communes (Corse-du-Sud, 2006-2025). En orange : les 3 "
                     "premières", hauteur=5.6)
    noms = [r[0] for r in top][::-1]
    valeurs = [r[1] for r in top][::-1]
    couleurs = [MISE_EN_AVANT if i >= len(top) - 3 else SERIE
                for i in range(len(top))]
    ax.barh(noms, valeurs, height=0.62, color=couleurs, edgecolor=FOND,
            linewidth=1)
    for y, v in enumerate(valeurs):
        ax.text(v + 3, y, str(v), va="center", fontsize=8, color=TEXTE)
    style(ax, "x")
    ax.tick_params(axis="y", labelsize=8.5, labelcolor=TEXTE)
    nom = enregistrer_gauche(fig, "3-feux-par-commune.png", 0.2)

    md = ["## 3. Détail", "", f"**{titre}**", "", f"![{titre}]({nom})", "",
          f"- Les 3 premières communes (en orange) : {fr(part3)} % des feux ; "
          f"les 10 premières : {fr(part10)} %.",
          "- Limite : le classement n'est pas rapporté à la surface boisée de "
          "chaque commune ; les grandes communes ressortent mécaniquement "
          "(voir D-008).", ""]
    md += tableau(["Rang", "Commune", "Feux", "Part des feux"],
                  [[str(i), r[0], str(r[1]), f"{fr(100 * r[1] / total)} %"]
                   for i, r in enumerate(top, 1)])
    return md + [""]


def enregistrer_gauche(fig: plt.Figure, nom: str, gauche: float) -> str:
    fig.subplots_adjust(left=gauche, right=0.95, top=fig._haut, bottom=0.12)
    fig.savefig(SORTIE / nom, facecolor=FOND, metadata={"Software": None})
    plt.close(fig)
    return nom


# ---------------------------------------------------------------------------
# 4. Detail : ou brule la surface
# ---------------------------------------------------------------------------

def surfaces(con: duckdb.DuckDBPyConnection) -> list[str]:
    rows = con.execute("""
        SELECT c.nom_commune, sum(f.surface_parcourue_ha) AS ha,
               count(*) AS feux
        FROM gold.fait_feu f JOIN gold.dim_commune c USING (code_insee)
        WHERE f.departement = '2A' GROUP BY 1 ORDER BY 2 DESC, 1
    """).fetchall()
    classement = con.execute("""
        SELECT c.nom_commune FROM gold.fait_feu f
        JOIN gold.dim_commune c USING (code_insee)
        WHERE f.departement = '2A' GROUP BY 1 ORDER BY count(*) DESC, 1
    """).fetchall()
    rang_feux = {r[0]: i for i, r in enumerate(classement, 1)}
    total = sum(r[1] for r in rows)
    top = rows[:10]
    part3 = 100 * sum(r[1] for r in rows[:3]) / total
    hors = [r[0] for r in rows[:3] if rang_feux[r[0]] > 20]

    titre = (f"La surface brûlée est encore plus concentrée : "
             f"{fr(part3)} % des hectares dans 3 communes")
    fig, ax = figure(titre, "Surface brûlée par commune en hectares, 10 "
                     "premières communes (Corse-du-Sud, 2006-2025). En "
                     "orange : communes hors des 20 qui ont le plus de feux.",
                     hauteur=5.0)
    noms = [r[0] for r in top][::-1]
    valeurs = [r[1] for r in top][::-1]
    couleurs = [MISE_EN_AVANT if rang_feux[n] > 20 else SERIE for n in noms]
    ax.barh(noms, valeurs, height=0.62, color=couleurs, edgecolor=FOND,
            linewidth=1)
    for y, v in enumerate(valeurs):
        ax.text(v + 30, y, fr(v, 0), va="center", fontsize=8, color=TEXTE)
    ax.set_xlim(0, max(valeurs) * 1.1)
    ax.xaxis.set_major_formatter(lambda v, _: fr(v, 0))
    style(ax, "x")
    ax.tick_params(axis="y", labelsize=8.5, labelcolor=TEXTE)
    nom = enregistrer_gauche(fig, "4-surface-par-commune.png", 0.2)

    md = ["## 4. Détail", "", f"**{titre}**", "", f"![{titre}]({nom})", "",
          f"- {fr(sum(r[1] for r in rows[:3]), 0)} ha sur {fr(total, 0)} "
          f"brûlés dans {', '.join(r[0] for r in rows[:2])} et {rows[2][0]}.",
          f"- {' et '.join(hors)} ne figurent pas parmi les 20 communes qui ont "
          "le plus de feux : quelques grands feux suffisent. Viser seulement "
          "les communes aux feux nombreux ne protège pas les hectares.", ""]
    md += tableau(["Rang", "Commune", "Surface brûlée (ha)",
                   "Part de la surface", "Feux", "Rang par nombre de feux"],
                  [[str(i), r[0], fr(r[1], 1), f"{fr(100 * r[1] / total)} %",
                    str(r[2]), str(rang_feux[r[0]])]
                   for i, r in enumerate(top, 1)])
    return md + [""]


def main() -> int:
    if not ENTREPOT.exists():
        print(f"{ENTREPOT} introuvable : lancer d'abord python src/pipeline.py",
              file=sys.stderr)
        return 1
    SORTIE.mkdir(exist_ok=True)
    plt.rcParams["font.family"] = "DejaVu Sans"
    con = duckdb.connect(str(ENTREPOT), read_only=True)
    md = ["# Tableau de bord : feux de forêt en Corse-du-Sud", "",
          "Généré par `src/dataviz.py` à partir de la couche or de "
          "l'entrepôt (`python src/pipeline.py` puis "
          "`python src/dataviz.py`). Tous les chiffres sont calculés depuis "
          "les données ; ne pas modifier ce fichier à la main.", "",
          "**Pour qui :** le directeur du SDIS 2A, qui doit préparer la "
          "saison des feux 2027 avant juin 2027.", "",
          "**Trois questions :** combien de feux et quelle tendance "
          "(synthèse) ; le niveau de danger prévu suffit-il à anticiper les "
          "feux (pourquoi) ; où concentrer les moyens (détail).", ""]
    md += feux_par_an(con)
    md += danger_et_feux(con)
    md += communes(con)
    md += surfaces(con)
    md += ["## Sources", "", SOURCE, "",
           "Méthode, couches et contrôles : `docs/pipeline/schema-entrepot.md`"
           " et `docs/pipeline/rapport-pipeline.md`."]
    con.close()
    (SORTIE / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Graphiques et page : {SORTIE}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
