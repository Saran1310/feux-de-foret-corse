# Profil de la source : BDIFF

- **Généré par :** `src/profilage.py` le 2026-11-18
- **Fichiers lus :** `data/raw/bdiff_2B_2006_2025.csv`
- **Lignes :** 4992
- **Colonnes :** 24

Ce rapport décrit les données telles qu'elles sont. Il ne décide rien : les règles de qualité et leurs seuils sont fixés à partir de ces constats.

## Informations du fichier

- Certaines données sont associées à l'ancienne version du formulaire incendie. Consultez la documentation pour plus d'informations.
- Nombre d'incendies suivant les critères de sélection : 4992
- Critères de sélection => ; Date de première alerte, de : 2006-01-01 00:00:00 ; Date de première alerte, jusqu'à : 2025-12-31 23:59:00 ; Département(s) : 2B ; Type de feu : F

## Profil des colonnes

| Colonne | Type observe | Non vides | Vides (%) | Distinctes | Min | Max | 3 valeurs les plus frequentes |
|---|---|---|---|---|---|---|---|
| Année | entier | 4992 | 0.00 | 20 | 2006 | 2025 | 2007 (544), 2006 (485), 2011 (396) |
| Numéro | entier | 4992 | 0.00 | 4282 | 26 | 25 787 | 4859 (5), 7152 (4), 6663 (4) |
| Département | texte | 4992 | 0.00 | 1 |  |  | 2B (4992) |
| Code INSEE | texte | 4992 | 0.00 | 226 |  |  | 2B185 (191), 2B049 (167), 2B143 (132) |
| Nom de la commune | texte | 4992 | 0.00 | 226 |  |  | Oletta (191), Calenzana (167), Linguizzetta (132) |
| Date de première alerte | date | 4992 | 0.00 | 4829 | 2006-01-15 16:11 | 2025-10-27 18:12 | 2014-10-25 00:21:00 (5), 2006-08-01 23:03:00 (4), 2007-09-18 19:13:00 (3) |
| Surface parcourue (m2) | entier | 4992 | 0.00 | 579 | 1 | 21 180 000 | 100 (260), 10 (258), 1000 (254) |
| Surface forêt (m2) | entier | 4675 | 6.35 | 400 | 0 | 6 349 200 | 0 (688), 5 (222), 47 (200) |
| Surface maquis garrigues (m2) | entier | 4875 | 2.34 | 559 | 0 | 18 900 000 | 5 (224), 48 (200), 96 (198) |
| Autres surfaces naturelles hors forêt (m2) | entier | 4105 | 17.77 | 22 | 0 | 1 023 500 | 0 (4077), 5000 (4), 3000 (2) |
| Surfaces agricoles (m2) | entier | 449 | 91.01 | 12 | 0 | 450 000 | 0 (436), 30000 (2), 25000 (2) |
| Autres surfaces (m2) | entier | 449 | 91.01 | 7 | 0 | 42 400 | 0 (443), 100 (1), 2600 (1) |
| Surface autres terres boisées (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées naturelles (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées artificialisées (m2) | vide | 0 | 100.00 | 0 |  |  |  |
| Surfaces non boisées (m2) | entier | 4085 | 18.17 | 303 | 0 | 3 001 937 | 0 (607), 1 (279), 2 (241) |
| Précision des surfaces | texte | 449 | 91.01 | 2 |  |  | Estimées (438), Mesurées (11) |
| Type de peuplement | entier | 2376 | 52.40 | 6 | 1 | 6 | 1 (1891), 2 (223), 3 (118) |
| Nature | texte | 2647 | 46.98 | 5 |  |  | Malveillance (1685), Involontaire (particulier) (340), Naturelle (252) |
| Décès ou bâtiments touchés | texte | 449 | 91.01 | 2 |  |  | Non (447), Oui (2) |
| Nombre de décès | entier | 2 | 99.96 | 1 | 0 | 0 | 0 (2) |
| Nombre de bâtiments totalement détruits | entier | 2 | 99.96 | 2 | 0 | 1 | 0 (1), 1 (1) |
| Nombre de bâtiments partiellement détruits | entier | 2 | 99.96 | 2 | 0 | 1 | 1 (1), 0 (1) |
| Précision de la donnée | vide | 0 | 100.00 | 0 |  |  |  |

## Contrôles propres à la source

- Doublons sur la cle (`Année`, `Numéro`) : 0 lignes sur 4992.
- Lignes entierement identiques : 0.
- Feux differents avec la meme commune et la meme date et heure d'alerte (doublons possibles a examiner) : 192 lignes.
- `Code INSEE` au format attendu (5 caracteres, 2A ou 2B possibles) : 4992 conformes, 0 non conformes, 0 vides. Communes distinctes : 226.
- `Date de première alerte` illisible ou vide : 0 lignes. Periode couverte : du 2006-01-15 16:11:00 au 2025-10-27 18:12:00.
- `Année` differente de l'annee de la date d'alerte : 0 lignes.
- Dates d'alerte dans le futur : 0.
- `Surface parcourue (m2)` : 0 vides, 0 negatives, 0 egales a 0. Mediane 1000 m2, maximum 21 180 000 m2 (2118 ha).
- Feux de plus de 1 ha : 1098.
- Feux de plus de 50 ha : 62.
- Feux hors juin-septembre : 2651 (53.1 %).
- Annees sans aucun feu entre 2006 et 2025 : aucune.
- Feux par annee : 2006 : 485, 2007 : 544, 2008 : 190, 2009 : 271, 2010 : 137, 2011 : 396, 2012 : 368, 2013 : 261, 2014 : 322, 2015 : 249, 2016 : 236, 2017 : 319, 2018 : 87, 2019 : 145, 2020 : 143, 2021 : 177, 2022 : 213, 2023 : 246, 2024 : 119, 2025 : 84.
- `Nature` (cause) vide : 2345 lignes (47.0 %).
- Part de `Nature` vide par annee (%) : 2006 : 22.5, 2007 : 37.7, 2008 : 41.1, 2009 : 23.6, 2010 : 39.4, 2011 : 54.8, 2012 : 40.8, 2013 : 44.1, 2014 : 64.3, 2015 : 62.2, 2016 : 52.5, 2017 : 68.3, 2018 : 43.7, 2019 : 64.1, 2020 : 67.1, 2021 : 63.3, 2022 : 36.2, 2023 : 48.4, 2024 : 80.7, 2025 : 21.4.

## Repérage des données personnelles

Colonnes signalées automatiquement (nom de colonne ou contenu). Un signal n'est pas une conclusion : chaque colonne est à examiner.

| Colonne | Signal |
|---|---|
| Nom de la commune | nom de colonne contenant : nom |
| Décès ou bâtiments touchés | nom de colonne contenant : deces, batiment |
| Nombre de décès | nom de colonne contenant : deces |
| Nombre de bâtiments totalement détruits | nom de colonne contenant : batiment |
| Nombre de bâtiments partiellement détruits | nom de colonne contenant : batiment |
