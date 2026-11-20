"""Pipeline : couche bronze -> argent -> or, entrepot DuckDB.

Construit l'entrepot data/processed/entrepot.duckdb a partir des fichiers de
la couche bronze (data/raw/), en trois couches :

- bronze : copie exacte des fichiers, toutes les valeurs en texte, telles
  qu'ecrites dans les fichiers ; chaque ligne garde son fichier et son numero
  de ligne d'origine ;
- argent : donnees typees et nettoyees (texte vide -> valeur manquante,
  surfaces en nombres, dates en dates, codes de departement sur deux
  caracteres) ; chaque ligne garde le fichier et le numero de ligne de la
  couche bronze dont elle vient (lineage). Aucune valeur n'est inventee :
  une valeur absente reste absente ;
- or : schema en etoile pour le tableau de bord (voir
  docs/pipeline/schema-entrepot.md) : dimensions date, departement et
  commune ; faits feu et danger_jour.

Les tables de la couche or sont aussi exportees en Parquet dans
data/processed/or/ pour Power BI (Obtenir des donnees > Parquet).

Le pipeline verifie d'abord que la couche bronze est intacte (manifeste
SHA-256, src/donnees_brutes.py), puis lance des controles a chaque couche.
Il s'arrete au premier controle en echec. Le rapport des controles est ecrit
dans docs/pipeline/rapport-pipeline.md.

Il ne modifie jamais les fichiers de data/raw/.

Utilisation, depuis la racine du depot :

    python src/pipeline.py
"""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

import duckdb
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import donnees_brutes  # noqa: E402

BRONZE = Path("data/raw")
SORTIE = Path("data/processed")
ENTREPOT = SORTIE / "entrepot.duckdb"
EXPORT = SORTIE / "or"
RAPPORT = Path("docs/pipeline/rapport-pipeline.md")

BDIFF = {"2A": "bdiff_2A_2006_2025.csv", "2B": "bdiff_2B_2006_2025.csv"}
MDF = ["mdf_2024.csv.gz", "mdf_2025.csv.gz", "mdf_2026.csv.gz"]

# Ligne du fichier ou commencent les donnees (numerotation a partir de 1).
# BDIFF : 3 lignes d'information, puis l'en-tete (ligne 4).
PREMIERE_LIGNE_BDIFF = 5
PREMIERE_LIGNE_MDF = 2

# Colonnes BDIFF : nom dans le fichier -> nom dans la couche argent.
COLONNES_BDIFF = {
    "Année": "annee",
    "Numéro": "numero",
    "Département": "departement",
    "Code INSEE": "code_insee",
    "Nom de la commune": "nom_commune",
    "Date de première alerte": "date_alerte",
    "Surface parcourue (m2)": "surface_parcourue_m2",
    "Surface forêt (m2)": "surface_foret_m2",
    "Surface maquis garrigues (m2)": "surface_maquis_garrigues_m2",
    "Autres surfaces naturelles hors forêt (m2)":
        "surface_autres_naturelles_hors_foret_m2",
    "Surfaces agricoles (m2)": "surface_agricole_m2",
    "Autres surfaces (m2)": "surface_autres_m2",
    "Surface autres terres boisées (m2)": "surface_autres_terres_boisees_m2",
    "Surfaces non boisées naturelles (m2)":
        "surface_non_boisee_naturelle_m2",
    "Surfaces non boisées artificialisées (m2)":
        "surface_non_boisee_artificialisee_m2",
    "Surfaces non boisées (m2)": "surface_non_boisee_m2",
    "Précision des surfaces": "precision_surfaces",
    "Type de peuplement": "type_peuplement",
    "Nature": "nature",
    "Décès ou bâtiments touchés": "deces_ou_batiments_touches",
    "Nombre de décès": "nombre_deces",
    "Nombre de bâtiments totalement détruits":
        "nombre_batiments_detruits",
    "Nombre de bâtiments partiellement détruits":
        "nombre_batiments_partiellement_detruits",
    "Précision de la donnée": "precision_donnee",
}
SURFACES = [c for c in COLONNES_BDIFF.values() if c.startswith("surface_")]
ENTIERS = ["nombre_deces", "nombre_batiments_detruits",
           "nombre_batiments_partiellement_detruits"]

MOIS = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet",
        "aout", "septembre", "octobre", "novembre", "decembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
         "dimanche"]


class Controle:
    """Liste des controles, avec arret au premier echec."""

    def __init__(self) -> None:
        self.lignes: list[str] = []

    def __call__(self, couche: str, libelle: str, ok: bool,
                 detail: str) -> None:
        self.lignes.append(f"| {couche} | {libelle} | "
                           f"{'OK' if ok else 'ECHEC'} | {detail} |")
        print(f"{'OK    ' if ok else 'ECHEC '} [{couche}] {libelle} : {detail}")
        if not ok:
            raise SystemExit(f"Controle en echec ({couche}) : {libelle}. "
                             "Pipeline arrete.")


# ---------------------------------------------------------------------------
# Bronze
# ---------------------------------------------------------------------------

def lire_texte(chemin: Path, **options) -> pd.DataFrame:
    """Lit un fichier en gardant chaque valeur telle qu'ecrite (texte)."""
    return pd.read_csv(chemin, dtype=str, keep_default_na=False,
                       encoding="utf-8-sig", **options)


def enregistrer(con: duckdb.DuckDBPyConnection, nom: str,
                df: pd.DataFrame) -> None:
    """Rend un DataFrame lisible par DuckDB sous le nom `nom`.

    Les colonnes de texte passent en type objet : ce type est accepte par
    toutes les versions de DuckDB, quelle que soit la facon dont pandas (2
    ou 3) represente le texte.
    """
    df = df.copy()
    for c in df.columns:
        if not pd.api.types.is_numeric_dtype(df[c]) and \
                not pd.api.types.is_bool_dtype(df[c]) and \
                not pd.api.types.is_datetime64_any_dtype(df[c]):
            df[c] = df[c].astype(object)
    con.register(nom, df)


def charger_bronze(con: duckdb.DuckDBPyConnection, ctl: Controle,
                   attendus: dict[str, int]) -> None:
    con.execute("CREATE SCHEMA bronze")

    morceaux, criteres = [], []
    for dep, nom in BDIFF.items():
        chemin = BRONZE / nom
        with open(chemin, encoding="utf-8-sig") as f:
            info = [f.readline().strip() for _ in range(3)]
        for a in ["Type de feu : F", f"Département(s) : {dep}",
                  "2006-01-01", "2025-12-31"]:
            ctl("bronze", f"{nom} : critere d'export \"{a}\"", a in info[2],
                "present dans la ligne 3" if a in info[2] else "absent")
        criteres.append({"fichier_source": nom, "ligne_1": info[0],
                         "ligne_2": info[1], "ligne_3": info[2]})
        df = lire_texte(chemin, sep=";", skiprows=3)
        df.insert(0, "fichier_source", nom)
        df.insert(1, "ligne_source", range(PREMIERE_LIGNE_BDIFF,
                                           PREMIERE_LIGNE_BDIFF + len(df)))
        ctl("bronze", f"{nom} : lignes chargees", len(df) == attendus[nom],
            f"{len(df)} (manifeste : {attendus[nom]})")
        morceaux.append(df)
    bdiff = pd.concat(morceaux, ignore_index=True)
    ctl("bronze", "BDIFF : colonnes attendues",
        list(bdiff.columns[2:]) == list(COLONNES_BDIFF),
        f"{len(bdiff.columns) - 2} colonnes")
    enregistrer(con, "v_bdiff", bdiff)
    con.execute("CREATE TABLE bronze.bdiff AS SELECT * FROM v_bdiff")
    enregistrer(con, "v_criteres", pd.DataFrame(criteres))
    con.execute("CREATE TABLE bronze.bdiff_criteres AS "
                "SELECT * FROM v_criteres")

    morceaux = []
    for nom in MDF:
        df = lire_texte(BRONZE / nom, sep=None, engine="python")
        df.insert(0, "fichier_source", nom)
        df.insert(1, "ligne_source", range(PREMIERE_LIGNE_MDF,
                                           PREMIERE_LIGNE_MDF + len(df)))
        ctl("bronze", f"{nom} : lignes chargees", len(df) == attendus[nom],
            f"{len(df)} (manifeste : {attendus[nom]})")
        morceaux.append(df)
    # Le nom du departement s'appelle dep_nom en 2025 et nom_dep sinon :
    # la couche bronze garde les deux colonnes telles quelles.
    mdf = pd.concat(morceaux, ignore_index=True).fillna("")
    enregistrer(con, "v_mdf", mdf)
    con.execute("CREATE TABLE bronze.mdf AS SELECT * FROM v_mdf")


# ---------------------------------------------------------------------------
# Argent
# ---------------------------------------------------------------------------

def construire_argent(con: duckdb.DuckDBPyConnection, ctl: Controle) -> None:
    con.execute("CREATE SCHEMA argent")

    def texte(src: str) -> str:
        return f"NULLIF(TRIM(\"{src}\"), '')"

    selections = []
    for src, cible in COLONNES_BDIFF.items():
        if cible in ("annee", "numero"):
            expr = f"CAST(\"{src}\" AS INTEGER)"
        elif cible == "date_alerte":
            expr = f"CAST(\"{src}\" AS TIMESTAMP)"
        elif cible in SURFACES:
            expr = f"CAST({texte(src)} AS DOUBLE)"
        elif cible in ENTIERS:
            expr = f"CAST({texte(src)} AS INTEGER)"
        else:
            expr = texte(src)
        selections.append(f"{expr} AS {cible}")
    con.execute(f"""
        CREATE TABLE argent.feu AS
        SELECT annee || '-' || numero AS id_feu, *
        FROM (SELECT {', '.join(selections)}, fichier_source, ligne_source
              FROM bronze.bdiff)
    """)

    # Bulletins de la Meteo des forets. La date de publication est en UTC :
    # elle est convertie a l'heure de Paris, comme dans calcul_diagnostic.py.
    con.execute("""
        CREATE TABLE argent.bulletin_danger AS
        SELECT
            CAST(date AS TIMESTAMPTZ) AS publication_utc,
            timezone('Europe/Paris', CAST(date AS TIMESTAMPTZ))
                AS publication_paris,
            CAST(timezone('Europe/Paris', CAST(date AS TIMESTAMPTZ)) AS DATE)
                AS jour_publication,
            lpad(num_dep, 2, '0') AS departement,
            COALESCE(NULLIF(nom_dep, ''), NULLIF(dep_nom, '')) AS nom_departement,
            CAST(niveau_j1 AS INTEGER) AS niveau_j1,
            CAST(niveau_j2 AS INTEGER) AS niveau_j2,
            fichier_source, ligne_source
        FROM bronze.mdf
    """)

    def q(sql: str) -> list[tuple]:
        return con.execute(sql).fetchall()
    n_bronze = q("SELECT count(*) FROM bronze.bdiff")[0][0]
    n = q("SELECT count(*) FROM argent.feu")[0][0]
    ctl("argent", "feu : une ligne par ligne bronze", n == n_bronze,
        f"{n} lignes")
    doublons = q("SELECT count(*) - count(DISTINCT id_feu) "
                 "FROM argent.feu")[0][0]
    ctl("argent", "feu : cle (annee, numero) unique", doublons == 0,
        f"{doublons} doublon")
    hors = q("SELECT count(*) FROM argent.feu WHERE year(date_alerte) <> annee"
             " OR date_alerte < DATE '2006-01-01' "
             "OR date_alerte >= DATE '2026-01-01'")[0][0]
    ctl("argent", "feu : date d'alerte dans l'annee et la periode exportees",
        hors == 0, f"{hors} feu hors periode")
    sans = q("SELECT count(*) FROM argent.feu WHERE code_insee IS NULL "
             "OR surface_parcourue_m2 IS NULL OR date_alerte IS NULL"
             )[0][0]
    ctl("argent", "feu : commune, date et surface parcourue renseignees",
        sans == 0, f"{sans} feu incomplet")
    neg = q("SELECT count(*) FROM argent.feu WHERE "
            + " OR ".join(f"{c} < 0" for c in SURFACES))[0][0]
    ctl("argent", "feu : aucune surface negative", neg == 0,
        f"{neg} feu concerne")
    insee = q("SELECT count(*) FROM argent.feu WHERE NOT regexp_matches("
              "code_insee, '^2[AB][0-9]{3}$') OR left(code_insee, 2) <> "
              "departement")[0][0]
    ctl("argent", "feu : code INSEE corse, coherent avec le departement",
        insee == 0, f"{insee} code incoherent")
    noms = q("SELECT count(*) FROM (SELECT code_insee FROM argent.feu "
             "GROUP BY code_insee HAVING count(DISTINCT nom_commune) > 1)"
             )[0][0]
    ctl("argent", "feu : un seul nom de commune par code INSEE", noms == 0,
        f"{noms} code avec plusieurs noms")

    n_bronze = q("SELECT count(*) FROM bronze.mdf")[0][0]
    n = q("SELECT count(*) FROM argent.bulletin_danger")[0][0]
    ctl("argent", "bulletin_danger : une ligne par ligne bronze",
        n == n_bronze, f"{n} lignes")
    doublons = q("SELECT count(*) FROM (SELECT departement, jour_publication "
                 "FROM argent.bulletin_danger GROUP BY ALL "
                 "HAVING count(*) > 1)")[0][0]
    ctl("argent", "bulletin_danger : un bulletin par departement et par jour",
        doublons == 0, f"{doublons} doublon")
    niveaux = q("SELECT count(*) FROM argent.bulletin_danger WHERE "
                "niveau_j1 NOT BETWEEN 1 AND 4 OR niveau_j2 NOT BETWEEN 1 AND 4"
                )[0][0]
    ctl("argent", "bulletin_danger : niveaux entre 1 et 4", niveaux == 0,
        f"{niveaux} niveau hors bornes")
    sans_nom = q("SELECT count(*) FROM argent.bulletin_danger "
                 "WHERE nom_departement IS NULL")[0][0]
    ctl("argent", "bulletin_danger : nom de departement renseigne",
        sans_nom == 0, f"{sans_nom} ligne sans nom")


# ---------------------------------------------------------------------------
# Or : schema en etoile
# ---------------------------------------------------------------------------

def construire_or(con: duckdb.DuckDBPyConnection, ctl: Controle) -> None:
    con.execute("CREATE SCHEMA gold")
    def q(sql: str) -> list[tuple]:
        return con.execute(sql).fetchall()

    # Jour vise : jour de publication + 1 pour niveau_j1 (bulletin de la
    # veille) ; niveau_j2 vient du bulletin publie deux jours avant le jour
    # vise. Le premier jour de chaque saison n'a pas de niveau_j2.
    con.execute("""
        CREATE TABLE gold.fait_danger_jour AS
        SELECT
            CAST(strftime(b1.jour_publication + 1, '%Y%m%d') AS INTEGER)
                AS id_date,
            b1.departement,
            b1.niveau_j1,
            b2.niveau_j2 AS niveau_j2,
            b1.niveau_j1 >= 3 AS danger_eleve,
            b1.jour_publication AS jour_publication,
            b1.fichier_source, b1.ligne_source
        FROM argent.bulletin_danger b1
        LEFT JOIN argent.bulletin_danger b2
          ON b2.departement = b1.departement
         AND b2.jour_publication = b1.jour_publication - 1
    """)

    con.execute("""
        CREATE TABLE gold.dim_commune AS
        SELECT code_insee, any_value(nom_commune) AS nom_commune,
               any_value(departement) AS departement
        FROM argent.feu GROUP BY code_insee ORDER BY code_insee
    """)

    con.execute("""
        CREATE TABLE gold.dim_departement AS
        SELECT departement, any_value(nom_departement) AS nom_departement,
               departement IN ('2A', '2B') AS corse
        FROM argent.bulletin_danger GROUP BY departement ORDER BY departement
    """)

    con.execute("""
        CREATE TABLE gold.fait_feu AS
        SELECT
            f.id_feu,
            CAST(strftime(f.date_alerte, '%Y%m%d') AS INTEGER) AS id_date,
            f.code_insee,
            f.departement,
            f.date_alerte,
            hour(f.date_alerte) AS heure_alerte,
            f.surface_parcourue_m2 / 10000 AS surface_parcourue_ha,
            f.surface_foret_m2 / 10000 AS surface_foret_ha,
            f.surface_maquis_garrigues_m2 / 10000 AS surface_maquis_garrigues_ha,
            CASE WHEN f.surface_parcourue_m2 < 10000 THEN 'moins de 1 ha'
                 WHEN f.surface_parcourue_m2 < 100000 THEN '1 a 10 ha'
                 WHEN f.surface_parcourue_m2 <= 500000 THEN '10 a 50 ha'
                 ELSE 'plus de 50 ha' END AS classe_surface,
            COALESCE(f.nature, 'Non renseignee') AS cause,
            f.nature IS NOT NULL AS cause_renseignee,
            f.precision_surfaces,
            f.deces_ou_batiments_touches,
            f.fichier_source, f.ligne_source
        FROM argent.feu f
    """)

    debut = date(2006, 1, 1)
    fin = q("SELECT max(jour_publication) + 2 FROM argent.bulletin_danger"
            )[0][0]
    fin = max(fin, date(2026, 12, 31))
    jours = pd.date_range(debut, fin, freq="D")
    dim = pd.DataFrame({
        "id_date": jours.strftime("%Y%m%d").astype("int32"),
        "date": jours.date,
        "annee": jours.year,
        "mois": jours.month,
        "nom_mois": [MOIS[m - 1] for m in jours.month],
        "jour_du_mois": jours.day,
        "jour_semaine": [JOURS[d] for d in jours.day_of_week],
        "week_end": jours.day_of_week >= 5,
        "ete_juin_septembre": jours.month.isin([6, 7, 8, 9]),
    })
    enregistrer(con, "v_dim_date", dim)
    con.execute("CREATE TABLE gold.dim_date AS SELECT * FROM v_dim_date")

    # Controles d'integrite du schema en etoile.
    def orphelins(fait: str, cle: str, dim_: str, cle_dim: str) -> int:
        return q(f"SELECT count(*) FROM gold.{fait} f WHERE NOT EXISTS "
                 f"(SELECT 1 FROM gold.{dim_} d WHERE d.{cle_dim} = f.{cle})"
                 )[0][0]

    for fait, cle, dim_, cle_dim in [
            ("fait_feu", "id_date", "dim_date", "id_date"),
            ("fait_feu", "code_insee", "dim_commune", "code_insee"),
            ("fait_feu", "departement", "dim_departement", "departement"),
            ("fait_danger_jour", "id_date", "dim_date", "id_date"),
            ("fait_danger_jour", "departement", "dim_departement",
             "departement")]:
        n = orphelins(fait, cle, dim_, cle_dim)
        ctl("or", f"{fait}.{cle} present dans {dim_}", n == 0,
            f"{n} ligne orpheline")
    for table, cle in [("dim_date", "id_date"), ("dim_commune", "code_insee"),
                       ("dim_departement", "departement"),
                       ("fait_feu", "id_feu")]:
        n = q(f"SELECT count(*) - count(DISTINCT {cle}) FROM gold.{table}"
              )[0][0]
        ctl("or", f"{table} : cle {cle} unique", n == 0, f"{n} doublon")
    n = q("SELECT count(*) FROM (SELECT id_date, departement FROM "
          "gold.fait_danger_jour GROUP BY ALL HAVING count(*) > 1)"
          )[0][0]
    ctl("or", "fait_danger_jour : un niveau par jour vise et departement",
        n == 0, f"{n} doublon")
    a, b = q("SELECT (SELECT sum(surface_parcourue_m2) FROM argent.feu), "
             "(SELECT sum(surface_parcourue_ha) * 10000 FROM gold.fait_feu)"
             )[0]
    ctl("or", "fait_feu : surface totale conservee (argent -> or)",
        abs(a - b) < 0.01, f"{a / 10000:.1f} ha")


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def chiffres(con: duckdb.DuckDBPyConnection) -> list[str]:
    """Chiffres de reference, recalcules depuis la couche or."""
    def q(sql: str) -> list[tuple]:
        return con.execute(sql).fetchall()
    r = ["| Mesure | Corse-du-Sud (2A) | Haute-Corse (2B) |", "|---|---|---|"]

    def ligne(libelle: str, sql: str, fmt: str = "{}") -> None:
        v = {d: q(sql.format(dep=d))[0][0] for d in ("2A", "2B")}
        r.append(f"| {libelle} | {fmt.format(v['2A'])} | "
                 f"{fmt.format(v['2B'])} |")

    ligne("Feux 2006-2025", "SELECT count(*) FROM gold.fait_feu "
          "WHERE departement = '{dep}'")
    ligne("Surface parcourue 2006-2025 (ha)", "SELECT sum(surface_parcourue_ha)"
          " FROM gold.fait_feu WHERE departement = '{dep}'", "{:.1f}")
    ligne("Communes ayant eu au moins un feu", "SELECT count(*) FROM "
          "gold.dim_commune WHERE departement = '{dep}'")
    ligne("Part des feux de cause non renseignee", "SELECT round(100 * "
          "avg(CASE WHEN cause_renseignee THEN 0 ELSE 1 END), 1) FROM "
          "gold.fait_feu WHERE departement = '{dep}'", "{} %")
    ligne("Feux en 2025", "SELECT count(*) FROM gold.fait_feu f JOIN "
          "gold.dim_date d USING (id_date) WHERE departement = '{dep}' "
          "AND d.annee = 2025")
    ligne("Jours vises par la Meteo des forets (3 saisons)",
          "SELECT count(*) FROM gold.fait_danger_jour "
          "WHERE departement = '{dep}'")
    ligne("Jours de danger eleve (niveau_j1 >= 3), etes 2024 et 2025",
          "SELECT count(*) FROM gold.fait_danger_jour f JOIN gold.dim_date d "
          "USING (id_date) WHERE departement = '{dep}' AND danger_eleve "
          "AND d.annee IN (2024, 2025)")
    ligne("dont jours sans feu", """
          SELECT count(*) FROM gold.fait_danger_jour j JOIN gold.dim_date d
          USING (id_date) WHERE j.departement = '{dep}' AND danger_eleve
          AND d.annee IN (2024, 2025) AND NOT EXISTS (SELECT 1 FROM
          gold.fait_feu f WHERE f.id_date = j.id_date
          AND f.departement = j.departement)""")
    return r


def ecrire_rapport(con: duckdb.DuckDBPyConnection, ctl: Controle) -> None:
    def q(sql: str) -> list[tuple]:
        return con.execute(sql).fetchall()
    tables = q("SELECT schema_name, table_name FROM "
               "duckdb_tables() ORDER BY schema_name, table_name")
    lignes = [
        "# Rapport du pipeline",
        "",
        "Genere par `src/pipeline.py` (`python src/pipeline.py`). Ne pas "
        "modifier a la main : relancer le pipeline.",
        "",
        "- **Entree :** couche bronze `data/raw/`, verifiee par le manifeste "
        "SHA-256 (`data/manifeste.csv`).",
        f"- **Entrepot :** `{ENTREPOT.as_posix()}` (DuckDB) ; tables de la "
        f"couche or exportees en Parquet dans `{EXPORT.as_posix()}/`.",
        "- **Schema :** `docs/pipeline/schema-entrepot.md`.",
        "",
        "## Tables",
        "",
        "| Couche | Table | Lignes |",
        "|---|---|---|",
    ]
    couche = {"bronze": "bronze", "argent": "argent", "gold": "or"}
    for schema, nom in tables:
        n = q(f"SELECT count(*) FROM {schema}.{nom}")[0][0]
        lignes.append(f"| {couche[schema]} | `{nom}` | {n} |")
    lignes += ["", "## Controles", "",
               "| Couche | Controle | Resultat | Detail |", "|---|---|---|---|"]
    lignes += ctl.lignes
    lignes += ["", "## Chiffres de reference (couche or)", "",
               "Recalcules depuis la couche or ; ils doivent etre identiques "
               "a ceux de `docs/qualite/calculs-diagnostic.md`, calcules "
               "directement sur les fichiers bruts.", ""]
    lignes += chiffres(con)
    RAPPORT.parent.mkdir(parents=True, exist_ok=True)
    RAPPORT.write_text("\n".join(lignes) + "\n", encoding="utf-8")


def main() -> int:
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()

    print("Verification de la couche bronze (manifeste) :")
    if donnees_brutes.verifier() != 0:
        print("Couche bronze differente du manifeste : pipeline arrete.",
              file=sys.stderr)
        return 1
    attendus = {}
    with open(donnees_brutes.MANIFESTE, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            attendus[l["fichier"]] = int(l["lignes_de_donnees"])

    SORTIE.mkdir(parents=True, exist_ok=True)
    ENTREPOT.unlink(missing_ok=True)
    con = duckdb.connect(str(ENTREPOT))
    con.execute("SET TimeZone = 'UTC'")
    ctl = Controle()
    ctl("bronze", "manifeste SHA-256", True,
        f"{len(attendus)} fichiers identiques")
    charger_bronze(con, ctl, attendus)
    construire_argent(con, ctl)
    construire_or(con, ctl)

    EXPORT.mkdir(parents=True, exist_ok=True)
    for (nom,) in q_tables(con):
        con.execute(f"COPY gold.{nom} TO '{(EXPORT / nom).as_posix()}.parquet' "
                    "(FORMAT parquet)")
    ecrire_rapport(con, ctl)
    con.close()
    print(f"Entrepot : {ENTREPOT} ; Parquet : {EXPORT}/ ; rapport : {RAPPORT}")
    return 0


def q_tables(con: duckdb.DuckDBPyConnection) -> list[tuple[str]]:
    return con.execute("SELECT table_name FROM duckdb_tables() WHERE "
                       "schema_name = 'gold' ORDER BY table_name").fetchall()


if __name__ == "__main__":
    sys.exit(main())
