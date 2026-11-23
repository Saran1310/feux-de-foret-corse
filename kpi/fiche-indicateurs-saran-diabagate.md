## Fiches d'indicateurs : Saran Diabagate (Q4)

- **Séance :** UE01.B, S2 (construire un indicateur, le protéger)
- **Objectif suivi :** `kpi/objectif-saran-diabagate.md` (ticket #71)
- **Calculs :** `python src/analyse_comparaison.py bdiff_france.csv data/raw/mdf_2024.csv.gz data/raw/mdf_2025.csv.gz` (section « Fiche d'indicateurs S2 » de la sortie). Les fichiers de la Météo des forêts sont dans la couche bronze (D-015). L'export BDIFF « France entière » (type de feu "F", du 2024-01-01 au 2025-12-31, 3 908 feux) sert à tous les calculs de cette fiche, mais il n'est pas encore versionné dans la couche bronze : il reste en fichier local (`bdiff_france.csv`). Son ajout à `data/raw/` passera par une pull request à part, avec une décision à écrire dans le journal (D-016, pas encore rédigée).

### I1 · Écart entre la part de jours avec feu du 2A et celle de la base de référence (KPI principal)

| Rubrique | Contenu |
|---|---|
| 1. Question et objectif | Q4 : à chaque niveau de la Météo des forêts, la part des jours avec au moins un feu est-elle comparable en Corse-du-Sud et ailleurs ? Objectif (provisoire, [y points] reste à fixer avec le SDIS 2A) : avant le 1er juin 2027, choisir la base de référence et figer ses parts aux niveaux 1 et 2 ; en octobre 2027, vérifier que l'écart observé en 2A reste d'au plus [y points] à chacun des deux niveaux. La tolérance, la référence et la règle de la rubrique 8 sont à fixer avec le SDIS 2A, pas seule. |
| 2. Formule | **Part (groupe G, niveau n)** = nombre de jours-départements du groupe G au niveau n avec au moins un feu, divisé par le nombre de jours-départements du groupe G au niveau n. **I1 (niveau n)** = Part(2A, n) moins Part(référence, n). **Unité :** points de pourcentage, pour n = 1 et n = 2. |
| 3. Paramètres | **La base de référence** : les 94 autres départements, la Haute-Corse (2B), ou 13 départements méditerranéens (choix exploratoire de l'auteure, ni validé par le groupe ni par le SDIS). **Les niveaux** : 1 et 2 (le niveau 3 n'a que 17 jours en 2A, le niveau 4 aucun). **La prévision** : `niveau_j1`, la prévision du lendemain. **La saison** : bulletins publiés du 3 juin au 30 septembre, soit les jours du 4 juin au 1er octobre (120 jours). **La définition d'un feu** : type "F" de la BDIFF, toutes surfaces. **La règle de calcul** : proportion globale (tous les jours-départements d'un groupe comptés ensemble). |
| 4. Périmètre, période, grain, fréquence | Corse-du-Sud et base de référence ; saison de juin à septembre ; grain de la donnée : un jour d'un département, agrégé en une valeur par niveau et par saison ; calcul en fin de saison (octobre). Pas de lecture en cours d'été, parce qu'un niveau n'a pas assez de jours. |
| 5. Source et champs | Météo des forêts, archives sur data.gouv.fr (`docs/sources/fiche-meteo-des-forets.md`) : `date` (date de publication, heure UTC), `num_dep`, `niveau_j1`. BDIFF, export de la consultation publique (`docs/sources/fiche-bdiff.md`) : `Département`, `Date de première alerte`. Pour 2027 : feux saisis par le SDIS 2A (à demander), confirmés par la BDIFF en 2028. |
| 6. Lignes utilisables | **BDIFF :** `Département`, `Code INSEE` et `Date de première alerte` renseignés sur 3 908 lignes sur 3 908, aucune date illisible. Sur ces 3 908 feux, 2 612 tombent dans la fenêtre de la Météo des forêts (139 en Corse-du-Sud, 87 en Haute-Corse), 1 252 sont hors fenêtre (avant le 4 juin ou après le 1er octobre) et 44 sont dans des départements d'outre-mer absents de la Météo des forêts. **Météo des forêts :** 23 040 lignes, soit 96 départements sur 240 jours, `date`, `num_dep` et `niveau_j1` renseignés partout, `niveau_j1` toujours entre 1 et 4, aucun doublon. |
| 7. Proxy et biais | La donnée voulue est « le comportement des feux en 2A à un niveau de l'indice est comparable à celui d'une autre base ». Le proxy est la part de jours avec au moins un feu. **Biais 1 :** les départements n'ont pas la même taille : un grand département continental est plus vaste qu'un département corse, donc un jour avec feu n'y a pas le même sens (écart **surestimé ou sous-estimé** selon la taille). **Biais 2 :** les départements ne saisissent pas tous les petits feux de la même façon dans la BDIFF : un écart peut venir de la saisie. **Biais 3 :** la date de la BDIFF n'a pas de fuseau précisé ; 24 feux sur 204 en 2A tombent entre 22 h et 2 h. Test : en lisant les dates en UTC puis à l'heure de Paris, les parts du 2A changent de moins de 1 point aux niveaux 1 et 2 (17,5 % et 39,8 %). **Biais 4 :** si le dispositif empêche des feux de partir, les parts du 2A changent sans que le lien entre l'indice et les feux ait changé, et l'écart bouge pour une raison qui n'a rien à voir avec la ressemblance des bases. |
| 8. Décision éclairée | **Écart d'au plus [y points] aux niveaux 1 et 2** : la référence tient, le SDIS 2A peut fixer son seuil avec des données plus nombreuses que les siennes. **Écart supérieur à la tolérance** : la référence est réexaminée avant 2028 (une saison différente peut l'expliquer) et, si l'écart se confirme, le SDIS fixe un seuil propre au 2A à partir de ses données. **Un seul niveau dépasse la tolérance** (par exemple le niveau 1 tient et le niveau 2 non) : proposition à valider avec le SDIS. On n'emprunte pas la référence pour le niveau qui dépasse, et on la réexamine pour ce niveau avant 2028. Un niveau sans assez de jours (voir I2) ne décide rien. |
| 9. Propriétaire | Calcul : Saran Diabagate (`src/analyse_comparaison.py`). Relecture : Arouna Touré (pipeline). |

**Valeur de départ (2024-2025) :** part du 2A de 17,5 % au niveau 1 (10 jours sur 57) et de 40,4 % au niveau 2 (67 sur 166). Écart avec les 94 autres départements : **+14,6 points** au niveau 1 et **+17,6 points** au niveau 2 (proportion globale). Le 2A s'écarte nettement de la moyenne des autres départements aux niveaux 1 et 2. La référence reste à choisir.

#### Un paramètre change : la base de référence

| Référence | Écart au niveau 1 | Écart au niveau 2 | Largeur de l'intervalle au niveau 2 |
|---|---|---|---|
| Les 94 autres départements | +14,6 | +17,6 | 15,1 points |
| 13 départements méditerranéens | +8,0 | +8,5 | 15,6 points |
| Haute-Corse | +6,3 | +9,7 | 20,5 points |

- **Ce qui bouge :** la valeur de l'écart, de 6,3 à 14,6 points au niveau 1 et de 8,5 à 17,6 points au niveau 2, selon la référence. Avec la moyenne des autres départements, le 2A paraît très éloigné ; avec la Haute-Corse ou les départements méditerranéens, il l'est moins. Une règle « niveau 2 ou plus » déclencherait le dispositif 17,1 % des jours dans les autres départements, contre 76,2 % des jours en 2A.
- **Ce qui ne bouge pas :** la formule, la source, les parts du 2A (17,5 % et 40,4 %), et le sens de l'écart (positif aux deux niveaux avec les trois références). Les intervalles suggèrent un écart positif entre le 2A et les références, mais il faut les lire avec prudence : ils supposent des jours indépendants, alors que des jours consécutifs ont des conditions météorologiques proches, et certains niveaux ont peu de jours. L'intervalle exclut à peine zéro avec les départements méditerranéens et ne l'exclut pas avec la Haute-Corse. Il ne prouve donc aucune différence entre territoires.
- **Autre variante :** la moyenne des proportions de chaque département, au lieu de la proportion globale, donne des parts de référence plus basses (3,6 % au niveau 1, 16,9 % au niveau 2) et donc des écarts plus grands (13,9 et 23,5 points). La proportion globale est gardée (voir « Rôle de chaque indicateur »). Elle donne plus de poids aux départements qui ont plus de jours observés. Elle décrit l'ensemble des observations, pas un département moyen.

#### Avis RACER

| Critère | Avis |
|---|---|
| Relevant | Oui : il mesure directement si le lien entre l'indice et les feux du 2A ressemble à celui d'une base plus grande, ce qui décide si le SDIS peut s'appuyer sur elle pour son seuil. |
| Accepted | À confirmer avec le SDIS 2A : le choix de la référence, la définition d'un feu (type "F", toutes surfaces) et la tolérance [y points]. |
| Credible | Oui si la référence et la définition sont figées avant le 1er juin 2027 ; un écart peut quand même venir d'une saison différente (météo, nombre de feux) ou de la façon de saisir les feux, pas seulement d'un lien différent. |
| Easy | Oui pour le calcul : cinq champs renseignés à 100 %, tout est recalculé par `src/analyse_comparaison.py`. La difficulté est d'obtenir les feux de 2027 auprès du SDIS 2A, car la BDIFF ne les publiera qu'en 2028. |
| Robust | Pas seul : il dépend de la référence choisie (de 6,3 à 14,6 points au niveau 1) et on ne peut plus le lire quand un niveau a trop peu de jours (8 jours au niveau 1 en 2025). C'est le rôle de I2. |

### I2 · Nombre de jours du 2A au niveau lu (garde-fou de I1)

| Rubrique | Contenu |
|---|---|
| Formule | Nombre de jours du 2A dont `niveau_j1` vaut n sur la saison (120 jours au plus), accompagné de la largeur de l'intervalle à 95 % de l'écart de I1 (méthode de Newcombe). **Unité :** jours ; points pour la largeur. |
| Paramètres | Les mêmes que I1 (saison, niveau, référence). **Le seuil plancher** : 30 jours (voir ci-dessous). |
| Source et lignes utilisables | Météo des forêts, champ `niveau_j1` : 23 040 lignes sur 23 040 renseignées, niveau toujours entre 1 et 4. |
| Valeur de départ | Sur 2024-2025 : 57 jours au niveau 1 et 166 au niveau 2 ; par saison, 49 et 68 jours en 2024, **8** et 98 jours en 2025. Largeur de l'intervalle de l'écart avec les 94 autres départements : 19,6 points au niveau 1 et 15,1 au niveau 2. |
| Seuil plancher | I1 n'est pas lu à un niveau si le 2A a moins de **30 jours** à ce niveau dans la saison. C'est une règle pratique provisoire, que j'ai fixée pour que le garde-fou soit vérifiable. Elle ne vient ni de la commande ni du cours, et ni la statistique ni le groupe ne l'ont validée. Pour une part de 40 %, l'intervalle à 95 % de la part du 2A a une demi-largeur d'environ 20 points avec 20 jours, 16,5 avec 30, 14,5 avec 40 et 12,3 avec 57 (calcul de Wilson, jours supposés indépendants). 30 jours ne rendent donc pas la mesure fiable : ils écartent seulement les cas extrêmes, comme les 8 jours du niveau 1 en 2025 (aucun feu). Avec ce plancher, ce niveau n'est pas lu, et l'écart de -4,2 à -16,7 points selon la référence ne dit rien. |
| Décision éclairée | Si un niveau est sous le plancher, la direction ne tire aucune conclusion à ce niveau pour la saison. Elle regarde l'autre niveau, ou elle cumule avec les saisons précédentes, mais seulement si les périodes et les conditions restent assez comparables (même fenêtre de saison, même définition d'un feu, même référence). |
| Biais | Un jour de plus ou de moins pèse beaucoup : au niveau 1 en 2025, un seul jour avec feu ferait passer la part de 0 % à 12,5 %. Le plancher dit si on peut lire I1, pas si le lien est le même ailleurs. |
| Propriétaire | Saran Diabagate, relu par Arouna Touré. |

### Pre-mortem

On imagine qu'à l'automne 2027, le SDIS 2A a pris une mauvaise décision à cause de I1.

| Rang | Raison de l'échec | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| 1 | La référence est choisie après coup, ou trop proche du 2A : l'écart est petit et le SDIS emprunte un seuil qui ne vaut pas pour lui. | Moyenne : le choix est libre tant qu'il n'est pas figé. | Haute : le seuil est faux pour tout l'été. | La référence et son critère sont figés avant le 1er juin 2027 (écrit dans l'objectif). Les trois références sont toujours affichées côte à côte (écarts de 6,3 à 14,6 points au niveau 1), avec l'effet d'une règle empruntée : « niveau 2 ou plus » déclencherait 17,1 % des jours dans les autres départements contre 76,2 % en 2A. |
| 2 | Une seule saison est lue comme une preuve, à un niveau qui a trop peu de jours. En 2025, le niveau 1 a 8 jours en 2A, aucun avec feu, et le niveau 2 avec les départements méditerranéens passe de +14,0 points en 2024 à +3,8 en 2025. | Haute : la mesure de 2027 est une saison, et les saisons varient de plus de 10 points. | Moyenne : la référence est abandonnée ou gardée à tort. | I2 : seuil plancher de 30 jours par niveau, intervalle de l'écart toujours affiché, les deux niveaux lus en même temps (comme dans l'objectif). |
| 3 | Les feux de 2027 transmis par le SDIS 2A ne sont pas saisis comme ceux de la BDIFF (petits feux, dates) : l'écart vient de la saisie, pas du comportement des feux. | Moyenne. | Moyenne : la mesure d'octobre 2027 est faussée, mais elle est corrigée en 2028 avec la BDIFF. | Quelques feux relus avec le SDIS, comparaison avec la BDIFF en 2028, et test sur le fuseau horaire (moins de 1 point d'écart aux niveaux 1 et 2). |

### Rôle de chaque indicateur (ma part du jeu)

| Rôle | Indicateur | Raison |
|---|---|---|
| KPI principal | I1, écart entre la part de jours avec feu du 2A et celle de la référence, aux niveaux 1 et 2 | Il répond à la décision de la Q4 : sur quelles données le SDIS 2A fixe son seuil. |
| KPI secondaire | Part des jours avec au moins un feu en 2A, à chaque niveau (17,5 % au niveau 1, 40,4 % au niveau 2) | Elle situe le 2A lui-même, sans dépendre de la référence : si cette part monte beaucoup, la direction le voit même si l'écart reste le même. |
| Garde-fou | I2, nombre de jours du 2A au niveau lu, avec la largeur de l'intervalle | Il évite de lire comme un résultat un écart dû au hasard (8 jours au niveau 1 en 2025). |
| Contexte | Nombre de feux du 2A dans la fenêtre (76 en 2024, 63 en 2025) et nombre de jours par niveau | Il montre si la saison a été calme ou sévère. On le note sans le piloter : le SDIS ne choisit pas le nombre de feux. |
| Écarté | Écart avec la moyenne des proportions de chaque département | Il dépend du nombre de jours de chaque département : au niveau 1, la médiane des départements est de 1,4 % contre 3,6 % pour la moyenne, et seuls 50 des 94 autres départements atteignent le niveau 3. La proportion globale est plus stable. |
| Écarté | Écart au niveau 3 | Le 2A n'a que 17 jours au niveau 3 sur deux saisons, et l'intervalle de l'écart avec les 94 autres départements va de -11,4 à +31,7 points : il ne dit rien. |
| Écarté | Écart au niveau 4 | Jamais atteint en Corse en 2024 et 2025 : rien à comparer. |