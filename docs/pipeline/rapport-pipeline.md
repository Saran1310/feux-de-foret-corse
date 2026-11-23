# Rapport du pipeline

Genere par `src/pipeline.py` (`python src/pipeline.py`). Ne pas modifier a la main : relancer le pipeline.

- **Entree :** couche bronze `data/raw/`, verifiee par le manifeste SHA-256 (`data/manifeste.csv`).
- **Entrepot :** `data/processed/entrepot.duckdb` (DuckDB) ; tables de la couche or exportees en Parquet dans `data/processed/or/`.
- **Schema :** `docs/pipeline/schema-entrepot.md`.

## Tables

| Couche | Table | Lignes |
|---|---|---|
| argent | `bulletin_danger` | 35616 |
| argent | `feu` | 9686 |
| bronze | `bdiff` | 9686 |
| bronze | `bdiff_criteres` | 2 |
| bronze | `mdf` | 35616 |
| or | `dim_commune` | 350 |
| or | `dim_date` | 7670 |
| or | `dim_departement` | 96 |
| or | `fait_danger_jour` | 35616 |
| or | `fait_feu` | 9686 |

## Controles

| Couche | Controle | Resultat | Detail |
|---|---|---|---|
| bronze | manifeste SHA-256 | OK | 6 fichiers identiques |
| bronze | bdiff_2A_2006_2025.csv : critere d'export "Type de feu : F" | OK | present dans la ligne 3 |
| bronze | bdiff_2A_2006_2025.csv : critere d'export "Département(s) : 2A" | OK | present dans la ligne 3 |
| bronze | bdiff_2A_2006_2025.csv : critere d'export "2006-01-01" | OK | present dans la ligne 3 |
| bronze | bdiff_2A_2006_2025.csv : critere d'export "2025-12-31" | OK | present dans la ligne 3 |
| bronze | bdiff_2A_2006_2025.csv : lignes chargees | OK | 4694 (manifeste : 4694) |
| bronze | bdiff_2B_2006_2025.csv : critere d'export "Type de feu : F" | OK | present dans la ligne 3 |
| bronze | bdiff_2B_2006_2025.csv : critere d'export "Département(s) : 2B" | OK | present dans la ligne 3 |
| bronze | bdiff_2B_2006_2025.csv : critere d'export "2006-01-01" | OK | present dans la ligne 3 |
| bronze | bdiff_2B_2006_2025.csv : critere d'export "2025-12-31" | OK | present dans la ligne 3 |
| bronze | bdiff_2B_2006_2025.csv : lignes chargees | OK | 4992 (manifeste : 4992) |
| bronze | BDIFF : colonnes attendues | OK | 24 colonnes |
| bronze | mdf_2024.csv.gz : lignes chargees | OK | 11520 (manifeste : 11520) |
| bronze | mdf_2025.csv.gz : lignes chargees | OK | 11520 (manifeste : 11520) |
| bronze | mdf_2026.csv.gz : lignes chargees | OK | 12576 (manifeste : 12576) |
| argent | feu : une ligne par ligne bronze | OK | 9686 lignes |
| argent | feu : cle (annee, numero) unique | OK | 0 doublon |
| argent | feu : date d'alerte dans l'annee et la periode exportees | OK | 0 feu hors periode |
| argent | feu : commune, date et surface parcourue renseignees | OK | 0 feu incomplet |
| argent | feu : aucune surface negative | OK | 0 feu concerne |
| argent | feu : code INSEE corse, coherent avec le departement | OK | 0 code incoherent |
| argent | feu : un seul nom de commune par code INSEE | OK | 0 code avec plusieurs noms |
| argent | bulletin_danger : une ligne par ligne bronze | OK | 35616 lignes |
| argent | bulletin_danger : un bulletin par departement et par jour | OK | 0 doublon |
| argent | bulletin_danger : niveaux entre 1 et 4 | OK | 0 niveau hors bornes |
| argent | bulletin_danger : nom de departement renseigne | OK | 0 ligne sans nom |
| or | fait_feu.id_date present dans dim_date | OK | 0 ligne orpheline |
| or | fait_feu.code_insee present dans dim_commune | OK | 0 ligne orpheline |
| or | fait_feu.departement present dans dim_departement | OK | 0 ligne orpheline |
| or | fait_danger_jour.id_date present dans dim_date | OK | 0 ligne orpheline |
| or | fait_danger_jour.departement present dans dim_departement | OK | 0 ligne orpheline |
| or | dim_date : cle id_date unique | OK | 0 doublon |
| or | dim_commune : cle code_insee unique | OK | 0 doublon |
| or | dim_departement : cle departement unique | OK | 0 doublon |
| or | fait_feu : cle id_feu unique | OK | 0 doublon |
| or | fait_danger_jour : un niveau par jour vise et departement | OK | 0 doublon |
| or | fait_feu : surface totale conservee (argent -> or) | OK | 37405.7 ha |

## Chiffres de reference (couche or)

Recalcules depuis la couche or ; ils doivent etre identiques a ceux de `docs/qualite/calculs-diagnostic.md`, calcules directement sur les fichiers bruts.

| Mesure | Corse-du-Sud (2A) | Haute-Corse (2B) |
|---|---|---|
| Feux 2006-2025 | 4694 | 4992 |
| Surface parcourue 2006-2025 (ha) | 13133.2 | 24272.6 |
| Communes ayant eu au moins un feu | 124 | 226 |
| Part des feux de cause non renseignee | 47.1 % | 47.0 % |
| Feux en 2025 | 93 | 84 |
| Jours vises par la Meteo des forets (3 saisons) | 371 | 371 |
| Jours de danger eleve (niveau_j1 >= 3), etes 2024 et 2025 | 17 | 9 |
| dont jours sans feu | 7 | 3 |
