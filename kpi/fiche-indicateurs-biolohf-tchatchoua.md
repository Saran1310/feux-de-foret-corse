## Fiches d'indicateurs : Biolohf Tchatchoua (Q3)

- **Séance :** UE01.B, S2 (construire un indicateur, le protéger)
- **Objectif suivi :** `kpi/objectif-biolohf-tchatchoua.md` (ticket #72)
- **Calculs :** `python src/calcul_diagnostic.py` (résultats dans `docs/qualite/calculs-diagnostic.md`), sur la Météo des forêts (`niveau_j1`) croisée avec l'export BDIFF de la Corse-du-Sud (type de feu "F"), du 4 juin au 1er octobre 2024 et 2025 : 240 jours, 139 feux. Chaque chiffre de cette fiche se trouve dans ce fichier de résultats : tableaux par niveau et par règle, « Detail par saison », « Jours declenches par ete » (moyennes par été) et « Feux hors de juin a septembre » (46,5 %).

### I1 · Part des feux de l'été partis un jour déclenché (KPI principal)

| Rubrique | Contenu |
|---|---|
| 1. Question et objectif | Q3 : combien de jours par été chaque seuil aurait-il déclenché, et quelle part des feux ces jours auraient-ils couverte ? Objectif : d'ici la fin de l'été 2027, retenir un seuil de `niveau_j1` qui couvre au moins [80 %] des feux du 2A de juin à septembre, sans déclencher plus de [92] jours par été (valeurs provisoires, à fixer avec le SDIS 2A). |
| 2. Formule | **Numérateur :** nombre de feux de forêt (type "F") en Corse-du-Sud dont la `Date de première alerte` tombe un jour déclenché. **Dénominateur :** nombre de feux de forêt (type "F") en Corse-du-Sud de juin à septembre. **Unité :** pourcentage. Un jour est déclenché si `niveau_j1`, rapporté au lendemain de sa publication, est supérieur ou égal au seuil. |
| 3. Paramètres | **Le seuil** : niveau 2 ou niveau 3 (le niveau 4 n'a jamais été atteint). **Le décalage** : `niveau_j1` publié le jour J décrit le jour J+1. **La saison** : juin à septembre (fenêtre de la Météo des forêts : 4 juin au 1er octobre). **La définition d'un feu**, règle fixée à l'avance dans cette fiche : un feu de forêt est une ligne de l'export BDIFF de type de feu "F" (filtre appliqué à l'export), toutes surfaces, rattaché au jour de sa `Date de première alerte`. Le glossaire (entrée « Feu de forêt ») la dit encore « à harmoniser » (question Q-3 de `docs/decisions.md`) : tant qu'elle ne l'est pas, c'est cette règle qui fait foi pour I1 et I2. |
| 4. Périmètre, période, grain, fréquence | Corse-du-Sud (2A) ; saison de juin à septembre ; grain de la donnée : un jour × un département, un feu rattaché à sa date de première alerte ; une valeur par été ; calcul en octobre, quand la saison est terminée. |
| 5. Source et champs | Météo des forêts (`docs/sources/fiche-meteo-des-forets.md`) : date de publication, département, `niveau_j1`. BDIFF (`docs/sources/fiche-bdiff.md`) : `Date de première alerte`, `Département`. Pour 2027 : feux saisis par le SDIS 2A (à demander), confirmés par la BDIFF en 2028. |
| 6. Lignes utilisables | `niveau_j1` : 240 jours sur 240 de la fenêtre ont un niveau (57 au niveau 1, 166 au niveau 2, 17 au niveau 3, 0 au niveau 4). `Date de première alerte` : 4 694 lignes sur 4 694 renseignées et lisibles (`docs/qualite/profil-bdiff.md`) ; 139 feux tombent dans la fenêtre des deux saisons. Pour les feux 2027 du SDIS : à vérifier à réception. |
| 7. Proxy et biais | La donnée voulue est "le feu est parti un jour où le dispositif renforcé était en place". Le proxy est "le feu est parti un jour où l'indice atteint le seuil". **Biais 1 :** le grain est le département : un jour déclenché ne dit pas où le dispositif est placé, le proxy **surestime** la couverture réelle. **Biais 2 :** la date de première alerte est celle de l'alerte, pas celle du départ, et un feu parti tard dans la soirée peut tomber sur le jour suivant. **Biais 3 :** si le dispositif empêche des feux de partir, la couverture mesurée baisse alors que le dispositif fonctionne ; ce biais ne peut pas être corrigé avec nos données. **Biais 4 :** 46,5 % des feux du 2A partent hors de juin à septembre, où la Météo des forêts n'est pas publiée : l'indicateur ne les voit pas. |
| 8. Décision éclairée | **Couverture au-dessus de la cible et jours sous le plafond :** la direction garde le seuil pour l'été suivant. **Couverture sous la cible :** le seuil est trop haut ; la direction l'abaisse ou ajoute un critère de déclenchement. **Jours au-dessus du plafond (voir I2) avec une bonne couverture :** le seuil seul ne suffit pas ; la direction relève le plafond ou ajoute un critère en plus de l'indice, à fixer avec le SDIS 2A. |
| 9. Propriétaire | Calcul : Biolohf Tchatchoua (`src/calcul_diagnostic.py`). Relecture : Arouna Touré (pipeline). |

**Valeur de départ :** au niveau 2 ou plus, **89,9 %** (125 feux sur 139, étés 2024-2025) ; au niveau 3 ou plus, **9,4 %** (13 feux sur 139). Par été au niveau 2 ou plus : 81,6 % en 2024 (62 feux sur 76), 100 % en 2025 (63 sur 63). Il n'existe pas de seuil intermédiaire : toute cible entre 9,4 % et 89,9 % impose le niveau 2.

#### Un paramètre change : ce qui bouge et ce qui ne bouge pas

| Paramètre | Valeur | Valeur de départ de I1 | Jours déclenchés par été (I2) | Couverture par été (2024, 2025) |
|---|---|---|---|---|
| Seuil | niveau 1 ou plus | 100 % | 120 (tous les jours) | 100 %, 100 % |
| Seuil | **niveau 2 ou plus (retenu pour la lecture)** | **89,9 %** | **91,5 (71, 112)** | **81,6 %, 100 %** |
| Seuil | niveau 3 ou plus | 9,4 % | 8,5 (3, 14) | 5,3 %, 14,3 % |
| Seuil | niveau 4 | 0 % | 0 | 0 %, 0 % |

- **Passer du niveau 2 au niveau 3** fait tomber la couverture de 89,9 % à 9,4 % et les jours de 91,5 à 8,5 par été. La décision change : le dispositif tient dans n'importe quel budget, mais il rate neuf feux sur dix. Ce qui ne change pas : la formule, la source et la saison.
- **Un jour de plus ou de moins au niveau 3** change beaucoup les pourcentages : il n'y a que 17 jours à ce niveau en deux saisons.

#### Avis RACER

| Critère | Avis |
|---|---|
| Relevant | Oui : il mesure si le seuil retenu attrape les feux, ce qui est la décision de la Q3. |
| Accepted | À confirmer avec le SDIS 2A : la définition d'un feu (type "F", toutes surfaces), la cible de couverture et le seuil actuellement appliqué, qui est inconnu. |
| Credible | Oui si le seuil, le décalage J+1 et la définition d'un feu sont fixés dans cette fiche avant la saison. Reste une ambiguïté : une couverture basse peut venir d'un mauvais seuil ou d'un dispositif qui a évité des feux (biais 3). |
| Easy | Oui : deux champs renseignés à 100 %, calcul automatique par `src/calcul_diagnostic.py`. La seule difficulté est d'obtenir les feux de 2027 auprès du SDIS 2A. |
| Robust | Non seul : il monte à 100 % si on déclenche tous les jours. D'où le garde-fou I2 ci-dessous. |

### Effets pervers et garde-fous

**Détournement 1 : déclencher tous les jours.** Par qui : celui qui présente le bilan, de bonne foi, pour "ne rien rater". Comment : abaisser le seuil au niveau 1. Effet : I1 passe à 100 % sans que le choix du seuil soit meilleur, et le dispositif est dilué sur tout l'été. **Garde-fou :** I2, le nombre de jours déclenchés par été, affiché à côté de I1 avec son plafond.

**Détournement 2 : relever le seuil au niveau 4.** Par qui : celui qui présente le bilan, pour tenir le plafond de jours. Comment : relever le seuil au niveau 4. Effet : I2 tombe à 0 jour et le plafond est respecté, mais I1 tombe à 0 % : plus aucun feu n'est couvert. **Garde-fou :** I1 et I2 sont deux indicateurs opposés qui se surveillent l'un l'autre. Gagner sur I2 en déclenchant moins fait perdre sur I1, et gagner sur I1 en déclenchant plus fait perdre sur I2. Aucun des deux ne se lit seul : ils sont affichés ensemble, avec leur cible.

**Détournement 3 : élargir la définition d'un feu** (compter aussi les très petits feux ou les feux de végétation) pour gonfler la couverture. **Garde-fou :** la définition est écrite dans cette fiche comme règle fixée à l'avance (type "F" de la BDIFF, toutes surfaces, voir les paramètres de I1) et ne change pas pour atteindre la cible. Tout changement passe par le journal des décisions.

**Risque résiduel.** Ce que les garde-fous ne voient pas : les feux évités par le dispositif, les feux non enregistrés, et l'endroit où le dispositif est placé (le grain est le département).

### I2 · Nombre de jours déclenchés par été (garde-fou de I1)

| Rubrique | Contenu |
|---|---|
| Formule | **Nombre de jours de juin à septembre où `niveau_j1`, rapporté au lendemain de sa publication, atteint le seuil.** **Unité :** jours par été, affiché avec la part des jours de la saison. |
| Paramètres | Les mêmes que I1 (même seuil, même saison, même décalage). |
| Source et lignes utilisables | Météo des forêts, champ `niveau_j1` : 240 jours sur 240 renseignés (`docs/qualite/profil-mdf.md`). |
| Valeur de départ | Au niveau 2 ou plus : 91,5 jours par été en moyenne (71 en 2024, 112 en 2025, 76,25 % des jours) ; en 2026, 128 jours au niveau 2 ou plus et 18 jours au niveau 3 ou plus (indice seul : saison 2026 de la Météo des forêts, `data/raw/mdf_2026.csv.gz` ; les feux de 2026 sont exclus, D-009 ; lignes « 2026 » de `docs/qualite/calculs-diagnostic.md`). Plafond provisoire : [92] jours par été, à fixer avec le SDIS 2A. |
| Seuil plancher | I2 n'est lu qu'avec la saison complète (fin septembre). Une lecture en cours d'été donne un nombre de jours trop faible. |
| Décision éclairée | Si I1 est bon mais I2 dépasse le plafond, le seuil seul ne tient pas dans le budget : la direction ajoute un critère de déclenchement en plus de l'indice ou relève le plafond. Si I2 est sous le plafond mais I1 est bas, le seuil est trop haut. |
| Biais | Il dépend du climat de l'été : 71, 112 et 128 jours au niveau 2 ou plus en 2024, 2025 et 2026. Un plafond fixé sur la moyenne est dépassé les étés chauds, sans que le seuil soit mauvais. Il se lit avec le nombre de jours de l'été. |
| Propriétaire | Biolohf Tchatchoua, relu par Arouna Touré. |

### Pre-mortem

On imagine qu'à l'automne 2027, la direction a pris une mauvaise décision à cause de I1.

| Rang | Raison de l'échec | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | I1 est excellent (100 % en 2025) et la direction retient le niveau 2 sans voir que I2 a dépassé le plafond : le dispositif est déclenché 112 jours, le budget ne suit pas. | Haute : le plafond provisoire de 92 jours est dépassé deux étés sur trois. | Haute : un dispositif impayable est abandonné en cours d'été. | I2 affiché à côté de I1 avec le plafond ; règle écrite : un seuil n'est retenu que si I1 et I2 sont tenus ensemble, ou si un critère supplémentaire est ajouté. |
| 2 | Une seule saison est lue comme une preuve : 100 % en 2025 est pris pour une réussite, 81,6 % en 2024 pour un échec, alors que deux saisons ne permettent pas de trancher. | Haute : 17 jours seulement au niveau 3, 63 à 76 feux par été. | Moyenne : le seuil est changé sans raison, ou gardé à tort. | I1 est toujours présenté avec les deux saisons, le nombre de feux de l'été et la plage observée ; aucune décision sur une saison isolée. |
| 3 | Les feux 2027 transmis par le SDIS 2A sont incomplets ou datés à la mauvaise journée : la couverture mesurée en octobre 2027 est fausse. | Moyenne. | Moyenne : l'erreur sera corrigée en 2028 avec la BDIFF, après la décision. | Contrôle par échantillon : quelques feux relus avec le SDIS, puis comparaison avec la BDIFF en 2028. |

### Rôle de chaque indicateur (ma part du jeu)

| Rôle | Indicateur | Raison |
|---|---|---|
| KPI principal | I1, part des feux de l'été partis un jour déclenché | Il répond à la décision de la Q3 : le seuil attrape-t-il les feux ? |
| Garde-fou | I2, nombre de jours déclenchés par été | Il se dégrade quand I1 est atteint en déclenchant tous les jours, et il mesure le coût du dispositif en jours. |
| KPI secondaire | Part des jours déclenchés sans aucun feu (57,9 % au niveau 2 ou plus : 106 jours sur 183) | Il dit combien de jours déclenchés ne servent à rien ; il rejoint l'indicateur de la Q2 d'Arouna. |
| Contexte | Nombre total de feux de l'été (76 en 2024, 63 en 2025) et nombre de jours au niveau 2 ou plus des saisons passées | Il dit si l'été a été calme ou sévère. On le note, on ne le pilote pas : le SDIS ne choisit pas le nombre de feux. |
| Écarté | Nombre de feux couverts (en valeur, pas en part) | Il monte et descend avec la sévérité de l'été, pas avec la qualité du seuil. Test : s'il double parce que l'été est sec, personne ne fait rien de différent. |
| Écarté | Part des jours au niveau 3 ou plus | Elle dépend du climat de l'été (3 jours en 2024, 14 en 2025, 18 en 2026 : indice seul, sans feux de 2026) et le SDIS ne la choisit pas ; elle ne change pas la décision. |
