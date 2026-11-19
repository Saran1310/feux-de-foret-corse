# Objectif : Arouna Touré

- **Séance :** UE01.B, S1 (de la question analytique à l'objectif)
- **Date :** 2026-11-18, mis à jour le 2026-11-19 après les deux relectures de Biolohf
- **Données utilisées :** Météo des forêts (`niveau_j1`, saisons 2024 et 2025) et BDIFF (feux de forêt du 2A et du 2B, `Date de première alerte`). Profils : `docs/qualite/profil-mdf.md`, `docs/qualite/profil-bdiff.md`, `docs/qualite/profil-bdiff-2b.md`.

## Question analytique

À chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu en Corse-du-Sud ? (Q2 de la matrice du groupe.)

## Décision que la réponse nourrit

À partir de quel niveau de la Météo des forêts la direction déclenche le dispositif renforcé pour l'été 2027.

## Trois formulations

| Formulation | Texte | Pourquoi ce n'est pas encore suffisant |
|---|---|---|
| Action | Recalibrer le seuil de déclenchement du dispositif renforcé. | C'est ce que l'on fait, pas le résultat attendu : rien ne dit quand ce sera réussi. |
| Objectif | Réduire les jours de dispositif renforcé déclenchés sans qu'aucun feu ne parte. | Le résultat est nommé, mais sans valeur de départ, sans cible, sans échéance, et sans garde-fou : on peut l'atteindre en ne déclenchant plus jamais. |
| Objectif SMART | Sur la saison 2027 (juin à septembre), faire passer de 41,2 % à 33 % (valeur provisoire, à valider avec le SDIS 2A) la part des jours de déclenchement du dispositif renforcé sans aucun départ de feu en Corse-du-Sud, sans que la part des feux qui partent hors des jours de déclenchement dépasse 90,6 % (sa valeur avec un déclenchement au niveau 3). Mesure en octobre 2027 sur les feux saisis par le SDIS 2A, confirmée en 2028 par la BDIFF. | |

## L'objectif SMART, critère par critère

| Critère | Contenu |
|---|---|
| Spécifique | Les jours de déclenchement du dispositif renforcé en Corse-du-Sud (2A), et parmi eux ceux où aucun feu de forêt n'est enregistré. La référence est calculée pour un déclenchement au niveau 3 (prévision J+1 de la Météo des forêts supérieure ou égale à 3), le seuil actuel du SDIS n'étant pas connu. |
| Mesurable | La part passe de 41,2 % à 33 %. Elle se calcule en croisant les jours de déclenchement et la date de première alerte des feux. La BDIFF ne publiera l'année 2027 qu'en 2028 : la mesure de fin de saison se fait donc sur les feux saisis par le SDIS 2A (à demander, comme le coût du dispositif, décision 3 de la matrice), puis elle est confirmée avec la BDIFF en 2028. |
| Atteignable | 33 % est la valeur observée en Haute-Corse avec le même indice et le même seuil (3 jours sans feu sur 9 jours de danger élevé, étés 2024-2025) : un département voisin l'atteint déjà. Cette valeur repose toutefois sur 9 jours seulement : un jour de plus ou de moins la fait varier d'environ 11 points (2 jours sur 9 = 22,2 %, 4 jours sur 9 = 44,4 %). Elle reste provisoire et doit être validée avec la direction du SDIS 2A une fois la situation de référence présentée. Attention : avec la Météo des forêts seule, aucune règle de déclenchement testée sur 2024-2025 n'atteint 33 % en Corse-du-Sud sans dépasser la limite de 90,6 % (niveau 2 : 57,9 % ; niveau 3 : 41,2 % ; niveau 3 annoncé à la fois en J+2 et en J+1 : 0 % sur 1 seul jour, mais 98,6 % des feux hors déclenchement). Atteindre la cible suppose donc un critère de déclenchement en plus de l'indice (vent ou sécheresse observés, auxquels nous avons renoncé, décision Q9 de ma section 5), que seul le SDIS 2A peut préciser ; sans un tel critère, la cible est à revoir avec lui. |
| Réaliste | La condition "sans que la part des feux hors des jours de déclenchement dépasse 90,6 %" empêche de gagner en relevant simplement le seuil : au niveau 4, aucun jour ne serait déclenché en 2024 et 2025, et cette part passerait de 90,6 % à 100 %. |
| Temporel | Saison 2027 (juin à septembre), mesurée en octobre 2027 avec les données du SDIS 2A ; confirmation avec la BDIFF lors de sa publication en 2028. |

## Situation de référence

Mesurée sur les deux saisons communes aux deux sources (jours du 4 juin au 1er octobre 2024 et 2025, soit 240 jours ; 139 feux de forêt en Corse-du-Sud ces jours-là).

| Niveau `niveau_j1` | Jours | Jours avec au moins un feu | Part des jours avec feu | Feux |
|---|---|---|---|---|
| 1 (faible) | 57 | 10 | 17,5 % | 14 |
| 2 (modéré) | 166 | 67 | 40,4 % | 112 |
| 3 (élevé) | 17 | 10 | 58,8 % | 13 |
| 4 (très élevé) | 0 | 0 | sans objet | 0 |

Valeurs de départ de l'objectif, pour un déclenchement au niveau 3 :

- **Part des jours de déclenchement sans feu : 41,2 %** (7 jours sur 17).
- **Part des feux hors des jours de déclenchement : 90,6 %** (126 feux sur 139, partis les jours de niveaux 1 et 2).

La part des feux des seuls jours de danger faible (niveau 1 : 14 feux sur 139, soit 10,1 %) n'est pas retenue comme garde-fou : elle ne dépend pas du seuil choisi, et elle peut augmenter si le dispositif fonctionne, puisque les feux évités les jours de déclenchement font monter la part des autres jours.

Si le groupe retient un autre sens pour "danger élevé" (question Q-1 de `docs/decisions.md`), les valeurs changent : avec un seuil au niveau 2, la part des jours d'alerte sans feu est de 57,9 % (106 jours sur 183). Le seuil actuel du SDIS 2A n'est pas connu (décision 3 de la matrice) : la valeur de référence du seuil réellement appliqué reste à mesurer.

## Test de cohérence

Comment atteindre l'objectif sans faire avancer la stratégie ?

1. **Relever le seuil au maximum.** Au niveau 4, il n'y a plus de jour de déclenchement, donc plus de fausse alerte. C'est pour bloquer ce contournement que le garde-fou porte sur la part des feux hors des jours de déclenchement : elle passerait de 90,6 % à 100 %.
2. **Changer la définition d'un feu.** Compter aussi les feux de végétation ou les très petits feux ferait baisser la part des jours sans feu sans rien changer au dispositif. La définition est figée : feux de type "F" de la BDIFF, toutes surfaces.
3. **Effet du dispositif lui-même.** Si le dispositif renforcé empêche des feux de partir, un jour d'alerte réussi ressemble à une fausse alerte. L'indicateur pénaliserait alors un dispositif efficace. Ce biais ne peut pas être corrigé avec nos données ; il est à signaler à la direction.

## Limites

- Échantillon très court : deux saisons, 17 jours de danger élevé seulement en Corse-du-Sud. Avec la Haute-Corse (9 jours de danger élevé, dont 3 sans feu), on monte à 26 jours, toujours fragile.
- Le niveau 4 n'a jamais été atteint en Corse en 2024 et 2025 : aucun seuil à 4 ne peut être évalué.
- Les feux de 2026 ne sont pas utilisés : l'année n'est pas terminée et la BDIFF ne la publie qu'en 2027.
- La BDIFF ne contient que les feux de forêt ; un départ de feu non enregistré n'est pas visible.
- Le nombre de jours de danger élevé varie beaucoup d'un été à l'autre en Corse-du-Sud : 3 en 2024, 14 en 2025, 18 en 2026. Si l'été 2027 en compte peu, un seul jour pèsera lourd dans la mesure (1 jour sur 4 = 25 points). Le résultat de 2027 sera à lire avec son nombre de jours.
- La mesure d'octobre 2027 dépend de la transmission des feux de la saison 2027 par le SDIS 2A. Sans cette transmission, l'objectif ne pourra être mesuré qu'en 2028, à la publication de la BDIFF.
