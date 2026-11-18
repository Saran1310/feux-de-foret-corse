# Profil de la source : Météo des forêts

- **Généré par :** `src/profilage.py` le 2026-11-18
- **Fichiers lus :** `data/raw/mdf_2024.csv.gz`, `data/raw/mdf_2025.csv.gz`, `data/raw/mdf_2026.csv.gz`
- **Lignes :** 35616
- **Colonnes :** 5

Ce rapport décrit les données telles qu'elles sont. Il ne décide rien : les règles de qualité et leurs seuils sont fixés à partir de ces constats.

## Informations du fichier

- `mdf_2024.csv.gz` : 11520 lignes, colonnes `date`, `num_dep`, `niveau_j1`, `niveau_j2`, `nom_dep`
- `mdf_2025.csv.gz` : 11520 lignes, colonnes `date`, `num_dep`, `niveau_j1`, `niveau_j2`, `dep_nom`
- `mdf_2026.csv.gz` : 12576 lignes, colonnes `date`, `num_dep`, `niveau_j1`, `niveau_j2`, `nom_dep`

## Profil des colonnes

| Colonne | Type observe | Non vides | Vides (%) | Distinctes | Min | Max | 3 valeurs les plus frequentes |
|---|---|---|---|---|---|---|---|
| date | date | 35616 | 0.00 | 371 | 2024-06-03 18:00 | 2026-10-05 16:50 | 2024-06-04T16:00:00Z (96), 2024-06-05T16:00:00Z (96), 2024-06-06T16:00:00Z (96) |
| num_dep | texte | 35616 | 0.00 | 105 |  |  | 10 (371), 11 (371), 12 (371) |
| niveau_j1 | entier | 35616 | 0.00 | 4 | 1 | 4 | 1 (24183), 2 (8763), 3 (2541) |
| niveau_j2 | entier | 35616 | 0.00 | 4 | 1 | 4 | 1 (25112), 2 (8593), 3 (1838) |
| nom_dep | texte | 35616 | 0.00 | 96 |  |  | Ain (371), Aisne (371), Allier (371) |

## Contrôles propres à la source

- `num_dep` sur 1 caractere (a normaliser sur 2) : 2160 lignes.
- Departements distincts apres normalisation : 96. Corse-du-Sud (2A) : 371 lignes ; Haute-Corse (2B) : 371 lignes.
- `date` illisible ou vide : 0 lignes.
- Doublons sur (jour de publication, departement) : 0 lignes sur 35616.
- `niveau_j1` vide ou hors de 1 a 4 : 0 lignes. Repartition : 1 : 24183, 2 : 8763, 3 : 2541, 4 : 129.
- `niveau_j2` vide ou hors de 1 a 4 : 0 lignes. Repartition : 1 : 25112, 2 : 8593, 3 : 1838, 4 : 73.
- `mdf_2024.csv.gz` : publications du 2024-06-03 au 2024-09-30, 120 jours, 0 jours sans bulletin dans cet intervalle.
  Departements avec moins de bulletins que de jours publies : 0.
- `mdf_2025.csv.gz` : publications du 2025-06-03 au 2025-09-30, 120 jours, 0 jours sans bulletin dans cet intervalle.
  Departements avec moins de bulletins que de jours publies : 0.
- `mdf_2026.csv.gz` : publications du 2026-05-28 au 2026-10-05, 131 jours, 0 jours sans bulletin dans cet intervalle.
  Departements avec moins de bulletins que de jours publies : 0.
- Departements avec plusieurs noms differents : 0.

## Repérage des données personnelles

Colonnes signalées automatiquement (nom de colonne ou contenu). Un signal n'est pas une conclusion : chaque colonne est à examiner.

| Colonne | Signal |
|---|---|
| nom_dep | nom de colonne contenant : nom |
