# Analyse de la commande - Biolohf Tchatchoua

## 1. Les questions

1. **Où les départs de feu sont-ils les plus fréquents dans le 2A ?**  
   Si les feux se produisent surtout dans certaines zones, le SDIS peut y envoyer plus de moyens. Si les feux sont répartis partout, les moyens doivent être répartis sur tout le département.

2. **À chaque niveau de l’indice, combien de jours ont eu au moins un départ de feu ?**  
   Si beaucoup de jours avec un niveau d’alerte élevé ne donnent aucun feu, le seuil est peut-être trop bas. Si des feux démarrent même avec un niveau faible, il faut peut-être le baisser.

3. **Combien de jours par été dépasseraient les différents seuils possibles ?**  
   Si un seuil entraîne trop de jours de renfort, il coûtera trop cher. Il faut donc choisir un seuil qui permet de protéger les zones à risque sans dépasser le budget.

4. **Le lien entre l’indice et les feux est-il le même en Corse-du-Sud qu’en Haute-Corse et dans le reste de la France ?**  
   Si le lien est semblable, on peut utiliser les données régionales et nationales. Sinon, il faudra calculer un seuil spécifique pour la Corse-du-Sud.

## 2. Les termes inconnus

| Terme | Ce que je pense qu’il veut dire | Ce qu’il faut vérifier |
|---|---|---|
| Météo des forêts | Un indice qui mesure chaque jour le risque d’incendie selon la météo | Quel indice est utilisé, à quelle échelle et quels sont ses niveaux |
| Danger élevé | Un niveau de l’indice au-dessus d’une certaine valeur | Quelle valeur correspond à ce niveau |
| Feu de forêt / départ de feu | Un incendie qui commence dans un espace naturel | Si toutes les sources comptent les mêmes feux |
| Dispositif renforcé | Des patrouilles, du guet et des moyens supplémentaires | Ce que comprend exactement ce dispositif et combien il coûte par jour |
| Département | Le département administratif de la Corse-du-Sud (2A) | Si le périmètre du SDIS est le même que celui du département |

## 3. Les besoins

**La décision à éclairer :** décider où concentrer les moyens du SDIS 2A et à partir de quel niveau de l’indice activer le dispositif renforcé en 2027.

**Ce qui manque dans la commande :**

- Le seuil actuel et le niveau appelé « danger élevé ».
- La définition exacte d’un « feu » : faut-il compter tous les départs, même les petits, ou seulement certains incendies ?
- La période à analyser : combien d’années ou d’étés faut-il étudier ?
- Le budget disponible, pour savoir combien de jours de renfort sont possibles.

## 4. Les données

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Liste des départs de feu avec leur localisation | Un départ de feu | Au moins 10 ans, dont 2026 | Annuelle | Corse-du-Sud, par commune |
| 2 | Indice quotidien et départs de feu | Un jour dans une zone | Au moins 10 ans | Quotidienne | Corse-du-Sud |
| 3 | Indice quotidien par zone | Un jour dans une zone | Au moins 10 étés | Quotidienne | Corse-du-Sud |
| 4 | Indice et départs de feu | Un jour dans un département | Au moins 10 ans | Quotidienne | 2A, 2B et France |