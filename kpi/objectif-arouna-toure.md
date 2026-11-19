# Objectif : Arouna Touré

- **Séance :** UE01.B, S1 (de la question analytique à l'objectif)
- **Date :** 2026-11-18
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
| Objectif SMART | D'ici la fin de l'été 2027, faire passer de 41,2 % à [b %] la part des jours de danger élevé (`niveau_j1` supérieur ou égal à 3) sans aucun départ de feu en Corse-du-Sud, sans augmenter la part des feux qui partent les jours de danger faible (`niveau_j1` = 1), aujourd'hui de 10,1 %. | |

## L'objectif SMART, critère par critère

| Critère | Contenu |
|---|---|
| Spécifique | Les jours de danger élevé en Corse-du-Sud (2A), c'est-à-dire les jours où la prévision J+1 de la Météo des forêts vaut 3 ou plus, et parmi eux ceux où aucun feu de forêt n'est enregistré dans la BDIFF. |
| Mesurable | La part passe de 41,2 % à [b %]. Elle se calcule en croisant `niveau_j1` (rapporté au lendemain de la publication) et la date de première alerte des feux BDIFF. |
| Atteignable | [b %] est fixée avec la direction du SDIS 2A une fois la situation de référence présentée, pas avant. |
| Réaliste | La condition "sans augmenter la part des feux les jours de danger faible" empêche de gagner en relevant simplement le seuil : au niveau 4, aucun jour ne serait déclenché en 2024 et 2025, et tous les feux tomberaient sous le seuil. |
| Temporel | D'ici la fin de la saison 2027 (fin septembre 2027). |

## Situation de référence

Mesurée sur les deux saisons communes aux deux sources (jours du 4 juin au 1er octobre 2024 et 2025, soit 240 jours ; 139 feux de forêt en Corse-du-Sud ces jours-là).

| Niveau `niveau_j1` | Jours | Jours avec au moins un feu | Part des jours avec feu | Feux |
|---|---|---|---|---|
| 1 (faible) | 57 | 10 | 17,5 % | 14 |
| 2 (modéré) | 166 | 67 | 40,4 % | 112 |
| 3 (élevé) | 17 | 10 | 58,8 % | 13 |
| 4 (très élevé) | 0 | 0 | sans objet | 0 |

Valeurs de départ de l'objectif :

- **Part des jours de danger élevé sans feu : 41,2 %** (7 jours sur 17).
- **Part des feux les jours de danger faible : 10,1 %** (14 feux sur 139).

Si le groupe retient un autre sens pour "danger élevé" (question Q-1 de `docs/decisions.md`), les valeurs changent : avec un seuil au niveau 2, la part des jours d'alerte sans feu est de 57,9 % (106 jours sur 183). Le seuil actuel du SDIS 2A n'est pas connu (décision 3 de la matrice) : la valeur de référence du seuil réellement appliqué reste à mesurer.

## Test de cohérence

Comment atteindre l'objectif sans faire avancer la stratégie ?

1. **Relever le seuil au maximum.** Au niveau 4, il n'y a plus de jour de danger élevé, donc plus de fausse alerte. La condition sur les feux des jours de danger faible bloque ce contournement seulement en partie : il faut aussi suivre la part des feux qui partent hors des jours déclenchés.
2. **Changer la définition d'un feu.** Compter aussi les feux de végétation ou les très petits feux ferait baisser la part des jours sans feu sans rien changer au dispositif. La définition est figée : feux de type "F" de la BDIFF, toutes surfaces.
3. **Effet du dispositif lui-même.** Si le dispositif renforcé empêche des feux de partir, un jour d'alerte réussi ressemble à une fausse alerte. L'indicateur pénaliserait alors un dispositif efficace. Ce biais ne peut pas être corrigé avec nos données ; il est à signaler à la direction.

## Limites

- Échantillon très court : deux saisons, 17 jours de danger élevé seulement en Corse-du-Sud. Avec la Haute-Corse (9 jours de danger élevé, dont 3 sans feu), on monte à 26 jours, toujours fragile.
- Le niveau 4 n'a jamais été atteint en Corse en 2024 et 2025 : aucun seuil à 4 ne peut être évalué.
- Les feux de 2026 ne sont pas utilisés : l'année n'est pas terminée et la BDIFF ne la publie qu'en 2027.
- La BDIFF ne contient que les feux de forêt ; un départ de feu non enregistré n'est pas visible.
