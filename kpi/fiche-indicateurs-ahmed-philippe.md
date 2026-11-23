## Fiches d'indicateurs : Ahmed Philippe (Q1)

- **Séance :** UE01.B, S2 (construire un indicateur, le protéger)
- **Objectif suivi :** `kpi/objectif-ahmed-philippe.md` (ticket #73)
- **Calculs :** `python src/objectif_q1.py data/raw/bdiff_2A_2006_2025.csv` (section « Fiche d'indicateurs S2 » de la sortie), sur l'export BDIFF de la Corse-du-Sud versionné dans la couche bronze (type de feu "F", 2006-2025, 4 694 feux, D-015)

### I1 · Part des feux de l'été partis dans les communes prioritaires (KPI principal)

| Rubrique | Contenu |
|---|---|
| 1. Question et objectif | Q1 : où se concentrent les départs de feu en Corse-du-Sud ? Objectif : pour la saison 2027, faire passer de 53,2 % à 60 % (provisoire) la part des feux de l'été qui partent dans une liste de 20 communes au plus, arrêtée avant le 1er juin 2027. |
| 2. Formule | **Numérateur :** nombre de feux de forêt (type "F") en Corse-du-Sud dont la `Date de première alerte` tombe de juin à septembre et dont le `Code INSEE` est dans la liste prioritaire. **Dénominateur :** nombre de feux de forêt en Corse-du-Sud dont la `Date de première alerte` tombe de juin à septembre. **Unité :** pourcentage. |
| 3. Paramètres | **k**, le nombre de communes de la liste (20). **La fenêtre de classement**, le nombre d'années utilisées pour classer les communes (10). **La règle de classement** : nombre de feux sur les années entières, égalités départagées par code INSEE. **La saison** : juin à septembre. |
| 4. Périmètre, période, grain, fréquence | Corse-du-Sud (124 communes) ; été (juin à septembre) ; grain de la donnée : un feu, agrégé en une valeur par été pour le département ; calcul en fin de saison (octobre). Une lecture mensuelle est possible en juillet et en août seulement (voir le seuil plancher). |
| 5. Source et champs | BDIFF, export de la consultation publique (`docs/sources/fiche-bdiff.md`) : `Code INSEE`, `Date de première alerte`, `Année`. Pour 2027 : feux saisis par le SDIS 2A (à demander), confirmés par la BDIFF en 2028. |
| 6. Lignes utilisables | 4 694 sur 4 694 (100 %) : `Code INSEE` et `Date de première alerte` n'ont aucune valeur vide ni illisible (`docs/qualite/profil-bdiff.md`). Sur les étés 2024-2025 : 139 feux sur 139. Pour les données 2027 du SDIS : à vérifier à réception. |
| 7. Proxy et biais | La donnée voulue est "le feu est parti dans une zone couverte par le dispositif". Le proxy est "la commune du point de départ est dans la liste". **Biais 1 :** une grande commune (Sartène, Porto-Vecchio, Ajaccio) n'est pas couverte en entier par les patrouilles : le proxy **surestime** la couverture réelle. **Biais 2 :** un feu parti juste de l'autre côté d'une limite communale compte comme hors liste alors que le dispositif est à côté : **sous-estimation**, plus faible. **Biais 3 :** les feux évités par le dispositif n'apparaissent pas : l'indicateur **sous-estime** la qualité de la liste quand le dispositif fonctionne. |
| 8. Décision éclairée | **Valeur haute** (au-dessus de la plage habituelle de 45 % à 65 %) : la liste attrape bien les feux, la direction la garde pour l'été suivant. **Valeur basse** (sous 45 %) : les feux partent ailleurs ; la direction revoit la règle de classement (fenêtre plus courte, autre critère) ou garde une part plus grande du dispositif en réserve mobile. Une valeur dans la plage ne change rien. |
| 9. Propriétaire | Calcul : Ahmed Philippe (`src/objectif_q1.py`). Relecture : Arouna Touré (pipeline). |

**Valeur de départ :** 53,2 % (74 feux sur 139, étés 2024-2025, liste faite sur 2014-2023). Plage observée avec la même méthode, été par été de 2016 à 2025 : de 45,3 % à 65,0 %, moyenne 55,2 %.

#### Un paramètre change : ce qui bouge et ce qui ne bouge pas

| Paramètre | Valeur | Valeur de départ de I1 | Garde-fou I2 | Stabilité 2016-2025 (moyenne, minimum) |
|---|---|---|---|---|
| k | 15 | 47,5 % | 29,7 % | non calculée |
| k | **20 (retenu)** | **53,2 %** | **30,2 %** | **55,2 %, 45,3 %** |
| k | 25 | 56,8 % | 30,3 % | non calculée |
| Fenêtre | 5 ans (2019-2023) | 55,4 % | 33,3 % | 54,9 %, 42,2 % |
| Fenêtre | **10 ans (retenu)** | **53,2 %** | **30,2 %** | **55,2 %, 45,3 %** |
| Fenêtre | 18 ans (2006-2023) | 48,9 % | 29,7 % | 53,8 %, 45,3 % |

- **Passer k de 20 à 15** fait baisser la valeur de départ (47,5 %) et le coût du dispositif. La décision change : la direction couvre moins de communes et doit garder plus de moyens mobiles. Ce qui ne change pas : la formule, la source, et la part des surfaces brûlées dans la liste (environ 30 %), parce que les grands feux partent hors des communes les plus touchées dans les deux cas.
- **Passer la fenêtre de 10 à 5 ans** donne une meilleure valeur sur 2024-2025 (55,4 %), mais une moins bonne année la plus faible (42,2 % contre 45,3 %) : la liste suit mieux les années récentes, mais elle est moins sûre. La fenêtre de 10 ans est gardée ; ce choix est écrit avant de voir les résultats de 2027.

#### Avis RACER

| Critère | Avis |
|---|---|
| Relevant | Oui : il mesure directement si les moyens sont placés là où partent les feux, ce qui est la décision de la Q1. |
| Accepted | À confirmer avec le SDIS 2A : la commune comme unité de zone, la définition d'un feu (type "F", toutes surfaces) et le nombre de communes que le budget permet. |
| Credible | Oui si k, la fenêtre et la définition d'un feu sont fixés dans cette fiche avant la saison. Reste une ambiguïté : une valeur basse peut venir d'une mauvaise liste ou d'un dispositif qui a évité des feux (biais 3). |
| Easy | Oui : trois champs renseignés à 100 %, calcul automatique par `src/objectif_q1.py`. La seule difficulté est d'obtenir les feux de 2027 auprès du SDIS 2A. |
| Robust | Non seul : il monte si on allonge la liste, et il ignore les grands feux. D'où les garde-fous ci-dessous. |

### Effets pervers et garde-fous (K4)

**Détournement 1 : allonger la liste.** Par qui : celui qui présente le bilan, de bonne foi, pour "mieux couvrir". Comment : passer de 20 à 30 communes. Effet : I1 monte de 53,2 % à 62,6 % sans que le classement soit meilleur, et le dispositif est dilué. **Garde-fou :** règle fixée à l'avance (k = 20, écrit dans cette fiche et dans l'objectif), et le nombre de communes de la liste est toujours affiché à côté de I1.

**Détournement 2 : viser les communes à beaucoup de petits feux.** Par qui : la règle de classement elle-même, sans mauvaise intention. Comment : le classement par nombre de feux favorise les communes où partent beaucoup de petits feux vite éteints (Ajaccio : 327 feux pour 305 ha sur 2006-2025), au détriment de celles où partent les grands feux (Fozzano : 22 feux pour 3 227 ha). Effet : I1 est bon pendant que les hectares brûlent ailleurs. **Garde-fou : I2, la part de la surface brûlée dans la liste** (indicateur contrepoids, il mesure des hectares et non un nombre de feux).

**Risque résiduel.** Ce que les garde-fous ne voient pas : les feux évités par le dispositif (un été calme dans les communes de la liste peut être un succès ou un hasard), les feux non enregistrés, et un grand feu qui traverse plusieurs communes, rattaché seulement à sa commune de départ.

### I2 · Part de la surface brûlée de l'été dans les communes prioritaires (garde-fou de I1)

| Rubrique | Contenu |
|---|---|
| Formule | **Numérateur :** somme de `Surface parcourue (m2)` des feux de l'été (juin à septembre) dont le `Code INSEE` est dans la liste. **Dénominateur :** somme de `Surface parcourue (m2)` de tous les feux de l'été en Corse-du-Sud. **Unité :** pourcentage, affiché avec la surface totale de l'été en hectares. |
| Paramètres | Les mêmes que I1 (même liste, même saison). |
| Source et lignes utilisables | BDIFF, champ `Surface parcourue (m2)` : 4 694 lignes sur 4 694, aucune vide, nulle ou négative (`docs/qualite/profil-bdiff.md`). |
| Valeur de départ | 30,2 % (91 ha sur 302, étés 2024-2025) ; 81,1 % à l'été 2024 (69 ha sur 85), 10,3 % à l'été 2025 (22 ha sur 217). |
| Seuil plancher | I2 n'est pas lu si la surface totale de l'été est inférieure à 20 ha (été 2018 : 4,8 ha). Un seul feu y ferait passer la part de 0 à 100 %. |
| Décision éclairée | Si I1 est bon mais I2 bas, les grands feux partent hors de la liste : la direction garde une réserve mobile et regarde les communes à grands feux (Fozzano, Quenza, Sari-Solenzara), même si elles ont peu de départs. |
| Biais | Très instable : un seul grand feu fait la valeur (Sari-Solenzara, 182 ha le 23 juin 2025). Sur 2016-2025, avec la même méthode, I2 varie de 10,3 % (2025) à 90,8 % (2021). Il se lit toujours avec la surface totale et le plus grand feu de l'été. |
| Propriétaire | Ahmed Philippe, relu par Arouna Touré. |

### Pre-mortem

On imagine qu'à l'automne 2027, la direction a pris une mauvaise décision à cause de I1.

| Rang | Raison de l'échec | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | Un grand feu part hors de la liste pendant que I1 est bon ; la direction croit sa liste efficace et retire la réserve mobile. | Haute : I2 est sous 15 % deux étés sur dix (2022 et 2025). | Haute : ce sont les grands feux qui font les dégâts. | I2 affiché à côté de I1 avec la surface totale et le plus grand feu de l'été ; règle écrite : une part du dispositif reste mobile tant que I2 n'est pas au-dessus de 50 % deux étés de suite. |
| 2 | Une seule saison est lue comme une preuve : un été à 60 % est pris pour une réussite, un été à 46 % pour un échec, alors que la plage normale va de 45 % à 65 %. | Haute : environ 70 feux par été, un feu pèse 1,5 point. | Moyenne : la liste est changée sans raison, ou gardée à tort. | I1 est toujours présenté avec la plage 2016-2025 et le nombre de feux de l'été ; seuil plancher : pas de lecture mensuelle sous 20 feux (seuls juillet et août l'atteignent en 2024-2025). |
| 3 | Les feux 2027 transmis par le SDIS 2A sont incomplets ou mal rattachés à leur commune. | Moyenne. | Moyenne : la mesure d'octobre 2027 est fausse, mais elle sera corrigée en 2028 avec la BDIFF. | Contrôle par échantillon : quelques feux relus avec le SDIS, puis comparaison avec la BDIFF en 2028. |

### Rôle de chaque indicateur (ma part du jeu)

| Rôle | Indicateur | Raison |
|---|---|---|
| KPI principal | I1, part des feux de l'été dans les communes prioritaires | Il répond à la décision de la Q1 : la liste attrape-t-elle les feux ? |
| KPI secondaire | Nombre de communes qui font la moitié des feux de l'été (10 en 2024, 11 en 2025, 12 sur 2006-2025) | Il dit si les feux restent concentrés. S'il monte nettement, une liste de 20 communes ne suffit plus et la direction élargit la couverture ou garde plus de moyens mobiles. |
| Garde-fou | I2, part de la surface brûlée de l'été dans les communes prioritaires | Il se dégrade quand I1 est atteint en ignorant les grands feux, et il mesure des hectares, pas un nombre de feux. |
| Contexte | Nombre total de feux de l'été (76 en 2024, 63 en 2025) et surface totale brûlée | Il dit si l'été a été calme ou sévère. On le note, on ne le pilote pas : le SDIS ne choisit pas le nombre de feux. |
| Écarté | Nombre de feux dans la liste (en valeur, pas en part) | Il monte et descend avec la sévérité de l'été, pas avec la qualité de la liste. Test : s'il double parce que l'été est sec, personne ne fait rien de différent. |
| Écarté | Classement des communes par surface brûlée totale depuis 2006 | Trois communes font la moitié des hectares sur 20 ans, à cause de deux ou trois très grands feux anciens : le classement ne prévoit pas où partira le prochain grand feu, il ne change donc pas la liste. |
