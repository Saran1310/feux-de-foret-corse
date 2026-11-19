# Objectif : Saran Diabagate

- **Séance :** UE01.B, S1 (de la question analytique à l'objectif)
- **Date :** 2026-11-19
- **Ticket :** #71
- **Données utilisées :** Météo des forêts (`niveau_j1`, saisons 2024 et 2025, 96 départements) et BDIFF (feux de forêt de type F de toute la France métropolitaine, `Date de première alerte`, 3 908 feux du 2024-01-01 au 2025-12-31). Les calculs sont refaits par `src/analyse_comparaison.py`. Lecture des dates selon la fiche Météo des forêts : `niveau_j1` concerne le lendemain de la publication, les heures sont en UTC.
- **Origine des fichiers :** export BDIFF « France entière » (type F, du 2024-01-01 au 2025-12-31) sur bdiff.agriculture.gouv.fr et fichiers des saisons 2024 et 2025 de la Météo des forêts sur data.gouv.fr, téléchargés le 2026-11-19. Les fichiers bruts ne sont pas dans le dépôt (le dossier `data/raw` n'est pas versionné) : pour refaire le calcul, `python src/analyse_comparaison.py bdiff_france.csv mdf_2024.csv mdf_2025.csv`.

## Question analytique

À chaque niveau de la Météo des forêts, la part des jours avec au moins un départ de feu est-elle comparable en Corse-du-Sud (2A), en Haute-Corse (2B) et dans les autres départements ? (Q4 de `docs/analyse/commande-groupe.md`.)

## Décision que la réponse nourrit

Sur quelles données le SDIS 2A peut-il fixer son seuil de déclenchement du dispositif renforcé pour 2027. Si le lien entre l'indice et les feux est le même ailleurs, il peut s'appuyer sur des données régionales ou nationales, bien plus nombreuses que les siennes. S'il diffère, il doit fixer un seuil propre au 2A.

## Trois formulations

| Formulation | Texte | Pourquoi ce n'est pas encore suffisant |
|---|---|---|
| Action | Comparer, pour chaque niveau, la part des jours avec feu en 2A, en 2B et dans les autres départements. | C'est ce que l'on fait, pas le résultat attendu : rien ne dit quand ce sera réussi. |
| Objectif | Choisir pour le 2A une base de données de référence dont le comportement est proche du sien. | Le résultat est nommé, mais sans écart mesurable, sans échéance et sans garde-fou : on peut le réussir en choisissant la base après coup. |
| Objectif SMART | Version provisoire : [y points] reste à fixer avec le SDIS 2A. **Étape 1, avant le 1er juin 2027 :** choisir, à partir des saisons 2024 et 2025, la base de référence qui sert à fixer le seuil de déclenchement en Corse-du-Sud, et figer sa part de jours avec au moins un feu aux niveaux 1 et 2 de la Météo des forêts. **Étape 2, en octobre 2027 :** vérifier que la part observée en 2027 dans le 2A s'écarte d'au plus [y points] de cette référence, à chacun des deux niveaux. Si l'écart dépasse la tolérance fixée, les résultats sont réexaminés afin de déterminer si la référence doit être ajustée pour 2028, car un écart peut aussi venir d'une saison différente (météo, nombre de feux). La saison 2027 couvre les bulletins publiés du 3 juin au 30 septembre, soit les jours du 4 juin au 1er octobre. Valeur de référence expérimentale : sur 2024-2025, avec la proportion globale des 94 autres départements, l'écart est de 14,6 points au niveau 1 et de 17,6 points au niveau 2. Les parts de référence ne sont pas recalculées avec les données 2027. Mesure en octobre 2027 sur les feux saisis par le SDIS 2A, confirmée avec la BDIFF en 2028. | |

## L'objectif SMART, critère par critère

| Critère | Contenu |
|---|---|
| Spécifique | La part des jours avec au moins un feu de forêt (type "F" de la BDIFF, toutes surfaces) en Corse-du-Sud, à chaque niveau de la prévision `niveau_j1` du lendemain, comparée à la part de la base de référence choisie. Un jour compte s'il a au moins un feu dont la `Date de première alerte` tombe ce jour-là. L'objectif porte sur les niveaux 1 et 2, les seuls qui ont assez de jours. |
| Mesurable | Écart en points = part observée en 2A pour un niveau, moins la part de la base pour ce niveau. Une part est le nombre de jours-départements avec au moins un feu divisé par le nombre de jours-départements du niveau, pour l'ensemble des départements du groupe (proportion globale, et non la moyenne des proportions de chaque département). Elle se calcule en croisant la Météo des forêts et la date de première alerte des feux. La BDIFF ne publiera l'année 2027 qu'en 2028 : la mesure d'octobre 2027 se fait sur les feux saisis par le SDIS 2A (à demander), puis elle est confirmée avec la BDIFF en 2028. |
| Atteignable | [y points] est fixé avec le SDIS 2A, une fois la situation de référence présentée, d'après ce que l'écart change pour lui (combien de jours de déclenchement en plus ou en moins) et d'après l'incertitude statistique. Il ne peut pas être très bas : sur deux saisons, la part du 2A est connue à environ 10 points près au niveau 1 (de 9,8 % à 29,4 %) et à environ 7 points près au niveau 2 (de 33,2 % à 48,0 %), et l'incertitude est plus grande pour la seule saison 2027. Un écart cible inférieur à ces marges mesurerait le hasard. Les écarts de 2024-2025 avec la Haute-Corse (6,3 et 9,7 points) et avec treize départements méditerranéens (8,0 et 8,5 points) sont dans cet ordre de grandeur, celui avec la moyenne des autres départements (14,6 et 17,6 points) est au-dessus. |
| Réaliste | Le garde-fou est que les parts de référence sont figées avant le 1er juin 2027, à partir des saisons 2024 et 2025. Sans lui, on atteindrait un écart nul en prenant les valeurs du 2A de 2027 comme référence. Les deux niveaux 1 et 2 doivent respecter l'écart en même temps. La qualité de la décision d'avant l'été ne dépend pas du résultat de 2027 : l'étape 2 sert à contrôler la référence, pas à juger la décision. |
| Temporel | Base choisie avant le 1er juin 2027, saison 2027 de juin à septembre (bulletins publiés du 3 juin au 30 septembre), mesure en octobre 2027 avec les données du SDIS 2A, confirmation avec la BDIFF lors de sa publication en 2028. |

## Situation de référence

Mesurée sur les deux saisons communes aux deux sources : 120 jours par saison (jours visés par les bulletins publiés du 3 juin au 30 septembre, donc du 4 juin au 1er octobre), soit 240 jours par département en 2024 et 2025. Sur 3 908 feux de type F en France, 2 612 tombent dans cette fenêtre, dont 139 en Corse-du-Sud et 87 en Haute-Corse. Un jour d'un département est un jour avec feu s'il compte au moins un feu.

**Part des jours avec au moins un feu, par niveau `niveau_j1` (entre crochets, intervalle à 95 %) :**

| Niveau | Corse-du-Sud (2A) | Haute-Corse (2B) | Autres départements (94) |
|---|---|---|---|
| 1 (faible) | 17,5 % [9,8 - 29,4] (10 jours sur 57) | 11,3 % [5,8 - 20,7] (8 sur 71) | 3,0 % [2,8 - 3,2] (558 sur 18 691) |
| 2 (modéré) | 40,4 % [33,2 - 48,0] (67 sur 166) | 30,6 % [24,0 - 38,2] (49 sur 160) | 22,8 % [21,4 - 24,3] (723 sur 3 172) |
| 3 (élevé) | 58,8 % [36,0 - 78,4] (10 sur 17) | 66,7 % [35,4 - 87,9] (6 sur 9) | 47,1 % [43,3 - 50,9] (314 sur 667) |
| 4 (très élevé) | aucun jour | aucun jour | 70,0 % [52,1 - 83,3] (21 sur 30) |

Contrôle sur 13 départements (04, 05, 06, 07, 11, 13, 26, 30, 34, 48, 66, 83, 84). Critère de choix : départements du pourtour méditerranéen et de son arrière-pays proche, à climat méditerranéen ou d'influence méditerranéenne. Je les ai choisis moi-même, sans source officielle ni critère forestier (type de végétation, surface boisée), et la liste n'est pas validée par le groupe ni par le SDIS : 9,6 % au niveau 1, 31,9 % au niveau 2, 53,5 % au niveau 3 (467 jours).

**Écarts du 2A, en points de pourcentage, avec l'intervalle à 95 % de la différence :**

| Niveau | avec le 2B | avec les autres départements | avec les 13 départements méditerranéens |
|---|---|---|---|
| 1 | +6,3 [-5,9 ; +19,3] | +14,6 [+6,8 ; +26,4] | +8,0 [+0,1 ; +19,9] |
| 2 | +9,7 [-0,7 ; +19,8] | +17,6 [+10,3 ; +25,3] | +8,5 [+0,9 ; +16,4] |
| 3 | -7,8 [-39,0 ; +29,0] | +11,7 [-11,4 ; +31,7] | +5,3 [-18,0 ; +25,4] |

**Méthode.** Une part est une proportion globale : tous les jours-départements d'un groupe sont comptés ensemble. La moyenne des proportions de chaque département donne d'autres valeurs pour les autres départements (3,6 % au niveau 1, 16,9 % au niveau 2, 38,6 % au niveau 3 sur 50 départements), et un écart encore plus grand avec le 2A aux niveaux 1 et 2 (13,9 et 23,5 points). Les intervalles sont ceux de Wilson pour une part et de Newcombe pour une différence. Ils supposent des jours indépendants : les jours consécutifs et les départements voisins se ressemblent, donc les vrais intervalles sont plus larges.

**Effet d'une règle empruntée au reste de la France.** Avec « niveau 2 ou plus », le dispositif se déclencherait 17,1 % des jours dans les autres départements (71,7 % des feux couverts), contre 76,2 % des jours en 2A (89,9 % des feux couverts) et 70,4 % en 2B (90,8 %).

**Une saison à la fois.** Le sens des résultats est le même en 2024 et en 2025. En 2025, le niveau 1 n'a que 8 jours en 2A (aucun avec feu), ce qui ne permet pas de conclure sur cette seule saison.

## Ce que montre l'analyse

- Le lien suit le même sens dans tous les territoires étudiés : plus le niveau monte, plus la part de jours avec feu monte.
- Le 2A a des parts nettement supérieures à celles des autres départements aux niveaux 1 et 2. Au niveau 1, il y a un feu un jour sur six en 2A contre environ un jour sur trente ailleurs. Au niveau 2, c'est 40 % contre 23 %. Les intervalles calculés indiquent un écart positif aux niveaux 1 et 2, mais cette conclusion est à interpréter avec prudence, car ils supposent l'indépendance des jours.
- Avec la Haute-Corse, la différence n'est pas distinguable de zéro. Avec les treize départements méditerranéens, elle exclut à peine zéro (de +0,1 à +19,9 points au niveau 1, de +0,9 à +16,4 au niveau 2) en supposant des jours indépendants. Comme cette supposition est optimiste, on ne peut pas conclure que le 2A en diffère ou n'en diffère pas.
- Au niveau 3 (17 jours en 2A, 9 en 2B), aucune conclusion. Le niveau 4 n'a jamais été atteint en Corse et ne se compare pas.
- Pour la décision, les résultats ne permettent pas de retenir la moyenne des autres départements comme référence directe pour le 2A sans ajustement préalable. La Haute-Corse et les départements méditerranéens semblent des références plus proches, mais deux saisons ne suffisent pas à confirmer qu'elles sont représentatives. Le SDIS 2A devrait étudier en priorité une référence régionale ou méditerranéenne, avec ses incertitudes et ses contraintes opérationnelles.

## Test de cohérence

Comment atteindre l'objectif sans faire avancer la stratégie ?

1. **Choisir la référence après coup.** Prendre comme référence les valeurs 2027 du 2A donnerait un écart nul. Le garde-fou est que les parts de référence sont figées avant le 1er juin 2027.
2. **Ne regarder que le niveau le plus favorable.** L'objectif porte sur les niveaux 1 et 2 en même temps.
3. **Changer la définition d'un feu.** Compter aussi les feux de végétation ou ne garder que les grands feux déplacerait les parts sans rien changer au dispositif. La définition est figée : feux de type "F" de la BDIFF, toutes surfaces.
4. **Effet du dispositif lui-même.** Si le dispositif renforcé empêche des feux de partir, les parts observées baissent. L'écart avec la référence augmenterait alors que le dispositif fonctionne. Ce biais ne peut pas être corrigé avec nos données : il est à signaler à la direction.
5. **Choisir une base trop proche du 2A.** Utiliser le 2A seul comme référence donne un petit écart en 2024-2025, mais sur très peu de données. L'objectif n'impose pas la base : il mesure si le choix tient.

## Limites

- **Échantillon court.** Deux saisons ne suffisent pas à établir une référence durable. Au niveau 3, 17 jours en 2A et 9 en 2B. Le niveau 4 n'a jamais été atteint en Corse et n'est pas exploitable pour la comparaison.
- **Un département n'est pas une unité comparable.** Un grand département continental a plus de surface qu'un département corse : un jour avec au moins un feu n'y a pas le même sens. Les parts comparent des jours-départements, pas des territoires de taille égale.
- **Saisie des feux.** Les départements ne saisissent pas forcément tous les petits feux de la même façon dans la BDIFF. Un écart peut venir de la saisie et pas du comportement des feux.
- **Dates des feux.** Le fuseau horaire des dates de la BDIFF n'est pas précisé dans l'export. 312 feux sur 3 908 (24 sur 204 en 2A) tombent entre 22 h et 2 h. J'ai refait le calcul en lisant ces dates en UTC puis en les convertissant à l'heure de Paris : les parts changent de moins de 1 point aux niveaux 1 et 2 pour le 2A (17,5 % et 39,8 %) et de moins de 0,3 point pour les autres départements. Le niveau 3 du 2A baisse de 58,8 % à 52,9 %, sur 17 jours seulement.
- **Choix des 13 départements méditerranéens.** Cette liste est un contrôle de mon choix, fondé sur la proximité géographique et le climat. Elle n'est pas une référence validée : le groupe et le SDIS doivent confirmer le critère et la liste, et d'autres critères (végétation, surface boisée) n'ont pas été testés.
- **Fenêtre de la Météo des forêts.** 1 296 feux sur 3 908 sont hors des jours couverts par la Météo des forêts (avant le 4 juin ou après le 1er octobre) et ne sont pas utilisés.
- **Les feux de 2026 sont exclus** (D-009) : l'année est incomplète et provisoire. La saison 2026 de la Météo des forêts n'est pas utilisée ici.
- **Pas de profil de la source.** Le dépôt n'a pas de profil pour cet export national de la BDIFF : à générer avec `src/profilage.py` avant de verser le fichier dans le pipeline.
- **La mesure dépend du SDIS.** Sans la transmission des feux de la saison 2027, l'objectif ne peut être mesuré qu'en 2028, avec la BDIFF.
- **Le seuil actuel du SDIS n'est pas connu** (décision 3 de la matrice), ni le sens de « danger élevé » (Q-1 de `docs/decisions.md`). La prévision du lendemain (J+1) est retenue provisoirement (Q-4).
- **Lien avec les autres objectifs.** Ahmed traite la Q1 (où se concentrent les feux), Arouna la Q2 (jours de déclenchement sans feu, dont les 9 jours de niveau 3 en Haute-Corse qu'on retrouve ici) et Biolohf la Q3 (seuil et budget). Le mien dit sur quelles données ces seuils peuvent s'appuyer.