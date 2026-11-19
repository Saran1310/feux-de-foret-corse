# Objectif - Biolohf Tchatchoua

- **Séance :** UE01.B, S1 (de la question analytique à l'objectif)
- **Question travaillée :** Q3 de la matrice du groupe
- **Données utilisées :** Météo des forêts (`niveau_j1`, saisons 2024 et 2025) et BDIFF (feux du 2A, `Date de première alerte`), d'après les profils `docs/qualite/profil-mdf.md` et `docs/qualite/profil-bdiff.md`

## 1. Diagnostic : les quatre niveaux

| Niveau | Contenu pour le SDIS 2A | Statut | Pièce |
|---|---|---|---|
| Stratégie | Préparer la saison des feux 2027 en concentrant les moyens humains et financiers là et quand ils servent le plus | établi | Commande : « où faut-il concentrer nos moyens » |
| Enjeu | Le budget ne permet pas de renforcer le dispositif sur tout l'été ; le seuil actuel se trompe dans les deux sens (alertes sans feu, feux sans alerte) | établi | Commande : budget limité, remarques des chefs de centre |
| Enjeu | Le seuil actuel déclenche plus de jours que le budget ne le permet | supposé | Valeur du seuil actuel et budget inconnus (décision 3 de la matrice) |
| Objectif | Choisir un seuil qui couvre l'essentiel des feux sans dépasser le nombre de jours finançables | supposé | La commande ne formule pas d'objectif chiffré |
| Action | Déclencher le dispositif renforcé (patrouilles, guet) à partir d'un niveau de la Météo des forêts | établi | Commande : « à partir de quel niveau de la Météo des forêts » |

## 2. Hypothèse stratégique et verdict

**Hypothèse (niveau Enjeu, supposé).** Le seuil actuel déclenche plus de jours que le budget du SDIS 2A ne permet d'en financer.

- **Pièce qui la fonde :** la commande dit que le budget ne permet pas de renforcer le dispositif sur tout le département pendant tout l'été, et que l'indice annonce souvent un danger élevé sans feu.
- **Confirmée si :** le nombre de jours déclenchés par le seuil actuel dépasse le nombre de jours que le budget finance.
- **Infirmée si :** il est inférieur ou égal.

**Verdict : les données ne permettent pas de trancher.** Le seuil actuel et le budget ne sont connus d'aucune source (décision 3 de la matrice). C'est une limite de l'objectif : [N] reste à fixer avec le SDIS 2A.

## 3. Question analytique et décision

- **Question (Q3) :** combien de jours par été chaque seuil envisagé aurait-il déclenché, et quelle part des feux ces jours auraient-ils couverte ?
- **Décision que la réponse nourrit :** quel seuil de `niveau_j1` retenir pour le dispositif renforcé, dans la limite du budget.

## 4. Trois formulations

| Formulation | Texte | Pourquoi ce n'est pas encore suffisant |
|---|---|---|
| Action | Choisir le seuil de `niveau_j1` à partir duquel déclencher le dispositif renforcé. | C'est ce que l'on fait, pas le résultat attendu. Rien ne dit quand ce sera réussi. |
| Objectif | Déclencher le dispositif renforcé sur les jours qui couvrent l'essentiel des feux, dans la limite du budget. | Le résultat est nommé, mais sans valeur de départ, sans cible, sans échéance. |
| Objectif SMART | D'ici la fin de l'été 2027, retenir un seuil de `niveau_j1` qui couvre au moins [80 %] des feux du 2A survenus de juin à septembre, sans déclencher plus de [92] jours par été. | |

[80 %] et [92] sont des valeurs provisoires, à valider avec le SDIS 2A. Voir la section 5.

## 5. L'objectif SMART, critère par critère

| Critère | Contenu |
|---|---|
| Spécifique | Un seuil de `niveau_j1` (niveau 2 ou 3 d'après les saisons observées) pour le dispositif renforcé en Corse-du-Sud. Un feu est couvert s'il part un jour où `niveau_j1`, rapporté au lendemain de sa publication, est supérieur ou égal au seuil. |
| Mesurable | Couverture = feux du 2A survenus un jour déclenché / feux du 2A de juin à septembre. Jours déclenchés = nombre de jours par été où `niveau_j1` atteint le seuil. Les deux se calculent en croisant la Météo des forêts et la date de première alerte des feux. |
| Atteignable | [80 %] et [92] jours ne sont pas fixés seuls : ils le sont avec le SDIS 2A, une fois le budget connu. Les niveaux de l'indice étant peu nombreux, il n'existe pas de seuil intermédiaire : toute cible de couverture entre 10 % et 89 % impose le niveau 2, donc environ 92 jours par été. |
| Réaliste | Les deux conditions se bloquent mutuellement : sans condition sur le nombre de jours, on déclencherait tous les jours ; sans condition de couverture, on choisirait le niveau 4 (zéro jour). Si le budget est inférieur à environ 92 jours, l'objectif n'est pas atteignable par le seuil seul. |
| Temporel | D'ici la fin de l'été 2027 (fin septembre 2027). Mesure en octobre 2027 avec les feux transmis par le SDIS 2A, à confirmer avec la BDIFF quand elle publiera 2027 (en 2028). |

## 6. Situation de référence

Mesurée sur les deux saisons communes aux deux sources (4 juin au 1er octobre 2024 et 2025, soit 240 jours ; 139 feux de forêt en Corse-du-Sud).

| Seuil de `niveau_j1` | Jours déclenchés (2 saisons) | Par été | Part des jours | Feux couverts | Part des feux |
|---|---|---|---|---|---|
| niveau 2 ou plus | 183 | environ 91,5 | 76,3 % | 125 | 89,9 % |
| niveau 3 ou plus | 17 | environ 8,5 | 7,1 % | 13 | 9,4 % |
| niveau 4 | 0 | 0 | 0 % | 0 | 0 % |

Ces valeurs sont calculées à partir des niveaux 1 à 4 (57, 166, 17 et 0 jours ; 14, 112, 13 et 0 feux) du profil de la Météo des forêts croisé avec la BDIFF. À contrôler dans `profil-mdf.md` et `profil-bdiff.md`.

Valeurs à mesurer, non disponibles aujourd'hui : le seuil réellement appliqué par le SDIS 2A, le nombre de jours finançables par été et le coût par jour du dispositif.

## 7. Test de cohérence

Comment atteindre l'objectif sans faire avancer la stratégie ?

1. **Déclencher tous les jours.** La couverture serait de 100 %, mais la condition sur le nombre de jours (92 par été) l'interdit.
2. **Relever le seuil au niveau 4.** Zéro jour déclenché respecte la limite de jours, mais la couverture tombe à 0 %. La condition de couverture l'interdit.
3. **Élargir la définition d'un feu** (compter aussi les très petits feux) pour gonfler la couverture. La définition d'un feu est figée dans le glossaire du groupe et ne doit pas changer pour atteindre la cible.
4. **Effet du dispositif lui-même.** S'il empêche des feux de partir, la couverture mesurée baisse alors que le dispositif fonctionne. Ce biais ne peut pas être corrigé avec nos données : il est à signaler à la direction.

## 8. Limites

- Échantillon court : deux saisons et 17 jours seulement au niveau 3. Un jour de plus ou de moins change beaucoup les pourcentages.
- Le niveau 4 n'a jamais été atteint en Corse-du-Sud en 2024 et 2025 : aucun seuil au niveau 4 ne peut être évalué.
- Seuls les feux de juin à septembre sont couverts : 46,5 % des feux du 2A partent hors de cette période, où la Météo des forêts n'est pas publiée.
- Les feux de 2026 sont exclus (décision du groupe, ticket #61).
- Le seuil actuel et le budget sont inconnus : [N] et [C %] sont des valeurs provisoires.
- La BDIFF ne contient que les feux enregistrés : un départ de feu non enregistré n'est pas visible.