# Règles de qualité et rapport de qualité : BDIFF Corse-du-Sud

- **Ticket :** #22 (règles de qualité initiales et repérage des données personnelles)
- **Auteur :** Ahmed Philippe (responsable qualité et conformité)
- **Date :** 2026-11-23
- **Source commune :** BDIFF, Corse-du-Sud, type de feu « F », 2006-2025 (`data/raw/bdiff_2A_2006_2025.csv`, 4 694 feux, couche bronze, D-015)
- **Profil :** `docs/qualite/profil-bdiff.md` (S3, travail personnel, étape 1)
- **Calculs :** `python src/regles_qualite.py data/raw/bdiff_2A_2006_2025.csv` refait toutes les valeurs de ce fichier et applique la barrière de qualité (le script s'arrête si une règle bloquante échoue).

## Pourquoi ces trois règles

Le pipeline (`src/pipeline.py`, PR #93) bloque déjà sur les contrôles de contrat : champs requis non vides, clé (`Année`, `Numéro`) unique, surface positive, code INSEE corse, année cohérente avec la date. Ces contrôles passent tous. Les trois règles ci-dessous portent sur ce qu'ils ne voient pas, et sur ce dont les indicateurs ont besoin : un feu compté une seule fois (unicité), aucune période manquante (complétude des périodes) et des surfaces cohérentes (cohérence dans la ligne). Leurs seuils sont tirés du profil de la Corse-du-Sud.

## Les règles

### R1 · Alertes simultanées dans une même commune (unicité, test d'ensemble)

| Composant | Contenu |
|---|---|
| Sélecteur | Tous les feux, regroupés par `Année`. |
| Prédicat | Deux feux de la même commune (`Code INSEE`) n'ont pas la même `Date de première alerte` à la minute près. On compte les feux « en trop » : tous ceux d'un groupe sauf le premier. |
| Seuil | Au plus **2,0 %** de feux en trop par année. |
| Justification du seuil | Le profil signale 86 feux partageant commune, date et heure (46 en trop, 1,0 % des 4 694 feux). De 2006 à 2023, la part annuelle ne dépasse jamais 2,0 % (maximum en 2016). Au-delà, la saisie a changé ou une série de départs gonfle les comptes. |
| Décision | **Alerter.** Ces feux ont des numéros et des surfaces différents (dans 34 groupes sur 40, les surfaces diffèrent) : ce sont probablement des départs multiples réels, par exemple une série de mises à feu, et non des doublons à supprimer. On ne les supprime pas ; on publie l'indicateur dans les deux comptes. |
| Résultat | **Échec** : 5,4 % en 2024 (6 feux en trop sur 111) et 4,3 % en 2025 (4 sur 93). Exemple tiré du fichier : le 13 août 2024 à 01 h 24, quatre feux ont la même heure d'alerte, deux à Appietto et deux à Calcatoggio. |

### R2 · Périodes présentes et volume plausible (complétude des périodes, test d'ensemble)

| Composant | Contenu |
|---|---|
| Sélecteur | Le nombre de feux par `Année`, de 2006 à 2025. |
| Prédicat | R2a : chaque année contient au moins un feu. R2b : le nombre de feux d'une année atteint au moins le seuil, rapporté à la moyenne des 5 années précédentes (seuil adaptatif, comme le recommande le cours quand l'attendu varie avec la saison). |
| Seuil | R2a : **0 année absente**. R2b : au moins **40 %** de la moyenne des 5 années précédentes. |
| Justification du seuil | Un fichier qui s'arrête avant la fin de l'année ou à qui il manque une saison passe tous les tests de ligne. Le profil montre aucune année sans feu, et de 2011 à 2025 le plus bas rapport observé est **47 % (2018 : 121 feux pour une moyenne de 255)**, une année calme et non un fichier incomplet. Le seuil de 40 % reste sous la variation observée, pour ne pas alerter sur une année calme (fatigue d'alerte). |
| Décision | R2a : **bloquer** (une période entière manque, les comparaisons entre années deviennent fausses). R2b : **alerter**, puis vérifier le nombre de feux de l'année auprès de la BDIFF ou du SDIS avant de publier. |
| Résultat | **Réussite** pour les deux : aucune année absente, aucune année sous 40 %. |

### R3 · Surface totale égale à la somme de son détail (cohérence dans la ligne, test de ligne)

| Composant | Contenu |
|---|---|
| Sélecteur | Les feux qui ont au moins une sous-surface renseignée (forêt, maquis et garrigues, autres surfaces naturelles, agricoles, autres, non boisées, etc.). |
| Prédicat | `Surface parcourue (m2)` égale la somme des sous-surfaces renseignées. |
| Seuil | **0 ligne fautive.** |
| Justification du seuil | La surface parcourue est le champ du garde-fou I2 (part des hectares brûlés dans les communes prioritaires) et de toutes les analyses de surfaces. Le profil montre des sous-surfaces souvent vides (36,5 % pour la forêt, 42,2 % pour les surfaces non boisées) : la règle vérifie que, là où le détail existe, il ne contredit pas le total. C'est une règle de contrat : aucune tolérance. |
| Décision | **Bloquer** : une surface incohérente fausserait les surfaces brûlées sans que rien ne le montre. |
| Résultat | **Réussite** : les 4 694 feux ont un détail, et dans les 4 694 cas la somme égale la surface parcourue. |

## Rapport de qualité

| Règle | Portée | Seuil | Résultat | Sévérité | Décision |
|---|---|---|---|---|---|
| R1 alertes simultanées | tous les feux, par année | au plus 2,0 % de feux en trop par année | échec : 5,4 % en 2024, 4,3 % en 2025 | alerter | indicateurs publiés en feux et en alertes distinctes ; question à poser au SDIS 2A |
| R2a année absente | 2006 à 2025 | 0 année sans feu | réussite : 0 | bloquer | chargement autorisé |
| R2b volume annuel | 2011 à 2025 | au moins 40 % de la moyenne des 5 années précédentes | réussite : minimum 47 % (2018) | alerter | aucune vérification nécessaire |
| R3 surfaces cohérentes | 4 694 feux avec détail | 0 ligne fautive | réussite : 0 | bloquer | chargement autorisé |

**Barrière de qualité : aucune règle bloquante en échec, une alerte (R1).** Les données sont chargées ; l'alerte R1 est reportée sur les indicateurs.

### Effet de l'alerte R1 sur un indicateur du groupe

L'indicateur I1 de la Q1 (part des feux de l'été partis dans les 20 communes prioritaires, `kpi/fiche-indicateurs-ahmed-philippe.md`) vaut **53,2 %** (74 feux sur 139, étés 2024-2025) en comptant chaque feu. En comptant une seule fois les feux d'une même commune à la même minute, il vaut **49,6 %** (64 alertes sur 129). Les 10 feux en trop des étés 2024-2025 sont tous dans des communes de la liste.

C'est un faux signal de confiance au sens du cours : sur l'ensemble du fichier, les alertes simultanées ne pèsent que 1,0 % des feux, mais elles pèsent 7,2 % (10 sur 139) des étés 2024-2025, la période de référence des objectifs. Tant que le SDIS 2A n'a pas dit si une série de départs à la même minute compte pour un ou plusieurs départs, I1 est publié avec les deux valeurs.

## Ce que nos indicateurs peuvent affirmer, et ce qu'ils ne peuvent pas

| Les indicateurs peuvent affirmer | Parce que |
|---|---|
| Le nombre de feux par année et par commune, de 2006 à 2025 | Aucune année absente (R2a), volumes plausibles (R2b), clé unique et communes au bon format (pipeline). |
| Les surfaces brûlées, par feu, par commune et par année | Surfaces toutes renseignées, positives, et cohérentes avec leur détail (R3). |
| La répartition des feux selon le niveau de la Météo des forêts, en été | Aucun bulletin manquant sur les jours publiés (`docs/qualite/profil-mdf.md`). |

| Les indicateurs ne peuvent pas affirmer | Parce que |
|---|---|
| Un nombre exact de « départs » en 2024 et 2025 | Les alertes simultanées (R1) changent les comptes de 7 % sur les étés de référence ; la définition d'un départ reste à fixer avec le SDIS 2A (glossaire, « Feu de forêt » : à harmoniser). |
| La cause des feux | `Nature` est vide pour 47,1 % des feux, et ce taux varie de 28,7 % (2006) à 70 % (2015) selon l'année : le manque dépend de l'année (manque de type MAR), un indicateur par cause comparerait des années mal renseignées à des années bien renseignées. |
| Le moment exact du départ | Le fichier donne l'heure de la première alerte, pas l'heure du départ : un feu parti tard le soir peut être rattaché au jour suivant. |
| Qu'une commune absente n'a pas eu de feu | Le test de population demande un référentiel des communes ; il n'est pas encore dans le dépôt. Les 124 communes du 2A ont toutes au moins un feu, mais en Haute-Corse 226 communes sur 236 ont un feu, sans que l'on puisse distinguer une commune sans feu d'un feu non saisi. |
| Les feux hors de juin à septembre, du point de vue du danger météo | 46,5 % des feux partent hors de cette période, où la Météo des forêts n'est pas publiée. |

## Repérage des données personnelles

Le profil signale automatiquement cinq colonnes (`Nom de la commune`, `Décès ou bâtiments touchés`, `Nombre de décès`, `Nombre de bâtiments totalement détruits`, `Nombre de bâtiments partiellement détruits`). Examen colonne par colonne :

| Colonne | Donnée personnelle ? | Constat dans le fichier | Décision |
|---|---|---|---|
| `Nom de la commune`, `Code INSEE` | Non : c'est un lieu, pas une personne. | 124 communes. | Utilisable à tous les niveaux. |
| `Décès ou bâtiments touchés` et les trois nombres associés | Pas directement, mais **un événement rare devient identifiable** : avec la commune et la date, on retrouve le bâtiment et donc ses propriétaires. | Un seul feu concerné en 20 ans (2024, un bâtiment partiellement détruit). | Jamais affiché feu par feu ni dans une case qui ne contient qu'un feu ; utilisable seulement en total. |
| `Nature` = « Malveillance » | Pas directement, mais elle désigne une infraction possible : rattachée à une commune et à une heure précises, elle peut renvoyer à une enquête en cours. | 767 feux en 2A. | Utilisable seulement en agrégé (par année, par département) ; pas de visuel qui montre un feu de malveillance avec sa commune et sa date. |
| Toutes les autres colonnes | Non. | Aucun nom de personne, aucune adresse, aucune coordonnée précise (le lieu s'arrête à la commune). | Aucune restriction. |

**Règle de restitution proposée :** dans le tableau de bord, aucune case croisant la cause ou les dégâts avec une commune ne s'affiche si elle contient moins de 5 feux (elle est regroupée ou masquée). Ce seuil est à valider avec le groupe ; il complète D-015, qui interdit de modifier les données mais n'impose rien sur leur affichage.

## Limites

- Les seuils sont fixés sur la Corse-du-Sud. Appliquées à la Haute-Corse, les mêmes règles donnent d'autres résultats : R1 dépasse 2 % neuf années sur vingt (jusqu'à 3,7 % en 2009) et R2b alerte en 2018 (31 % de la moyenne). La Haute-Corse a son propre régime ; ses seuils sont à fixer sur son propre profil avant toute comparaison entre les deux départements.
- R1 ne dit pas si les feux simultanés sont des doublons ou des départs multiples réels : seul le SDIS 2A peut le dire. La règle rend le problème visible, elle ne le tranche pas.
- R2b ne voit pas un mois manquant à l'intérieur d'une année ; le mois d'été le plus faible du fichier compte 1 feu (juin 2023), ce qui rend un test par mois peu discriminant sans plus d'historique.
- Aucune règle d'exactitude par référentiel externe : la BDIFF est elle-même la source de référence pour les feux (décision 5 de `docs/sources/matrice.md`), et le fichier du SDIS 2A (interventions) n'est pas disponible.
