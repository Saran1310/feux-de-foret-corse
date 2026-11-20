"""Tests de l'entrepot construit par src/pipeline.py.

A lancer apres le pipeline, depuis la racine du depot :

    python src/pipeline.py
    python tests/test_pipeline.py

(ou `python -m pytest tests` si pytest est installe).

Deux familles de tests :

1. Lineage : une ligne de la couche or renvoie, par fichier_source et
   ligne_source, a la ligne exacte du fichier brut dont elle vient, avec les
   memes valeurs.
2. Coherence : les chiffres recalcules depuis la couche or sont ceux que
   src/calcul_diagnostic.py obtient directement sur les fichiers bruts
   (docs/qualite/calculs-diagnostic.md). Deux chemins de calcul differents
   donnent le meme resultat.
"""

from __future__ import annotations

import csv
import gzip
import sys
from pathlib import Path

import duckdb

ENTREPOT = Path("data/processed/entrepot.duckdb")
BRONZE = Path("data/raw")


def connexion() -> duckdb.DuckDBPyConnection:
    if not ENTREPOT.exists():
        raise SystemExit(f"{ENTREPOT} introuvable : lancer d'abord "
                         "python src/pipeline.py")
    return duckdb.connect(str(ENTREPOT), read_only=True)


def q(sql: str) -> list[tuple]:
    con = connexion()
    try:
        return con.execute(sql).fetchall()
    finally:
        con.close()


def ligne_brute(fichier: str, numero: int) -> list[str]:
    """Renvoie la ligne `numero` (a partir de 1) du fichier brut, decoupee."""
    chemin = BRONZE / fichier
    ouvrir = gzip.open if chemin.suffix == ".gz" else open
    with ouvrir(chemin, "rt", encoding="utf-8-sig", newline="") as f:
        lignes = f.read().splitlines()
    texte = lignes[numero - 1]
    sep = ";" if (fichier.startswith("bdiff") or ";" in lignes[0]) else ","
    return next(csv.reader([texte], delimiter=sep))


# ---------------------------------------------------------------------------
# 1. Lineage
# ---------------------------------------------------------------------------

def test_lineage_feu() -> None:
    """Chaque feu de la couche or se retrouve a sa ligne du fichier BDIFF."""
    feux = q("SELECT id_feu, code_insee, strftime(date_alerte, "
             "'%Y-%m-%d %H:%M:%S'), surface_parcourue_ha, fichier_source, "
             "ligne_source FROM gold.fait_feu USING SAMPLE 50 ROWS "
             "(reservoir, 7)")
    assert len(feux) == 50
    for id_feu, insee, alerte, surface, fichier, numero in feux:
        brut = ligne_brute(fichier, numero)
        # Colonnes : Annee, Numero, Departement, Code INSEE, Nom, Date,
        # Surface parcourue (m2), ...
        assert f"{brut[0]}-{brut[1]}" == id_feu, (fichier, numero)
        assert brut[3] == insee, (fichier, numero)
        assert brut[5] == alerte, (fichier, numero)
        assert float(brut[6]) / 10000 == surface, (fichier, numero)


def test_lineage_danger() -> None:
    """Chaque niveau de danger se retrouve a sa ligne du fichier Meteo."""
    jours = q("SELECT departement, niveau_j1, fichier_source, ligne_source "
              "FROM gold.fait_danger_jour USING SAMPLE 50 ROWS "
              "(reservoir, 7)")
    assert len(jours) == 50
    for dep, n1, fichier, numero in jours:
        brut = ligne_brute(fichier, numero)
        # Colonnes : date, num_dep, niveau_j1, niveau_j2, nom
        assert brut[1].zfill(2) == dep, (fichier, numero)
        assert int(brut[2]) == n1, (fichier, numero)


# ---------------------------------------------------------------------------
# 2. Coherence avec docs/qualite/calculs-diagnostic.md
# ---------------------------------------------------------------------------

def test_totaux_bdiff() -> None:
    r = q("SELECT departement, count(*), round(sum(surface_parcourue_ha), 1)"
          " FROM gold.fait_feu GROUP BY 1 ORDER BY 1")
    assert r == [("2A", 4694, 13133.2), ("2B", 4992, 24272.6)]


def test_niveaux_ete_2024_2025_2a() -> None:
    """Jours, jours avec feu et feux par niveau_j1 (Corse-du-Sud)."""
    r = q("""
        WITH j AS (
            SELECT d.niveau_j1,
                   (SELECT count(*) FROM gold.fait_feu f
                    WHERE f.id_date = d.id_date AND f.departement = '2A')
                       AS feux
            FROM gold.fait_danger_jour d JOIN gold.dim_date USING (id_date)
            WHERE d.departement = '2A' AND annee IN (2024, 2025))
        SELECT niveau_j1, count(*), sum(CAST(feux > 0 AS INTEGER)), sum(feux)
        FROM j GROUP BY 1 ORDER BY 1
    """)
    assert r == [(1, 57, 10, 14), (2, 166, 67, 112), (3, 17, 10, 13)]


def test_concentration_communes_2a() -> None:
    r = q("SELECT c.nom_commune, count(*) FROM gold.fait_feu f "
          "JOIN gold.dim_commune c USING (code_insee) "
          "WHERE f.departement = '2A' GROUP BY 1 ORDER BY 2 DESC, 1 LIMIT 3")
    assert r == [("Ajaccio", 327), ("Porto-Vecchio", 317), ("Sartène", 265)]


def test_grands_feux_2a() -> None:
    r = q("SELECT count(*) FROM gold.fait_feu WHERE departement = '2A' "
          "AND classe_surface = 'plus de 50 ha'")
    assert r == [(18,)]


if __name__ == "__main__":
    tests = [(n, f) for n, f in globals().items()
             if n.startswith("test_") and callable(f)]
    echecs = 0
    for nom, test in tests:
        try:
            test()
            print(f"OK     {nom}")
        except AssertionError as e:
            echecs += 1
            print(f"ECHEC  {nom} : {e}")
    print(f"{len(tests) - echecs}/{len(tests)} tests reussis")
    sys.exit(1 if echecs else 0)
