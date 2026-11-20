# Objectif : Ahmed Philippe

- **Séance :** UE01.B, S1 (diagnostic, puis de la question analytique à l'objectif)
- **Date :** 2026-11-19
- **Données utilisées :** BDIFF, export de la consultation publique avec les mêmes critères que `docs/qualite/profil-bdiff.md` (Corse-du-Sud, type de feu "F", date de première alerte du 2006-01-01 au 2025-12-31) : 4 694 feux, 124 communes. Champs utilisés : `Année`, `Code INSEE`, `Nom de la commune`, `Date de première alerte` (pour isoler les étés, juin à septembre), `Surface parcourue (m2)`.
- **Calculs :** tous les chiffres de ce fichier sont refaits par `src/objectif_q1.py` (`python src/objectif_q1.py data/raw/bdiff_2A_2006_2025.csv`). Le fichier brut n'est pas dans le dépôt (`data/raw` n'est pas versionné). Les communes sont classées par nombre de feux ; en cas d'égalité, elles sont départagées par code INSEE.

## Diagnostic (ma version, pour la mise en commun du groupe)

| Niveau | Sur notre sujet | Établi ou supposé |
|---|---|---|
| Stratégie | Lutter au mieux contre les départs de feu en Corse-du-Sud pendant la saison 2027. | Établi : la commande demande « où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ». |
| Enjeu | Le budget ne permet pas de renforcer le dispositif sur tout le département pendant tout l'été : il faut choisir où le placer. | Établi : citation de la commande, reprise dans `docs/analyse/commande-groupe.md` (section 3). |
| Objectif | Placer les moyens là où les feux partent, dans un nombre limité de communes. | Supposé : la commande pose une question, elle ne fixe ni résultat ni critère de zone prioritaire (« critères qui rendent une zone prioritaire » : à demander au SDIS 2A). |
| Action | Arrêter avant la saison une liste de communes prioritaires pour les patrouilles et le guet. | Supposé : la répartition actuelle des moyens du SDIS 2A n'est pas connue. |

### Hypothèse stratégique (niveau Objectif)

"Le SDIS 2A cherche à concentrer ses moyens sur un petit nombre de communes où les départs de feu se répètent d'une année à l'autre."

- **Pièce qui la fonde :** la commande parle de « concentrer nos moyens » sous contrainte de budget ; la question Q1 du groupe pose le test « si quelques communes concentrent l'essentiel des feux chaque année, elle y affecte en priorité patrouilles, guet et investissements durables ; si les feux sont dispersés ou changent de place, elle garde une couverture large et un dispositif mobile ».
- **Confirmée si** une minorité de communes regroupe la majorité des départs de feu **et** si une liste choisie sur les années passées retrouve l'essentiel des feux de l'année suivante.
- **Infirmée si** les feux sont dispersés (il faut presque toutes les communes pour en couvrir la moitié) ou s'ils changent de commune d'une année à l'autre.

### Verdict : confirmée pour les départs de feu, pas pour les surfaces brûlées

- **Concentration :** sur les étés 2006-2025 (juin à septembre, 2 509 feux), 12 communes sur 124 (10 %) regroupent la moitié des feux ; il en faut 40 (32 %) pour 80 %. Sur les années entières, il en faut 17 pour la moitié et 45 pour 80 %.
- **Stabilité :** une liste de 20 communes classées sur les 10 années précédentes retrouve chaque été entre 45,3 % (2022) et 65,0 % (2017) des feux de l'été suivant, 55,2 % en moyenne sur 2016-2025. Le classement est donc stable : les mêmes communes reviennent.
- **Réserve, les surfaces :** les surfaces brûlées dépendent de quelques grands feux qui ne se prévoient pas par le nombre de départs. Sur 2006-2025 (années entières), trois communes font la moitié des 13 133 ha brûlés (Fozzano 3 227 ha, Quenza 3 221 ha, Sartène 1 321 ha), dont deux hors des 20 communes qui ont le plus de feux. À l'été 2025, le plus grand feu (Sari-Solenzara, 182 ha, le 23 juin) part hors de la liste.

Conséquence pour la direction : concentrer patrouilles et guet sur une liste de communes est justifié pour les départs de feu, mais une partie du dispositif doit rester mobile pour les grands feux. Cette réserve est une limite de mon objectif.

## Question analytique

Où se concentrent les départs de feu en Corse-du-Sud, et ces zones restent-elles les mêmes d'une année à l'autre ? (Q1 de la matrice du groupe.)

## Décision que la réponse nourrit

Dans quelles communes la direction concentre patrouilles, guet et investissements pour l'été 2027, sachant qu'elle ne peut pas couvrir tout le département.

## Trois formulations

| Formulation | Texte | Pourquoi ce n'est pas encore suffisant |
|---|---|---|
| Action | Établir une liste de communes prioritaires pour le dispositif renforcé. | C'est ce que l'on fait, pas le résultat attendu : rien ne dit si la liste est bonne. |
| Objectif | Concentrer le dispositif sur les communes où partent la majorité des feux. | Le résultat est nommé, mais sans valeur de départ, sans cible, sans échéance, et sans condition : on peut l'atteindre en ajoutant des communes jusqu'à couvrir tout le département. |
| Objectif SMART | Pour la saison 2027 (juin à septembre), faire passer de 53,2 % à 60 % (valeur provisoire, à valider avec le SDIS 2A) la part des départs de feu de l'été en Corse-du-Sud qui partent dans les communes prioritaires, avec une liste de 20 communes au plus, arrêtée avant le 1er juin 2027 à partir des seules données BDIFF disponibles à cette date. Mesure en octobre 2027 sur les feux saisis par le SDIS 2A, confirmée en 2028 par la BDIFF. | |

## L'objectif SMART, critère par critère

| Critère | Contenu |
|---|---|
| Spécifique | Les départs de feu de forêt (type "F" de la BDIFF, toutes surfaces) de juin à septembre en Corse-du-Sud (mois de la `Date de première alerte`), et parmi eux ceux qui partent dans une commune de la liste prioritaire (rattachement par `Code INSEE`). La liste compte au plus 20 communes, soit 16 % des 124 communes du 2A. |
| Mesurable | La part passe de 53,2 % à 60 %. Elle se calcule en divisant le nombre de feux de l'été dont le `Code INSEE` est dans la liste par le nombre total de feux de l'été dans le 2A. La BDIFF ne publiera 2027 qu'en 2028 : la mesure de fin de saison se fait sur les feux saisis par le SDIS 2A (à demander), puis elle est confirmée avec la BDIFF. |
| Atteignable | Avec la méthode actuelle (classement des 10 années précédentes, 20 communes), 60 % a été atteint ou dépassé 3 étés sur 10 entre 2016 et 2025 (2017 : 65,0 % ; 2018 : 62,1 % ; 2020 : 62,5 %) : la cible est donc déjà observée, mais pas de façon régulière. L'atteindre de façon régulière suppose d'améliorer le classement (par exemple donner plus de poids aux années récentes, ou rapporter les feux à la surface boisée de la BD Forêt, D-008). La cible reste provisoire et doit être fixée avec la direction du SDIS 2A une fois la situation de référence présentée. |
| Réaliste | La condition "20 communes au plus" empêche de gagner en allongeant la liste : avec 30 communes, la part monte à 62,6 % sans que le classement soit meilleur. La condition "arrêtée avant le 1er juin 2027" empêche de choisir les communes après avoir vu les feux. |
| Temporel | Saison 2027 (juin à septembre), mesurée en octobre 2027 avec les données du SDIS 2A ; confirmation avec la BDIFF lors de sa publication en 2028. |

## Situation de référence

Mesurée "à l'aveugle", comme la direction devra le faire en 2027 : la liste est construite sur les 10 années précédentes (2014-2023, années entières, pour avoir assez de feux par commune), puis on regarde où partent les feux des deux derniers étés publiés (juin à septembre 2024 et 2025 : 139 feux, 76 en 2024 et 63 en 2025).

| Nombre de communes dans la liste | Feux des étés 2024-2025 dans la liste | Part |
|---|---|---|
| 10 | 54 sur 139 | 38,8 % |
| 15 | 66 sur 139 | 47,5 % |
| **20** | **74 sur 139** | **53,2 %** |
| 25 | 79 sur 139 | 56,8 % |
| 30 | 87 sur 139 | 62,6 % |

Valeur de départ de l'objectif : **53,2 %** (74 feux sur 139), avec 20 communes (39 sur 76 à l'été 2024, 35 sur 63 à l'été 2025).

Classer les communes sur les seuls étés 2014-2023 donne presque le même résultat (54,0 %, 75 feux sur 139), mais avec des ex aequo à la vingtième place : le classement sur les années entières est retenu.

La liste de référence (20 communes ayant eu le plus de feux sur 2014-2023, de la première à la vingtième) : Porto-Vecchio, Zonza, Ajaccio, Appietto, Bonifacio, Sartène, Alata, Bastelica, Vero, Lecci, Peri, Sarrola-Carcopino, Figari, Calcatoggio, Sotta, Palneca, Carbuccia, Vico, Zicavo, Conca.

Le choix de 20 communes est provisoire : le nombre de communes que le budget permet de couvrir n'est pas connu (contenu et coût du dispositif renforcé : à demander au SDIS 2A). Si le budget permet 15 ou 25 communes, la référence devient 47,5 % ou 56,8 %.

## Test de cohérence

Comment atteindre l'objectif sans faire avancer la stratégie ?

1. **Allonger la liste.** Plus il y a de communes, plus la part monte (62,6 % avec 30 communes), mais le dispositif est dilué et le budget dépassé. C'est pour bloquer ce contournement que la liste est plafonnée à 20 communes.
2. **Choisir la liste après coup.** Une liste faite en connaissant les feux de 2027 atteindrait la cible sans rien prévoir. La liste est donc arrêtée avant le 1er juin 2027 et n'est plus modifiée pendant la saison.
3. **Couvrir les départs, mais pas les dégâts.** La liste peut retrouver beaucoup de petits feux pendant qu'un grand feu brûle ailleurs. Aux étés 2024-2025, les 20 communes ont 53,2 % des départs mais seulement 30,2 % des surfaces brûlées (91 ha sur 302) ; à l'été 2025, 10,3 % (22 ha sur 217), à cause d'un seul feu de 182 ha à Sari-Solenzara. L'objectif serait atteint sans que la lutte contre les feux progresse vraiment. La part de la surface brûlée qui se trouve dans les communes de la liste est à suivre à côté de l'objectif (garde-fou à construire en S2).

## Limites

- **L'effet du dispositif lui-même.** Si les patrouilles et le guet empêchent des feux de partir dans les communes de la liste, la part des feux dans la liste baisse : l'objectif pénaliserait un dispositif efficace. Ce biais ne peut pas être corrigé avec nos données ; il est à signaler à la direction.
- **Une seule saison mesure mal.** Avec la même méthode, la part varie de 45,3 % à 65,0 % selon les étés (2016-2025) : l'écart entre la référence et la cible (6,8 points) est plus petit que cette variation naturelle. Avec environ 70 feux par été (76 en 2024, 63 en 2025), un feu pèse environ 1,5 point. Un résultat de 2027 au-dessus de la cible ne prouvera pas, à lui seul, que la liste est meilleure ; le plan de mesure (S3) devra en tenir compte.
- **Les grands feux ne se prévoient pas par le nombre de départs** (voir le verdict) : l'objectif ne couvre que les départs de feu.
- **Le nombre de feux baisse fortement** (407 en 2006, 86 en 2023, 93 en 2025) : les comparaisons entre années se font en part, jamais en nombre.
- **Les feux de 2026 ne sont pas utilisés** : l'année n'est pas terminée et la BDIFF ne la publie qu'en 2027 (décision 1 de la matrice). La liste 2027 sera faite sur 2016-2025, ou sur 2017-2026 si la BDIFF publie 2026 avant le 1er juin 2027.
- **La commune est le seul lieu disponible** : un feu est rattaché à la commune de son point de départ, pas à une zone plus fine. Les grandes communes (Ajaccio, Porto-Vecchio, Sartène) pèsent plus parce qu'elles sont grandes.
- **La mesure d'octobre 2027 dépend de la transmission des feux de la saison 2027 par le SDIS 2A.** Sans cette transmission, l'objectif ne pourra être mesuré qu'en 2028, à la publication de la BDIFF.
