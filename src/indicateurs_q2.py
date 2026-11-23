"""Chiffres de la fiche d'indicateurs Q2 (seuil de declenchement).

Lit la couche or de l'entrepot (data/processed/entrepot.duckdb, construit par
src/pipeline.py) et ecrit docs/qualite/indicateurs-q2.md : tous les chiffres
de kpi/fiche-indicateurs-arouna-toure.md.

Definitions (identiques a src/calcul_diagnostic.py) :

- jour : jour vise par la prevision de la Meteo des forets (fait_danger_jour),
  heure de Paris ; saisons 2024 et 2025 (du 4 juin au 1er octobre) pour les
  calculs avec les feux, les feux de 2026 etant exclus (D-009) ;
- jour de declenchement : jour ou la regle de declenchement est vraie
  (par defaut niveau_j1 >= 3) ;
- feu : feu de foret de la BDIFF (type F, toutes surfaces), rattache au jour
  de sa date de premiere alerte et a son departement ;
- I1 : part des jours de declenchement sans aucun feu ;
- I2 : part des feux partis hors des jours de declenchement.

Utilisation, depuis la racine du depot :

    python src/pipeline.py
    python src/indicateurs_q2.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import duckdb

ENTREPOT = Path("data/processed/entrepot.duckdb")
SORTIE = Path("docs/qualite/indicateurs-q2.md")

REGLES = {
    "niveau_j1 >= 2": "niveau_j1 >= 2",
    "niveau_j1 >= 3 (retenue)": "niveau_j1 >= 3",
    "niveau_j2 >= 3 (prevision a deux jours)": "niveau_j2 >= 3",
    "niveau_j1 >= 3 et niveau_j2 >= 3": "niveau_j1 >= 3 AND niveau_j2 >= 3",
}


def pct(n: int, d: int) -> str:
    return "sans objet" if d == 0 else f"{100 * n / d:.1f} %"


def jours(con: duckdb.DuckDBPyConnection) -> None:
    """Table temporaire : un jour vise par departement, avec ses feux."""
    con.execute("""
        CREATE TEMP TABLE j AS
        SELECT d.departement, dd.annee AS saison, d.id_date,
               d.niveau_j1, d.niveau_j2,
               (SELECT count(*) FROM gold.fait_feu f
                WHERE f.id_date = d.id_date
                  AND f.departement = d.departement) AS feux
        FROM gold.fait_danger_jour d JOIN gold.dim_date dd USING (id_date)
        WHERE d.departement IN ('2A', '2B')
    """)


def mesure(con: duckdb.DuckDBPyConnection, dep: str, regle: str,
           saisons: tuple[int, ...]) -> dict:
    s = ", ".join(str(a) for a in saisons)
    r = con.execute(f"""
        SELECT
            count(*) FILTER (WHERE {regle}),
            count(*) FILTER (WHERE ({regle}) AND feux = 0),
            coalesce(sum(feux), 0),
            coalesce(sum(feux) FILTER (WHERE {regle}), 0)
        FROM j WHERE departement = '{dep}' AND saison IN ({s})
    """).fetchall()[0]
    declenches, sans_feu, feux, couverts = r
    return {"declenches": declenches, "sans_feu": sans_feu, "feux": feux,
            "hors": feux - couverts,
            "i1": pct(sans_feu, declenches), "i2": pct(feux - couverts, feux)}


def main() -> int:
    if not ENTREPOT.exists():
        print(f"{ENTREPOT} introuvable : lancer d'abord python src/pipeline.py",
              file=sys.stderr)
        return 1
    con = duckdb.connect(str(ENTREPOT), read_only=True)
    jours(con)
    deux = (2024, 2025)
    l = ["# Chiffres de la fiche d'indicateurs Q2",
         "",
         "Genere par `src/indicateurs_q2.py` a partir de la couche or de "
         "l'entrepot. Ne pas modifier a la main.",
         "",
         "- I1 : part des jours de declenchement sans aucun feu.",
         "- I2 : part des feux partis hors des jours de declenchement.",
         "- Jours vises des saisons 2024 et 2025 (du 4 juin au 1er "
         "octobre) ; feux de 2026 exclus (D-009).",
         ""]

    # 1. Valeurs de depart, par departement et par regle
    l += ["## 1. Valeurs de depart (saisons 2024 et 2025)", "",
          "| Departement | Regle de declenchement | Jours declenches | "
          "Dont sans feu | I1 | Feux | Feux hors declenchement | I2 |",
          "|---|---|---|---|---|---|---|---|"]
    for dep in ("2A", "2B"):
        for nom, regle in REGLES.items():
            m = mesure(con, dep, regle, deux)
            l.append(f"| {dep} | {nom} | {m['declenches']} | {m['sans_feu']}"
                     f" | {m['i1']} | {m['feux']} | {m['hors']} | {m['i2']} |")
    l.append("")

    # 2. Saison par saison, regle retenue
    l += ["## 2. Saison par saison (niveau_j1 >= 3)", "",
          "| Departement | Saison | Jours declenches | Dont sans feu | I1 | "
          "Feux | Feux hors declenchement | I2 |",
          "|---|---|---|---|---|---|---|---|"]
    for dep in ("2A", "2B"):
        for saison in deux:
            m = mesure(con, dep, "niveau_j1 >= 3", (saison,))
            l.append(f"| {dep} | {saison} | {m['declenches']} | "
                     f"{m['sans_feu']} | {m['i1']} | {m['feux']} | "
                     f"{m['hors']} | {m['i2']} |")
    l.append("")

    # 3. Sensibilite de I1 a un jour
    m = mesure(con, "2A", "niveau_j1 >= 3", deux)
    n, s = m["declenches"], m["sans_feu"]
    l += ["## 3. Poids d'un jour dans I1 (2A, niveau_j1 >= 3)", "",
          f"- {s} jours sans feu sur {n} : {pct(s, n)} ; un jour sans feu de "
          f"moins : {pct(s - 1, n)} ; un de plus : {pct(s + 1, n)}.",
          f"- Un jour pese {100 / n:.1f} points sur {n} jours ; sur 10 jours,"
          " il pese 10 points ; sur 3 jours (ete 2024), 33.3 points.", ""]

    # 4. KPI secondaire et contexte : jours declenches et feux par saison
    l += ["## 4. Jours declenches et feux par saison (niveau_j1 >= 3)", "",
          "| Departement | Saison | Jours vises | Jours declenches | "
          "Feux de l'ete | Jours avec au moins un feu |",
          "|---|---|---|---|---|---|"]
    for dep in ("2A", "2B"):
        rows = con.execute(f"""
            SELECT saison, count(*), count(*) FILTER (WHERE niveau_j1 >= 3),
                   sum(feux), count(*) FILTER (WHERE feux > 0)
            FROM j WHERE departement = '{dep}' GROUP BY 1 ORDER BY 1
        """).fetchall()
        for saison, vises, decl, feux, avec in rows:
            exclus = saison not in deux
            l.append(f"| {dep} | {saison} | {vises} | {decl} | "
                     f"{'exclus (D-009)' if exclus else feux} | "
                     f"{'exclus (D-009)' if exclus else avec} |")
    l.append("")

    # 5. Part des jours avec feu selon le niveau (ecart entre niveaux)
    l += ["## 5. Part des jours avec feu, jours de declenchement et autres "
          "jours (2A, saisons 2024 et 2025)", ""]
    a = con.execute("""
        SELECT count(*) FILTER (WHERE niveau_j1 >= 3 AND feux > 0),
               count(*) FILTER (WHERE niveau_j1 >= 3),
               count(*) FILTER (WHERE niveau_j1 < 3 AND feux > 0),
               count(*) FILTER (WHERE niveau_j1 < 3)
        FROM j WHERE departement = '2A' AND saison IN (2024, 2025)
    """).fetchall()[0]
    l += [f"- Jours de declenchement avec feu : {a[0]} sur {a[1]} "
          f"({pct(a[0], a[1])}).",
          f"- Autres jours avec feu : {a[2]} sur {a[3]} ({pct(a[2], a[3])}).",
          ""]
    con.close()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text("\n".join(l) + "\n", encoding="utf-8")
    print(f"Chiffres ecrits : {SORTIE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
