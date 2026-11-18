# Analyse de la commande - Biolohf Tchatchoua

## 1. Les questions

1. **Où les départs de feu sont-ils les plus fréquents dans le 2A ?**  
   Si les feux se produisent surtout dans certaines zones, le SDIS peut y envoyer plus de moyens. Si les feux sont répartis partout, les moyens doivent être répartis sur tout le département.

2. **À chaque niveau de l’indice, combien de jours ont eu au moins un départ de feu ?**  
   Si beaucoup de jours avec un niveau d’alerte élevé ne donnent aucun feu, le seuil est peut-être trop bas. Si des feux démarrent même avec un niveau faible, il faut peut-être le baisser.

3. **Combien de jours par été dépasseraient les différents seuils possibles ?**  
   Si un seuil entraîne trop de jours de renfort, il coûtera trop cher. Il faut donc choisir un seuil qui permet de protéger les zones à risque sans dépasser le budget.

4. **Le lien entre l’indice et les feux est-il le même en Corse-du-Sud qu’en Haute-Corse et dans le reste de la France ?**  
   Si le lien est semblable, on peut utiliser les données régionales et nationales. Sinon, il faudra calculer un seuil spécifique pour la Corse-du-Sud.

## 2. Les termes inconnus

| Terme | Ce que je pense qu’il veut dire | Ce qu’il faut vérifier |
|---|---|---|
| Météo des forêts | Un indice qui mesure chaque jour le risque d’incendie selon la météo | Quel indice est utilisé, à quelle échelle et quels sont ses niveaux |
| Danger élevé | Un niveau de l’indice au-dessus d’une certaine valeur | Quelle valeur correspond à ce niveau |
| Feu de forêt / départ de feu | Un incendie qui commence dans un espace naturel | Si toutes les sources comptent les mêmes feux |
| Dispositif renforcé | Des patrouilles, du guet et des moyens supplémentaires | Ce que comprend exactement ce dispositif et combien il coûte par jour |
| Département | Le département administratif de la Corse-du-Sud (2A) | Si le périmètre du SDIS est le même que celui du département |

## 3. Les besoins

**La décision à éclairer :** décider où concentrer les moyens du SDIS 2A et à partir de quel niveau de l’indice activer le dispositif renforcé en 2027.

**Ce qui manque dans la commande :**

- Le seuil actuel et le niveau appelé « danger élevé ».
- La définition exacte d’un « feu » : faut-il compter tous les départs, même les petits, ou seulement certains incendies ?
- La période à analyser : combien d’années ou d’étés faut-il étudier ?
- Le budget disponible, pour savoir combien de jours de renfort sont possibles.

## 4. Les données

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Liste des départs de feu avec leur localisation | Un départ de feu | Au moins 10 ans, dont 2026 | Annuelle | Corse-du-Sud, par commune |
| 2 | Indice quotidien et départs de feu | Un jour dans une zone | Au moins 10 ans | Quotidienne | Corse-du-Sud |
| 3 | Indice quotidien par zone | Un jour dans une zone | Au moins 10 étés | Quotidienne | Corse-du-Sud |
| 4 | Indice et départs de feu | Un jour dans un département | Au moins 10 ans | Quotidienne | 2A, 2B et France |

## 5. Confrontation aux sources

### Matrice

Degrés : complet, partiel, absent, inconnu. Chaque cellule cite la rubrique de la fiche ou la colonne du fichier qui la justifie.

| Question | Météo des forêts | BDIFF | DDT 2A | Prométhée | Interventions SDIS | Admin Express | BD Forêt | Corine Land Cover |
|---|---|---|---|---|---|---|---|---|
| 1 | absent : aucune donnée de feu, seulement `niveau_j1` et `niveau_j2` par département (rubrique Grain) | partiel : `Code INSEE` et `Surface parcourue (m2)` de 2006 à 2025, saison 2026 non publiée (rubrique Période) | partiel : points de départ depuis 1973 (rubrique Grain), arrêtés à 2024, archive non ouverte (rubrique Période) | inconnu : aucun export ouvert | absent : une ligne par département et par année, sans commune ni date (rubrique Grain) | partiel : référentiel, `code_insee` des 124 communes du 2A, aucun feu (rubrique Grain) | partiel : dénominateur, surface boisée par polygone `TFV`, photos de 2011 (rubrique Période), fichier non ouvert | partiel : dénominateur, maille de 25 ha trop grossière pour une commune corse (rubrique Grain) |
| 2 | partiel : `niveau_j1` au grain jour x département, trois saisons seulement, 2024 à 2026 (rubrique Période) | partiel : `Date de première alerte` et `Département`, mais seulement les feux de juin à septembre 2024 et 2025, période commune avec l'indice | inconnu : date des points de départ non vérifiée (archive non ouverte) | inconnu : aucun export ouvert | absent : aucune donnée journalière (rubrique Grain) | absent : ni feu ni danger | absent : végétation seulement | absent : végétation seulement |
| 3 | partiel : `niveau_j1` permet de compter les jours par seuil (2024 à 2026), mais aucun coût du dispositif | partiel : `Date de première alerte` donne la part des feux couverts par les jours d'alerte, aucun coût | absent : aucun coût, dates non vérifiées | inconnu : aucun export ouvert | absent : ni donnée journalière ni coût (rubrique Grain) | absent : référentiel géographique | absent : végétation seulement | absent : végétation seulement |
| 4 | partiel : 96 départements (rubrique Emprise), trois saisons seulement, Haute-Corse non vérifiée | inconnu : France entière selon le site (rubrique Emprise), mais export ouvert limité au 2A (rubrique Volumétrie) | absent : Corse-du-Sud uniquement (rubrique Emprise) | inconnu : zone méditerranéenne selon la fiche, aucun export ouvert | absent : grain année x département, ne relie pas le niveau d'un jour aux feux de ce jour (rubrique Grain) | partiel : référentiel, `code_insee_du_departement` sépare 2A, 2B et le reste de la France | partiel : dénominateur, millésimes différents selon les départements, 2007 à 2018 (rubrique Période) | partiel : dénominateur, même règle pour toute la France, colonne `CLC_3`, millésime 2018 |

### Écarts avec la section 4

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | BDIFF | = | au moins 10 ans, dont 2026 → 2006 à 2025 | annuelle → bilan publié l'année suivante (2026 en 2027) | = |
| 2 | Météo des forêts + BDIFF | un jour dans une zone → un jour x un département | au moins 10 ans → juin à septembre 2024 et 2025 en commun | quotidienne → quotidienne pour l'indice, annuelle pour les feux | = |
| 3 | Météo des forêts | un jour dans une zone → un jour x un département | au moins 10 étés → trois saisons, 2024 à 2026 | = | = |
| 4 | Météo des forêts + BDIFF | = | au moins 10 ans → 2024 et 2025 en commun | quotidienne → quotidienne pour l'indice, annuelle pour les feux | 2A, 2B et France → 2A seulement extrait (BDIFF), 2B non vérifiée (Météo des forêts) |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1 | Feux de la saison 2026 | collecter | Le SDIS 2A saisit ses feux et peut transmettre 2026 ; en attendant, la BDIFF (2006 à 2025) suffit pour classer les zones | Dépend d'une réponse avant le 11 décembre ; sans elle, les évolutions de 2026 ne sont pas visibles |
| 2 | Historique de l'indice sur plus de trois saisons | approximer | Croiser `niveau_j1` (prévision) avec les feux BDIFF de juin à septembre 2024 et 2025. Mesure mal le niveau réellement observé, et ignore les feux hors saison (46,5 %) | Échantillon réduit (139 feux dans le 2A) : taux fragiles |
| 3 | Coût par jour du dispositif et seuil actuel | collecter | Seul le SDIS 2A les connaît ; le nombre de jours par seuil se calcule déjà avec la Météo des forêts | Dépend d'une réponse avant le 11 décembre ; sinon, résultat exprimé en jours et non en euros |
| 4 | Feux de la Haute-Corse et de la France, présence du 2B dans l'indice | vérifier d'abord, puis approximer | Cellules « inconnu » : exporter la BDIFF pour le 2B et la France, contrôler le 2B dans la Météo des forêts | Temps d'extraction ; comparaison limitée aux deux saisons communes |
