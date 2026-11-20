# Diagnostic stratégique : binôme Ahmed Philippe et Biolohf Tchatchoua

- **Séance :** UE01.B, S1, exercice 1
- **Binôme :** Ahmed Philippe (Q1, où concentrer les moyens) et Biolohf Tchatchoua (Q3, combien de jours le seuil déclenche)
- **Date :** 2026-11-20
- **Supports :** la commande de la direction du SDIS 2A, reformulée dans \docs/analyse/commande-groupe.md\ (section 3) ; nos objectifs \kpi/objectif-ahmed-philippe.md\ et \kpi/objectif-biolohf-tchatchoua.md\.
- **Calculs :** volet Q1 par \src/objectif_q1.py\ (export BDIFF 2A, type de feu F, 2006-2025, 4 694 feux) ; volet Q3 par \src/calcul_diagnostic.py\ (Météo des forêts \
iveau_j1\ croisée avec la BDIFF, du 4 juin au 1er octobre 2024 et 2025, 240 jours, 139 feux), résultats dans \docs/qualite/calculs-diagnostic.md\.
- **Lien avec le diagnostic de Saran et Arouna** (\kpi/diagnostic-strategique.md\, PR #82) : même lecture des quatre niveaux. Ce fichier ajoute deux tests qui n'y sont pas : la liste de communes choisie sur le passé retrouve-t-elle les feux de l'été suivant (Q1), et un seuil peut-il couvrir l'essentiel des feux sans déclencher trop de jours (Q3).

## Les quatre niveaux

| Niveau | Pour le SDIS 2A | Établi ou supposé | Pièce |
|---|---|---|---|
| Stratégie | Lutter au mieux contre les départs de feu pendant l'été 2027, avec des moyens limités. | Établi | Commande : « où faut-il concentrer nos moyens, humains comme financiers, pour lutter au mieux contre les départs de feu ? » |
| Enjeu | Le budget ne permet pas de renforcer le dispositif partout pendant tout l'été, et le seuil actuel se trompe dans les deux sens. | Établi | Commande : « notre budget ne nous permet pas de renforcer le dispositif sur tout le département pendant tout l'été », « Le seuil actuel ne nous convient pas ». |
| Objectif | Placer le dispositif renforcé là où partent les feux (une liste limitée de communes) et les jours où ils partent (un seuil), sans dépasser le nombre de jours que le budget finance. | **Supposé** | La commande pose deux questions, elle ne fixe ni résultat chiffré, ni nombre de communes, ni nombre de jours finançables. |
| Action | Arrêter avant la saison une liste de communes prioritaires et le niveau de la Météo des forêts qui déclenche le dispositif renforcé (patrouilles, guet). | Établi pour le seuil, supposé pour la liste de communes | Commande : « à partir de quel niveau de la Météo des forêts devons-nous déclencher le dispositif renforcé (patrouilles, guet, etc.) ? ». La commande demande « où » concentrer les moyens, sans dire sous quelle forme (liste de communes, sectors, massifs). |

## Hypothèse stratégique (niveau Objectif)

**Le SDIS 2A peut cibler son dispositif à l'avance, avec les données dont il dispose avant la saison : une liste de communes faite sur les années passées retrouve l'essentiel des feux de l'été suivant (volet Q1), et un seuil de la Météo des forêts couvre l'essentiel des feux sans déclencher plus de jours que le budget n'en finance (volet Q3).**

- **Pièce qui la fonde :** la commande demande « où » et « à partir de quel niveau » concentrer des moyens limités ; les deux réponses doivent être fixées avant la saison, donc à partir du passé.
- **Volet Q1, confirmé si** une liste de 20 communes (16 % des 124), classées sur les 10 années précédentes, retrouve en moyenne au moins la moitié des feux de l'été suivant et jamais moins de 40 % ; **infirmé si** elle en retrouve moins de 30 % en moyenne (les feux changeraient de commune d'un été à l'autre). Entre les deux, non tranché.
- **Volet Q3, confirmé si** un seuil couvre au moins 80 % des feux de l'été en déclenchant au plus le nombre de jours que le budget finance ; **infirmé si** aucun seuil n'y parvient.
- **Choix des seuils :** fixés par le binôme pour rendre le verdict vérifiable (20 communes, 50 %, 40 %, 30 %, 80 %) ; ils ne viennent ni de la commande ni du cours. Le nombre de jours finançables, lui, n'est connu d'aucune source (décision 3 de la matrice).

## Confrontation aux résultats

### Volet Q1 : confirmé pour les départs de feu, pas pour les surfaces brûlées

Test "à l'aveugle", comme la direction devra le faire en 2027 : pour chaque été de 2016 à 2025, la liste des 20 communes est faite sur les 10 années précédentes, puis on compte les feux de l'été (juin à septembre) partis dans ces communes.

- La liste retrouve en moyenne **55,2 %** des feux de l'été suivant, entre **45,3 %** (2022) et **65,0 %** (2017). Elle ne descend jamais sous 40 % : **le volet Q1 est confirmé.**
- Sur les étés 2024-2025, avec une liste faite sur 2014-2023 : **53,2 %** (74 feux sur 139). C'est la situation de référence de l'objectif d'Ahmed.
- **Réserve :** la même liste ne retrouve que **30,2 %** des hectares brûlés de ces deux étés (91 ha sur 302), et 10,3 % à l'été 2025, à cause d'un seul feu de 182 ha parti à Sari-Solenzara, hors de la liste. Une liste fondée sur le nombre de départs ne prévoit pas où partent les grands feux : une partie du dispositif doit rester mobile.

### Volet Q3 : non tranché, mais le choix est presque binaire

| Seuil de \
iveau_j1\ | Jours déclenchés sur 240 | Par été | Feux couverts sur 139 |
|---|---|---|---|
| niveau 2 ou plus | 183 (76,25 %) | 71 en 2024, 112 en 2025 | 125 (89,9 %) |
| niveau 3 ou plus | 17 (7,1 %) | 3 en 2024, 14 en 2025 | 13 (9,4 %) |
| niveau 4 | 0 | 0 | 0 |

- Seul le niveau 2 ou plus couvre au moins 80 % des feux, et il déclenche en moyenne 91,5 jours par été. Le niveau 3 ou plus reste dans n'importe quel budget, mais il ne couvre qu'un feu sur dix. **Il n'existe pas de seuil intermédiaire avec l'indice seul.**
- **Verdict : les données ne permettent pas de trancher**, parce que le nombre de jours finançables n'est pas connu. Si le budget finance au moins 112 jours par été (le niveau de 2025), le volet est confirmé ; s'il en finance moins de 71 (le niveau de 2024), il est infirmé, et le seuil seul ne suffit pas.
- C'est une limite de l'objectif de Biolohf : sa cible de 92 jours par été est provisoire et doit être fixée avec le SDIS 2A.

### Ce que les deux volets disent ensemble

Le temps (le seuil) et l'espace (la liste de communes) ne se règlent pas avec la même précision. La liste de communes est stable d'un été à l'autre et se prépare à l'avance. Le seuil, lui, oblige à choisir entre beaucoup de jours (niveau 2) et peu de feux couverts (niveau 3). Une piste à tester par le groupe : déclencher au niveau 2 seulement dans les communes de la liste, et au niveau 3 ailleurs, pour réduire le nombre de jours-commune sans perdre la majorité des feux. Ce croisement n'est pas encore calculé.

## Limites

- **Deux saisons seulement pour le volet Q3** (240 jours, 17 jours au niveau 3 ou plus) : un jour de plus ou de moins change beaucoup les pourcentages. Le volet Q1 repose sur 20 ans de données, mais il ne dit rien des jours.
- **Le nombre de jours finançables et le seuil actuel ne sont pas connus** (décision 3 de la matrice) : le volet Q3 ne peut pas être tranché sans le SDIS 2A.
- **« Danger élevé » = niveau 3 ou plus** est un choix de calcul (question ouverte Q-1 de \docs/decisions.md\).
- **La commune est le seul lieu disponible** dans la BDIFF : une grande commune (Sartène, Porto-Vecchio, Ajaccio) n'est pas couverte en entier par une patrouille. Le classement n'est pas rapporté à la surface boisée (BD Forêt, D-008).
- **Effet du dispositif :** s'il empêche des feux de partir, les feux "retrouvés" par la liste et les feux "couverts" par le seuil baissent alors que le dispositif fonctionne.
- **Les feux de 2026 sont exclus** (D-009) ; en 2026, le niveau 2 ou plus aurait déclenché 128 jours, ce qui montre que le nombre de jours varie beaucoup d'un été à l'autre.
- **Les feux hors de la fenêtre de la Météo des forêts** (avant le 4 juin ou après le 1er octobre) ne sont pas couverts par le volet Q3.
