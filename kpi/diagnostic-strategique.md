# Diagnostic stratégique

- **Séance :** UE01.B, S1, exercice 1
- **Binôme :** Saran Diabagate et Arouna Touré
- **Date :** 2026-11-19
- **Supports :** la commande de la direction du SDIS 2A, citée mot pour mot d'après l'énoncé « Exercice 1 - De la commande aux données - Corse » (reformulée par le groupe dans `docs/analyse/commande-groupe.md`, section 3, « La décision à éclairer ») ; nos résultats : profils `docs/qualite/`, matrice `docs/sources/matrice.md`. Tous les chiffres tirés des données sont recalculés par `src/calcul_diagnostic.py` à partir des fichiers bruts (Météo des forêts 2024-2026, exports BDIFF 2A et 2B 2006-2025, feux de forêt de type F, filtre vérifié par le script dans l'en-tête de chaque export) ; résultats dans `docs/qualite/calculs-diagnostic.md`.

## Les quatre niveaux

| Niveau | Question | Pour le SDIS 2A | Établi ou supposé | Pièce |
|---|---|---|---|---|
| Stratégie | Que veut faire l'organisation ? | Lutter au mieux contre les départs de feu pendant l'été 2027, avec des moyens limités. | Établi | Commande : « où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ? » |
| Enjeu | Qu'est-ce qui bloque ? Qui contraint ? | Le seuil actuel semble produire des alertes sans feu observé, tandis que certains feux partent des jours où l'indice est au plus bas. Le budget ne permet pas de renforcer le dispositif partout pendant tout l'été. | Établi | Commande : « Le seuil actuel ne nous convient pas », « l'indice annonce souvent un danger élevé alors qu'aucun feu ne se déclare », « des feux partis des jours où l'indice était au plus bas », « notre budget ne nous permet pas de renforcer le dispositif sur tout le département pendant tout l'été ». |
| Objectif | Quel résultat vise-t-on ? | Concentrer le dispositif renforcé sur les zones et les jours où le risque de départ de feu est le plus élevé, dans la limite du budget. | **Supposé** | La commande ne formule pas directement cet objectif : il est déduit des deux questions posées par la direction et des contraintes exprimées. |
| Action | Que décide-t-on ? Que fait-on ? | Choisir le niveau de la Météo des forêts qui déclenche le dispositif renforcé, et les zones où concentrer les moyens. | Établi | Commande : « à partir de quel niveau de la Météo des forêts devons-nous déclencher le dispositif renforcé (patrouilles, guet, etc.) ? » et la question des moyens citée en Stratégie. |

## Hypothèse stratégique

**Le SDIS 2A cherche à concentrer un budget limité là où et les jours où le risque de départ de feu est le plus important : sur des zones prioritaires de Corse-du-Sud et les jours où le niveau de la Météo des forêts justifie le déclenchement du dispositif renforcé.**

- **Pièces qui la fondent :** la commande (« où faut-il concentrer nos moyens », « Le seuil actuel ne nous convient pas », « notre budget ne nous permet pas de renforcer le dispositif sur tout le département pendant tout l'été »), reprise par la décision à éclairer de `docs/analyse/commande-groupe.md` (section 3). Elle comporte deux volets : où concentrer les moyens (Q1) et à partir de quel niveau déclencher le dispositif (Q2 et Q3).
- **Hypothèse confirmée si** (a) quelques communes concentrent une part importante des feux et restent parmi les plus touchées d'une période à l'autre (test de Q1), **et** (b) les résultats montrent à la fois des jours de danger élevé sans aucun feu observé et des feux partis les jours de danger faible (test de Q2).
- **Hypothèse infirmée si** les feux sont largement dispersés ou si les communes les plus touchées changent fortement d'une période à l'autre, ce qui plaiderait pour une couverture plus large, **ou** si l'une des deux erreurs liées au seuil est pratiquement absente.

## Confrontation aux résultats

Croisement, par `src/calcul_diagnostic.py` (méthode décrite en tête du script), de la prévision `niveau_j1` de la Météo des forêts (rapportée au lendemain de sa publication) avec les feux de forêt de la BDIFF (`Date de première alerte`), sur les jours communs aux deux sources : du 4 juin au 1er octobre 2024 et 2025, soit 240 jours par département. Dans cette analyse, « danger élevé » désigne les niveaux 3 ou plus et « danger faible » désigne le niveau 1.

| Département | Feux | Jours de danger élevé | Dont sans aucun feu | Feux partis un jour de danger faible |
|---|---:|---:|---:|---:|
| Corse-du-Sud (2A) | 139 | 17 | 7 (41,2 %) | 14 (10,1 %) |
| Haute-Corse (2B) | 87 | 9 | 3 (33,3 %) | 8 (9,2 %) |

Pour la Haute-Corse, 87 feux sont comptés sur les jours couverts par l'indice (du 4 juin au 1er octobre) ; 88 sont recensés sur juin-septembre calendaire, chiffre cité dans la PR #52.

« Danger faible » suit ici la commande, qui parle de feux partis « des jours où l'indice était au plus bas » : c'est le niveau 1. Le garde-fou de l'objectif (`kpi/objectif-arouna-toure.md`) porte, lui, sur tous les feux partis hors des jours de déclenchement (90,6 % au niveau 3), pour les raisons données dans ce fichier.

**Précaution de lecture :** les indicateurs « jours de danger élevé sans aucun feu » et « feux partis un jour de danger faible » n'ont pas le même dénominateur. Le premier est calculé en nombre de jours ; le second en nombre de feux. Ils ne doivent donc pas être comparés directement comme s'ils mesuraient la même chose. Par ailleurs, un jour sans feu observé ne signifie pas nécessairement que le risque était absent : aucun départ de feu n'a simplement été recensé ce jour-là.

### Verdict, volet (b) : le problème de compromis lié au seuil est confirmé

Les deux types de situations observées existent dans les deux départements étudiés : au moins un tiers des jours de danger élevé ne présentent aucun feu recensé (41,2 % en 2A et 33,3 % en 2B), tandis qu'environ un feu sur dix part un jour de danger faible.

**Le diagnostic confirme donc l'existence d'un compromis à arbitrer entre les jours de déclenchement sans feu observé et les départs de feu survenant à faible niveau de danger. Il ne permet pas encore de déterminer le seuil optimal.** Il faudra comparer les seuils possibles en tenant compte du nombre de jours de déclenchement, des feux survenus hors déclenchement et des moyens nécessaires.

Si le dispositif renforcé contribue à empêcher des départs de feu, certains jours d'alerte sans feu observé peuvent aussi correspondre à des interventions efficaces. Le nombre de jours de danger élevé sans feu ne doit donc pas être interprété automatiquement comme un taux de fausses alertes.

### Verdict, volet (a) : hypothèse globalement confirmée à l'échelle communale

Calcul sur l'export BDIFF du 2A (4 694 feux de 2006 à 2025, 124 communes, toutes touchées au moins une fois), par `src/calcul_diagnostic.py` (section « Volet zones » de `docs/qualite/calculs-diagnostic.md`) :

- **Concentration :** trois communes (Ajaccio : 327 feux, Porto-Vecchio : 317, Sartène : 265) regroupent 909 feux, soit 19,4 % (profil `docs/qualite/profil-bdiff.md`) ; les 10 premières communes regroupent 38,5 % des feux ; il faut 17 communes sur 124 (14 %) pour atteindre la moitié des feux.
- **Stabilité :** en comparant 2006-2015 (3 009 feux) et 2016-2025 (1 685 feux), 8 des 10 premières communes sont les mêmes (Ajaccio, Porto-Vecchio, Sartène, Zonza, Appietto, Alata, Bonifacio, Bastelica), et le classement des 124 communes est très proche d'une période à l'autre (corrélation de rang de Spearman : 0,89).

Ces résultats montrent une concentration des feux dans un groupe de communes et une stabilité relative de leur classement entre les deux périodes. La corrélation de Spearman de 0,89 indique une forte association entre les rangs des communes dans les deux périodes ; elle ne signifie pas que le nombre de feux est identique d'une période à l'autre.

**Le volet géographique de l'hypothèse est donc globalement confirmé à l'échelle communale.** Toutefois, ces résultats ne suffisent pas à désigner directement les meilleurs emplacements pour les patrouilles. La priorisation porte sur un groupe de communes plus large que trois communes : il faut 17 communes pour atteindre la moitié des feux recensés. De plus, le classement communal doit être complété par des informations sur la surface boisée, la localisation précise des départs de feu, l'accessibilité et les moyens déjà disponibles avant de devenir une recommandation opérationnelle.

L'indice apporte tout de même une information : en Corse-du-Sud, la part des jours avec au moins un feu passe de 17,5 % au niveau 1 à 40,4 % au niveau 2 et 58,8 % au niveau 3 (détail dans `docs/qualite/calculs-diagnostic.md`). Ces résultats montrent une relation entre le niveau de danger et la fréquence des jours avec feu, mais ils ne suffisent pas, à eux seuls, à choisir le seuil de déclenchement.

## Limites

- **« Danger élevé » = niveau 3 ou plus** est un choix de calcul : le sens de « danger élevé » est une question ouverte du groupe (Q-1, `docs/decisions.md`). Avec un autre sens, les valeurs changent.
- **Bornes des jours :** les feux sont comptés sur les jours couverts par `niveau_j1` (du 4 juin au 1er octobre), alors que la matrice parle de « juin-septembre ». Le nombre de feux du 2A est le même dans les deux cas (139) ; celui de la Haute-Corse diffère d'un feu (87 contre 88).
- **Échantillon court (volet b) :** deux saisons seulement, et 17 jours de danger élevé en Corse-du-Sud (26 avec la Haute-Corse). Le constat de l'existence des deux types de situations est valable pour cet échantillon, mais les pourcentages restent fragiles.
- **Grande variation d'une saison à l'autre :** 3 jours de danger élevé en 2024, 14 en 2025 et 18 en 2026 en Corse-du-Sud. Le nombre de jours de déclenchement associé à un même seuil peut donc changer sensiblement selon la saison.
- **Le niveau 4 n'a jamais été atteint** en Corse en 2024 et 2025 : un seuil à 4 ne peut pas être évalué sur ces deux saisons.
- **Le seuil actuel du SDIS n'est pas connu** (décision 3 de la matrice) : on ne peut pas mesurer les erreurs du seuil réellement appliqué, seulement comparer les seuils possibles.
- **Effet du dispositif :** si le dispositif renforcé empêche des feux, un jour d'alerte sans feu observé peut correspondre à une intervention efficace. Les jours de danger élevé sans feu ne sont donc pas nécessairement des fausses alertes.
- **Feux de 2026 exclus** (ticket #61) : l'été 2026, cité par la direction comme référence, n'entre pas dans le verdict.
- **Volet (a) à l'échelle de la commune :** la BDIFF ne donne pas de coordonnées ; une commune étendue peut cacher plusieurs massifs. Le classement ne tient pas compte de la surface boisée de chaque commune (dénominateur BD Forêt, D-008), ni de la surface brûlée. Il ne tient pas non plus compte, à ce stade, de l'accessibilité ni de la répartition des moyens opérationnels.
- **Données de coût :** aucun coût détaillé des patrouilles, du guet ou des autres moyens n'est présenté dans les résultats disponibles. La contrainte budgétaire est connue par la commande, mais elle ne peut pas encore être traduite en montant ou en capacité opérationnelle dans cette analyse.

## Suites nécessaires pour éclairer la décision

Avant de formuler une recommandation au SDIS 2A, il reste à :

1. **Compléter le volet géographique** en rapportant les feux à la surface boisée et, si les données le permettent, en étudiant leur localisation plus précise, l'accessibilité des secteurs et la répartition des moyens existants.
2. **Comparer les seuils possibles** en présentant, pour chacun, le nombre de jours de déclenchement, la part des feux survenus hors déclenchement et la part des jours déclenchés sans feu observé.
3. **Relier les résultats aux moyens disponibles** en estimant les besoins en patrouilles, en guet et en ressources humaines ou financières pour chaque scénario, avec les données du SDIS.
4. **Formuler une recommandation prudente** qui explicite le compromis retenu, les limites des données et les conditions de réévaluation après la saison 2027.

Le diagnostic doit aider le SDIS 2A à répartir ses moyens dans le temps et dans l'espace, selon le risque, la couverture opérationnelle et le budget.
