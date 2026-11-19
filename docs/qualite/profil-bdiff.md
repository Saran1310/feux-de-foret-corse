# Profil de la source : BDIFF

- **Généré par :** `src/profilage.py` le 2026-11-19
- **Fichiers lus :** `data/raw/bdiff_2A_2006_2025.csv`
- **Lignes :** 4694
- **Colonnes :** 24

Ce rapport décrit les données telles qu'elles sont. Il ne décide rien : les règles de qualité et leurs seuils sont fixés à partir de ces constats.

## Informations du fichier

- Certaines données sont associées à l'ancienne version du formulaire incendie. Consultez la documentation pour plus d'informations.
- Nombre d'incendies suivant les critères de sélection : 4694
- Critères de sélection => ; Date de première alerte, de : 2006-01-01 00:00:00 ; Date de première alerte, jusqu'à : 2025-12-31 23:59:00 ; Département(s) : 2A ; Type de feu : F

## Profil des colonnes

| Colonne | Type observe | Non vides | Vides (%) | Distinctes | Min | Max | 3 valeurs les plus frequentes |
|---|---|---|---|---|---|---|---|
| Année | entier | 4694 | 0.00 | 20 | 2006 | 2025 | 2007 (420), 2006 (407), 2009 (378) |
| Numéro | entier | 4694 | 0.00 | 3928 | 550 | 28 316 | 7313 (5), 7648 (4), 7310 (4) |
| Département | texte | 4694 | 0.00 | 1 |  |  | 2A (4694) |
| Code INSEE | texte | 4694 | 0.00 | 124 |  |  | 2A004 (327), 2A247 (317), 2A272 (265) |
| Nom de la commune | texte | 4694 | 0.00 | 124 |  |  | Ajaccio (327), Porto-Vecchio (317), Sartène (265) |
| Date de première alerte | date | 4694 | 0.00 | 4631 | 2006-01-11 16:03 | 2025-12-24 19:35 | 2024-08-13 01:24:00 (4), 2025-08-26 15:11:00 (4), 2006-07-14 15:30:00 (3) |
| Surface parcourue (m2) | entier | 4694 | 0.00 | 380 | 1 | 32 210 000 | 50 (412), 100 (391), 200 (336) |
| Surface forêt (m2) | entier | 2980 | 36.51 | 213 | 0 | 30 381 100 | 0 (263), 47 (249), 24 (217) |
| Surface maquis garrigues (m2) | entier | 4627 | 1.43 | 418 | 0 | 15 460 800 | 10 (269), 48 (249), 5 (222) |
| Autres surfaces naturelles hors forêt (m2) | entier | 2886 | 38.52 | 6 | 0 | 150 000 | 0 (2881), 10000 (1), 6000 (1) |
| Surfaces agricoles (m2) | entier | 290 | 93.82 | 3 | 0 | 20 000 | 0 (288), 20000 (1), 2000 (1) |
| Autres surfaces (m2) | entier | 290 | 93.82 | 5 | 0 | 5000 | 0 (285), 2000 (2), 1000 (1) |
| Surface autres terres boisées (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées naturelles (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées artificialisées (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées (m2) | entier | 2714 | 42.18 | 158 | 0 | 1 610 500 | 2 (336), 0 (259), 5 (251) |
| Précision des surfaces | texte | 290 | 93.82 | 2 |  |  | Mesurées (147), Estimées (143) |
| Type de peuplement | entier | 2296 | 51.09 | 6 | 1 | 6 | 1 (2086), 4 (94), 3 (43) |
| Nature | texte | 2482 | 47.12 | 5 |  |  | Involontaire (particulier) (1003), Malveillance (767), Involontaire (travaux) (307) |
| Décès ou bâtiments touchés | texte | 290 | 93.82 | 2 |  |  | Non (289), Oui (1) |
| Nombre de décès | entier | 1 | 99.98 | 1 | 0 | 0 | 0 (1) |
| Nombre de bâtiments totalement détruits | entier | 1 | 99.98 | 1 | 0 | 0 | 0 (1) |
| Nombre de bâtiments partiellement détruits | entier | 1 | 99.98 | 1 | 1 | 1 | 1 (1) |
| Précision de la donnée | vide | 0 | 100.00 | 0 |  |  |  |

## Contrôles propres à la source

- Doublons sur la cle (`Année`, `Numéro`) : 0 lignes sur 4694.
- Lignes entierement identiques : 0.
- Feux differents avec la meme commune et la meme date et heure d'alerte (doublons possibles a examiner) : 86 lignes.
- `Code INSEE` au format attendu (5 caracteres, 2A ou 2B possibles) : 4694 conformes, 0 non conformes, 0 vides. Communes distinctes : 124.
- `Date de première alerte` illisible ou vide : 0 lignes. Periode couverte : du 2006-01-11 16:03:00 au 2025-12-24 19:35:00.
- `Année` differente de l'annee de la date d'alerte : 0 lignes.
- Dates d'alerte dans le futur : 0.
- `Surface parcourue (m2)` : 0 vides, 0 negatives, 0 egales a 0. Mediane 200 m2, maximum 32 210 000 m2 (3221 ha).
- Feux de plus de 1 ha (strictement) : 383 ; d'au moins 1 ha : 472 ; dont exactement 1 ha : 89.
- Feux de plus de 50 ha (strictement) : 18 ; d'au moins 50 ha : 18 ; dont exactement 50 ha : 0.
- Feux hors juin-septembre : 2185 (46.5 %).
- Annees sans aucun feu entre 2006 et 2025 : aucune.
- Feux par annee : 2006 : 407, 2007 : 420, 2008 : 219, 2009 : 378, 2010 : 275, 2011 : 354, 2012 : 245, 2013 : 192, 2014 : 219, 2015 : 300, 2016 : 247, 2017 : 318, 2018 : 121, 2019 : 217, 2020 : 144, 2021 : 164, 2022 : 184, 2023 : 86, 2024 : 111, 2025 : 93.
- `Nature` (cause) vide : 2212 lignes (47.1 %).
- Part de `Nature` vide par annee (%) : 2006 : 28.7, 2007 : 41.4, 2008 : 48.9, 2009 : 57.4, 2010 : 61.8, 2011 : 52.8, 2012 : 58.8, 2013 : 39.6, 2014 : 38.4, 2015 : 70, 2016 : 53, 2017 : 59.1, 2018 : 33.9, 2019 : 34.6, 2020 : 31.9, 2021 : 33.5, 2022 : 43.5, 2023 : 47.7, 2024 : 30.6, 2025 : 37.6.

## Repérage des données personnelles

Colonnes signalées automatiquement (nom de colonne ou contenu). Un signal n'est pas une conclusion : chaque colonne est à examiner.

| Colonne | Signal |
|---|---|
| Nom de la commune | nom de colonne contenant : nom |
| Décès ou bâtiments touchés | nom de colonne contenant : deces, batiment |
| Nombre de décès | nom de colonne contenant : deces |
| Nombre de bâtiments totalement détruits | nom de colonne contenant : batiment |
| Nombre de bâtiments partiellement détruits | nom de colonne contenant : batiment |
