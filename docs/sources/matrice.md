# Matrice questions x sources (v0)

- **Tenue par :** Biolohf Tchatchoua (responsable sources)
- **Contributions :** Arouna Touré (relecture et mise à jour des cellules à partir des fiches)
- **Date :** 2026-11-18
- **Ticket :** #20

Une ligne par question retenue par le groupe, une colonne par source de l'inventaire (`docs/sources/inventaire.md`). Les questions sont les quatre questions communes de `docs/analyse/commande-groupe.md` ; les quatre membres les ont posées sous une forme ou une autre dans leur analyse individuelle.

## Questions

| N° | Question | Décision de la direction | Posée par |
|---|---|---|---|
| Q1 | Où se concentrent les départs de feu en Corse-du-Sud ? | Où placer les moyens | Saran, Biolohf, Ahmed, Arouna |
| Q2 | À chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu ? | Relever ou abaisser le seuil | Saran, Biolohf, Ahmed, Arouna |
| Q3 | Combien de jours par été chaque seuil envisagé aurait-il déclenché, et quelle part des feux ces jours auraient-ils couverte ? | Choisir un seuil tenable dans le budget | Biolohf, Ahmed, Arouna |
| Q4 | Le lien entre l'indice et les feux est-il le même en Haute-Corse et dans le reste de la France ? | S'appuyer ou non sur des données régionales et nationales | Saran, Biolohf, Ahmed, Arouna |

## Matrice

Degrés de la consigne : **complet** (répond au grain, sur la période et l'emprise nécessaires), **partiel** (grain trop large, période trop courte, emprise incomplète, donnée indirecte), **absent** (rien d'utile), **inconnu** (non vérifié dans le fichier ou sa documentation). Chaque degré cite la colonne du fichier ou la rubrique de la fiche qui le justifie.

| Question | Météo des forêts | BDIFF | DDT 2A | Prométhée | Interventions SDIS | Admin Express | BD Forêt | Corine Land Cover |
|---|---|---|---|---|---|---|---|---|
| Q1 | absent : aucune donnée de feu, seulement `niveau_j1` / `niveau_j2` par département (rubrique Grain) | partiel : `Code INSEE` et `Surface parcourue (m2)` sur 2006-2025, mais saison 2026 non publiée (rubrique Période) | partiel : points de départ depuis 1973 (rubrique Grain), mais données arrêtées à 2024 et archive non ouverte (rubrique Période) | inconnu : aucun export ouvert (toutes rubriques non vérifiées) | absent : une ligne par département et par année, ni commune ni date (rubrique Grain) | partiel : référentiel, `code_insee` des 124 communes du 2A ; ne contient aucun feu (rubrique Grain) | partiel : dénominateur, surface boisée par polygone `TFV`, photos de 2011 pour le 2A (rubrique Période) ; fichier non ouvert | partiel : dénominateur, maille de 25 ha trop grossière pour une commune corse (rubrique Grain) |
| Q2 | partiel : `niveau_j1` au grain jour x département, mais trois saisons seulement, 2024 à 2026 (rubrique Période) | partiel : `Date de première alerte` et `Département`, mais 139 feux seulement sur juin-septembre 2024-2025, période commune avec l'indice | inconnu : date des points de départ non vérifiée (archive non ouverte) | inconnu : aucun export ouvert | absent : aucune donnée journalière (rubrique Grain) | absent : aucune donnée de feu ni de danger | absent : végétation seulement | absent : végétation seulement |
| Q3 | partiel : `niveau_j1` permet de compter les jours par seuil (2024-2026), mais aucun coût du dispositif | partiel : `Date de première alerte` donne la part des feux couverts par les jours d'alerte, mais aucun coût | absent : aucun coût ; dates non vérifiées | inconnu : aucun export ouvert | absent : aucune donnée journalière ni de coût | absent | absent | absent |
| Q4 | partiel : 96 départements (rubrique Emprise), mais trois saisons, et Haute-Corse non vérifiée | inconnu : France entière selon le site (rubrique Emprise), mais export limité au 2A (rubrique Volumétrie) | absent : Corse-du-Sud uniquement (rubrique Emprise) | inconnu : couvre la zone méditerranéenne selon la fiche, rien d'ouvert | absent : grain année x département, ne permet pas de relier le niveau d'un jour aux feux de ce jour ; contexte seulement | partiel : référentiel, `code_insee_du_departement` sépare 2A, 2B et le reste de la France | partiel : dénominateur, mais millésimes différents selon les départements (2007 à 2018, rubrique Période) | partiel : dénominateur, même règle pour toute la France ; colonne `CLC_3` (forêts et milieux semi-naturels), millésime 2018 (fiche mise à jour, CSV communal ouvert). Points d'attention : codes communes du COG 2010, et doublons des versions « révisées » à filtrer sur `base` |

## Lecture dans les deux sens

**Questions vers sources.** Aucune question n'a de source "complet". La saison 2026 manque pour les feux, l'indice n'a que trois saisons, et le coût du dispositif n'existe dans aucune source.

**Écart avec l'inventaire.** L'inventaire note la BDIFF "Oui" pour Q1 parce qu'elle répond au bon grain (le feu, rattaché à sa commune) ; la matrice la note "partiel" parce qu'elle applique en plus la période attendue, et la saison 2026 n'est pas publiée. Les deux lectures sont cohérentes : la matrice est la plus stricte et c'est elle qui fait foi pour les décisions.

**Sources vers questions.**

- **Interventions SDIS** : aucune cellule utile pour Q1 à Q4. Source à écarter du pipeline, ou à garder pour un contrôle de cohérence : comparer chaque année ses "Feux de végétations" au nombre de feux de la BDIFF (en 2024 pour le 2A : 375 "Feux de végétations" dans le fichier `interventions2024.csv`, rubrique Ce que nous avons découvert de la fiche Interventions SDIS, contre 111 feux de forêt dans l'export BDIFF de la fiche, lignes où `Année` = 2024 ; les deux notions ne recouvrent pas les mêmes événements).
- **Prométhée** : "inconnu" partout. Une vérification est nécessaire avant toute décision ; sinon, source à écarter pour la v1.

## Écarts avec la donnée idéale

Pour chaque question, comparaison de la donnée idéale (`commande-groupe.md`, section 4) à la meilleure source disponible : "idéal -> réel", ou "=".

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
|---|---|---|---|---|---|
| Q1 | BDIFF | = | au moins 10 ans dont 2026 -> 2006 à 2025 | bilan annuel -> bilan publié l'année suivante (2026 en 2027) | = |
| Q2 | Météo des forêts + BDIFF | = | toutes les saisons -> juin-septembre 2024 et 2025 en commun | quotidienne -> quotidienne pour l'indice, annuelle pour les feux | = |
| Q3 | Météo des forêts + BDIFF | jour x département et coût par jour d'activation -> jour x département sans coût | toutes les saisons -> juin-septembre 2024 et 2025 en commun | = | = |
| Q4 | Météo des forêts + BDIFF | = | toutes les saisons -> 2024 et 2025 en commun | idem Q2 | 2A, 2B et France -> 2A seulement extrait (BDIFF), 2B non vérifiée (Météo des forêts) |

## Décisions

À consigner une à une dans `docs/decisions.md`.

| N° | Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|---|
| 1 | Q1 | Feux de 2026 | collecter, à défaut approximer | Le SDIS 2A saisit ses feux et peut nous transmettre 2026 ; sans réponse, la BDIFF (20 saisons à la commune, 2006-2025) suffit pour classer les zones, mais 2026 ne sera publiée qu'en 2027 | Dépend d'une réponse du SDIS avant le 11 décembre ; sans elle, les évolutions de 2026 ne sont pas visibles |
| 2 | Q2 | Historique de l'indice (trois saisons) | approximer | Croiser `niveau_j1` (prévision J+1) avec les feux BDIFF de juin à septembre 2024 et 2025 ; élargir l'échantillon grâce à Q4 | 139 feux pour le 2A : taux fragiles ; les 46,5 % de feux hors saison restent hors du champ de l'indice |
| 3 | Q3 | Coût journalier du dispositif, seuil actuel | collecter | Seul le SDIS 2A les connaît ; le nombre de jours par seuil se calcule déjà avec la Météo des forêts | Dépend d'une réponse avant le 11 décembre ; sans elle, résultat exprimé en jours et non en euros |
| 4 | Q4 | Feux de la Haute-Corse et de la France ; présence du 2B dans l'indice | vérifier, puis approximer | Les cellules "inconnu" appellent d'abord une vérification : exporter la BDIFF pour le 2B et la France, contrôler le 2B dans la Météo des forêts | Temps d'extraction ; comparaison limitée à deux saisons communes |
| 5 | Q1 à Q4 | Source de référence pour les feux | désigner la BDIFF comme source de référence | Seule base nationale vérifiée, avec date et commune ; la source DDT 2A la reprend depuis 2023 | DDT 2A gardée en complément pour la localisation ; en cas de désaccord depuis 2023, la BDIFF prévaut |
| 6 | Q1, Q4 | Dénominateur de surface boisée | voir D-008 (proposition à confirmer par le groupe) : BD Forêt pour Q1, Corine Land Cover pour Q4 ; millésime 2018 de Corine : voir D-007 | Ne jamais additionner les deux sources (règles différentes) ; Corine applique la même règle partout | Deux sources de surface à documenter, millésimes anciens (2011 et 2018) |
