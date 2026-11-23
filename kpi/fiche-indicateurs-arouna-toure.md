## Fiches d'indicateurs : Arouna Touré (Q2)

- **Séance :** UE01.B, S2 (construire un indicateur, le protéger)
- **Objectif suivi :** `kpi/objectif-arouna-toure.md` (ticket #70)
- **Calculs :** `python src/pipeline.py` puis `python src/indicateurs_q2.py`, qui écrit tous les chiffres de cette fiche dans `docs/qualite/indicateurs-q2.md`. Ils sont lus dans la couche or de l'entrepôt (Météo des forêts et BDIFF de la couche bronze, D-015) et sont identiques à ceux de `src/calcul_diagnostic.py` (`docs/qualite/calculs-diagnostic.md`), calculés directement sur les fichiers bruts.
- **Période de mesure :** jours visés par la Météo des forêts du 4 juin au 1er octobre 2024 et 2025 (240 jours) ; les feux de 2026 ne sont pas utilisés (D-009).

### I1 · Part des jours de déclenchement sans aucun départ de feu (KPI principal)

| Rubrique | Contenu |
|---|---|
| 1. Question et objectif | Q2 : à chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu en Corse-du-Sud ? Objectif : pour la saison 2027, faire passer de 41,2 % à 33 % (provisoire, à valider avec le SDIS 2A) la part des jours de déclenchement du dispositif renforcé sans aucun départ de feu, sans que la part des feux partis hors des jours de déclenchement dépasse 90,6 % (I2). |
| 2. Formule | **Numérateur :** nombre de jours de la saison où la règle de déclenchement est vraie et où aucun feu de forêt (type "F") de Corse-du-Sud n'a sa `Date de première alerte` ce jour-là. **Dénominateur :** nombre de jours de la saison où la règle de déclenchement est vraie. **Unité :** pourcentage, toujours affiché avec « x jours sur n ». |
| 3. Paramètres | **Le seuil** : niveau 3 (`niveau_j1` supérieur ou égal à 3). **L'horizon de la prévision** : J+1 (`niveau_j1`, bulletin publié la veille ; question Q-4 encore ouverte). **La saison** : jours visés de juin à septembre. **La définition d'un feu** : feu de forêt de la BDIFF, type "F", toutes surfaces. **Le rattachement** : un feu compte pour le jour de sa date de première alerte, à l'heure de Paris. |
| 4. Périmètre, période, grain, fréquence | Corse-du-Sud ; saison des feux ; grain : un jour visé pour le département ; une valeur par saison, calculée en fin de saison (octobre). Pas de lecture mensuelle : il y a trop peu de jours de déclenchement (voir le seuil plancher). |
| 5. Source et champs | Météo des forêts (Météo-France, data.gouv.fr, Licence Ouverte 2.0) : `date`, `num_dep`, `niveau_j1`. BDIFF : `Date de première alerte`, `Département`. Dans l'entrepôt : `gold.fait_danger_jour` et `gold.fait_feu`, reliés par le jour et le département. Pour 2027 : bulletins de la Météo des forêts de la saison et feux saisis par le SDIS 2A (à demander), confirmés par la BDIFF en 2028. |
| 6. Lignes utilisables | Météo des forêts : 240 jours visés sur 240 en Corse-du-Sud, `niveau_j1` toujours entre 1 et 4 (contrôle du pipeline). BDIFF : `Date de première alerte` renseignée pour les 4 694 feux (`docs/qualite/profil-bdiff.md`). Les 139 feux de juin à septembre 2024 et 2025 sont tous rattachés à un jour visé : aucun feu perdu. Pour les données 2027 du SDIS : à vérifier à réception. |
| 7. Proxy et biais | La donnée voulue est « jour où le dispositif renforcé a été déclenché et n'a servi à rien ». **Proxy 1 :** « jour où `niveau_j1` est supérieur ou égal à 3 » remplace « jour de déclenchement », car le seuil appliqué par le SDIS 2A n'est pas connu. **Biais 1 :** si le SDIS déclenche aussi selon le vent ou son jugement, I1 mesure une règle théorique, pas le dispositif réel ; le sens de l'erreur est inconnu. **Proxy 2 :** « aucun feu de forêt enregistré ce jour » remplace « le dispositif n'a servi à rien ». **Biais 2 :** les feux évités par le dispositif n'apparaissent pas : un jour réussi ressemble à une fausse alerte, et I1 **surestime** les fausses alertes quand le dispositif fonctionne. **Biais 3 :** les départs qui ne sont pas des feux de forêt (type "F") ne sont pas comptés, alors que le dispositif les traite : I1 **surestime** encore les jours inutiles. **Biais 4 :** un feu parti le soir et signalé après minuit compte pour le lendemain : erreur faible, dans les deux sens. |
| 8. Décision éclairée | **Valeur haute** (au-dessus de 50 %, plus d'un jour de déclenchement sur deux sans feu, comme à l'été 2025) : l'indice seul déclenche trop ; la direction ajoute un critère au déclenchement (vent ou sécheresse, à préciser avec le SDIS) avant de toucher au seuil, et vérifie I2. **Valeur à la cible ou en dessous** (33 % ou moins) avec I2 sous 90,6 % : le seuil est bien placé, la direction le garde. **Entre les deux** : le seuil est gardé et la mesure continue sur une saison de plus. Toute lecture se fait avec le nombre de jours (seuil plancher). |
| 9. Propriétaire | Calcul : Arouna Touré (`src/indicateurs_q2.py`). Relecture : Saran Diabagate. |

**Valeur de départ :** 41,2 % (7 jours sans feu sur 17 jours de déclenchement, étés 2024 et 2025). Saison par saison : 0,0 % à l'été 2024 (0 sur 3) et 50,0 % à l'été 2025 (7 sur 14). Les archives de la Météo des forêts commencent en 2024 : il n'existe pas de plage sur dix ans comme pour la Q1. Repère voisin : 33,3 % en Haute-Corse avec la même règle (3 jours sur 9), qui sert de cible provisoire.

**Seuil plancher :** I1 n'est pas lu pour une saison qui compte moins de 10 jours de déclenchement ; il est alors cumulé avec la saison précédente. Sur 17 jours, un jour pèse 5,9 points (35,3 % ou 47,1 % avec un jour sans feu de moins ou de plus) ; sur 3 jours, comme à l'été 2024, il pèse 33,3 points.

#### Un paramètre change : ce qui bouge et ce qui ne bouge pas

| Paramètre | Valeur | Jours de déclenchement | I1 | Garde-fou I2 |
|---|---|---|---|---|
| Seuil | niveau 2 | 183 | 57,9 % | 10,1 % |
| Seuil | **niveau 3 (retenu)** | **17** | **41,2 %** | **90,6 %** |
| Horizon | J+2 (`niveau_j2` supérieur ou égal à 3) | 1 | 0,0 % | 98,6 % |
| Horizon | J+1 et J+2 à la fois | 1 | 0,0 % | 98,6 % |
| Département | Haute-Corse, niveau 3 | 9 | 33,3 % | 90,8 % |

- **Passer le seuil de 3 à 2** fait monter I1 à 57,9 % et descendre I2 à 10,1 % : le dispositif couvrirait presque tous les feux, mais il serait déclenché 183 jours sur 240. La décision change de nature : c'est un dispositif presque permanent, dont le coût est à comparer avec le budget. Ce qui ne change pas : la formule, la source, et le fait que l'indice seul ne distingue pas bien les jours à feu (au niveau 2, 40,4 % des jours ont un feu ; au niveau 3, 58,8 %).
- **Passer l'horizon de J+1 à J+2** ne laisse qu'un jour de déclenchement en deux étés : I1 vaut 0 %, mais sur un seul jour, et 98,6 % des feux partent hors déclenchement. La prévision à deux jours annonce trop rarement le niveau 3 pour servir de règle. L'horizon J+1 est gardé ; ce choix est écrit avant de voir les résultats de 2027.

#### Avis RACER

| Critère | Avis |
|---|---|
| Relevant | Oui : il mesure directement les fausses alertes du seuil, ce qui est la décision de la Q2. |
| Accepted | À confirmer avec le SDIS 2A : le seuil réellement appliqué, ce qu'est un jour de déclenchement, et le coût d'un jour de dispositif renforcé. |
| Credible | Fragile : 17 jours de déclenchement sur deux étés, un jour pèse 5,9 points. Reste une ambiguïté : une valeur haute peut venir d'un mauvais seuil ou d'un dispositif qui a évité des feux (biais 2). |
| Easy | Oui : deux sources ouvertes, champs renseignés à 100 %, calcul automatique par `src/indicateurs_q2.py`. La seule difficulté est d'obtenir les feux de 2027 auprès du SDIS 2A. |
| Robust | Non seul : il s'améliore si l'on déclenche moins souvent, au prix de feux non couverts. D'où le garde-fou I2. |

### Effets pervers et garde-fous (K4)

**Détournement 1 : relever le seuil.** Par qui : la direction, de bonne foi, pour « réduire les fausses alertes ». Comment : déclencher seulement au niveau 4, ou ne pas déclencher certains jours de niveau 3. Effet : au niveau 4, aucun jour n'aurait été déclenché en 2024 et 2025 ; il n'y a plus de fausse alerte, mais 100 % des feux partent hors déclenchement. **Garde-fou :** I2, qui ne doit pas dépasser 90,6 %, et le nombre de jours de déclenchement toujours affiché à côté de I1 (KPI secondaire).

**Détournement 2 : élargir la définition d'un feu.** Par qui : celui qui prépare le bilan, sans mauvaise intention, en reprenant tous les départs saisis par le SDIS. Comment : compter aussi les feux de végétation ou d'un autre type que "F". Effet : plus de jours « avec feu », donc I1 baisse sans que rien ne change dans le dispositif. **Garde-fou :** la définition est figée dans cette fiche (feux de forêt de type "F", toutes surfaces) ; le pipeline contrôle que chaque export BDIFF ne contient que des feux de type "F" et s'arrête sinon.

**Risque résiduel.** Ce que les garde-fous ne voient pas : les feux évités par le dispositif (biais 2), l'écart entre la règle théorique et le déclenchement réel du SDIS (biais 1), et le petit nombre de jours.

### I2 · Part des feux partis hors des jours de déclenchement (garde-fou de I1)

| Rubrique | Contenu |
|---|---|
| Formule | **Numérateur :** nombre de feux de forêt de la saison en Corse-du-Sud dont la `Date de première alerte` tombe un jour où la règle de déclenchement est fausse. **Dénominateur :** nombre de feux de forêt de la saison en Corse-du-Sud. **Unité :** pourcentage, affiché avec le nombre de feux et de jours de déclenchement. |
| Paramètres | Les mêmes que I1 (seuil, horizon, saison, définition d'un feu, rattachement). |
| Source et lignes utilisables | Mêmes sources que I1 ; 139 feux sur 139 rattachés à un jour visé. |
| Valeur de départ | 90,6 % (126 feux sur 139, étés 2024 et 2025) ; 94,7 % à l'été 2024 (72 sur 76) et 85,7 % à l'été 2025 (54 sur 63). |
| Limite | Ne doit pas dépasser 90,6 %, sa valeur avec le seuil au niveau 3 : au-delà, la baisse de I1 vient de déclenchements en moins, pas d'un meilleur seuil. |
| Décision éclairée | Si I1 baisse mais que I2 dépasse 90,6 %, la direction revient à la règle précédente : la cible est atteinte en couvrant moins de feux. |
| Biais | I2 monte tout seul quand l'été compte peu de jours de danger élevé : 94,7 % à l'été 2024, avec 3 jours de déclenchement seulement. C'est la météo, pas un choix de la direction : I2 se lit toujours avec le nombre de jours de déclenchement de la saison. |
| Propriétaire | Arouna Touré, relu par Saran Diabagate. |

### Pre-mortem

On imagine qu'à l'automne 2027, la direction a pris une mauvaise décision à cause de I1.

| Rang | Raison de l'échec | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | L'été 2027 compte très peu de jours de déclenchement, et I1 est lu sur ces seuls jours : un été comme 2024 (0 jour sans feu sur 3) fait croire à un seuil parfait, un seul jour sans feu le ferait passer à 33,3 %. La direction fige ou change le seuil sur un hasard. | Haute : 3 jours de déclenchement en 2024, 14 en 2025, 18 en 2026. | Haute : le seuil est la décision elle-même. | Seuil plancher : pas de lecture de I1 sous 10 jours de déclenchement dans la saison, cumul avec la saison précédente ; I1 toujours affiché en « x jours sur n ». |
| 2 | La cible est atteinte en déclenchant moins : le dispositif n'est pas lancé certains jours de niveau 3, les fausses alertes baissent, et les feux de ces jours-là partent sans dispositif renforcé. | Moyenne : c'est la façon la plus simple d'atteindre la cible. | Haute : des feux partent sans moyens renforcés. | I2 affiché à côté de I1, avec sa limite de 90,6 %, et le nombre de jours de déclenchement de la saison (KPI secondaire). |
| 3 | Le dispositif évite des feux : les jours réussis ressemblent à des fausses alertes, I1 monte, et la direction allège un dispositif qui fonctionne. | Inconnue : nos données ne permettent pas de la mesurer. | Haute. | Pas de garde-fou chiffré possible ; le biais est expliqué à la direction, et les interventions du SDIS les jours de déclenchement sont à demander pour le vérifier. |

### Rôle de chaque indicateur (ma part du jeu)

| Rôle | Indicateur | Raison |
|---|---|---|
| KPI principal | I1, part des jours de déclenchement sans aucun départ de feu | Il répond à la décision de la Q2 : le seuil déclenche-t-il les bons jours ? |
| KPI secondaire | Nombre de jours de déclenchement par saison (3 en 2024, 14 en 2025, 18 en 2026) | Il donne le coût du dispositif et le poids d'un jour dans I1. S'il monte nettement, la direction vérifie que le budget suit ou revoit la règle. |
| Garde-fou | I2, part des feux partis hors des jours de déclenchement | Il se dégrade quand I1 est atteint en déclenchant moins, et il compte des feux, pas des jours. |
| Contexte | Nombre de feux de l'été (76 en 2024, 63 en 2025) et nombre de jours avec au moins un feu (42 et 45) | Ils disent si l'été a été calme ou sévère. On les note, on ne les pilote pas : le SDIS ne choisit pas le nombre de feux. |
| Contexte | I1 en Haute-Corse (33,3 %, 3 jours sur 9) | Repère voisin avec le même indice et la même règle ; il fonde la cible provisoire. |
| Écarté | Part des feux partis les jours de danger faible (niveau 1 : 14 sur 139, soit 10,1 %) | Elle ne dépend pas du seuil choisi, et elle monte si le dispositif fonctionne, puisque les feux évités les jours de déclenchement font monter la part des autres jours. |
| Écarté | Part des jours avec feu au niveau 3 (58,8 %) | C'est le complément de I1 (100 % moins 41,2 %) : il n'apporte aucune information de plus. |
| Écarté | Règle à deux jours (`niveau_j2`) | Un seul jour de déclenchement en deux étés : on ne peut pas la mesurer. |
