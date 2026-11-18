# Matrice questions × sources (v0)

Tenue par : Biolohf Tchatchoua (responsable sources)

Version 0. Les cellules « À vérifier » seront mises à jour quand les fiches correspondantes auront été relues et que des fichiers auront été ouverts.

## Questions

Les questions viennent de l'analyse de la commande de Biolohf Tchatchoua. Ajouter les questions des autres membres une fois les numéros alignés.

| N° | Question | Décision de la direction |
|---|---|---|
| Q1 | Où les départs de feu se concentrent-ils dans le 2A ? | Où placer les moyens |
| Q2 | À chaque niveau de l'indice, quelle part des jours compte au moins un départ de feu ? | Relever ou abaisser le seuil |
| Q3 | Combien de jours par été dépasseraient chaque seuil envisagé ? | Dimensionner le dispositif renforcé selon le budget |
| Q4 | Le lien entre l'indice et les feux est-il le même en 2A, en 2B et en France ? | Utiliser ou non des références nationales |

## Matrice

Légende : **Oui** (répond à la question), **Partiel** (répond en partie ou en appoint), **Non**, **À vérifier** (fiche non lue ou fichier non ouvert).

| Source | Explorée par | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|---|
| Interventions SDIS | B. Tchatchoua | Non | Non | Non | Partiel |
| Prométhée | B. Tchatchoua | À vérifier | À vérifier | Non | Partiel |
| BDIFF | A. Touré | À vérifier | À vérifier | Non | À vérifier |
| Archives Météo des forêts | A. Touré | Non | Partiel | Partiel | Partiel |
| BD Forêt | A. Philippe | Partiel | Non | Non | Partiel |
| Corine Land Cover | A. Philippe | Partiel | Non | Non | Partiel |
| Admin Express | S. Diabagate | Partiel | Non | Non | Non |

## Justification des cellules

- **Interventions SDIS** (fichiers ouverts) : une ligne par département et par année, avec des totaux, sans date ni commune. Q1 à Q3 impossibles. Q4 en partie : comparaison annuelle entre départements, « Feux de végétations » disponible en 2008, 2009 et 2014 à 2024.
- **Prométhée** (fiche en cours, aucun export ouvert) : Q1 et Q2 dépendent d'une localisation et d'une date qu'on n'a pas vérifiées. Q4 en partie seulement, car la base couvre la zone méditerranéenne et non la France entière.
- **BDIFF** (fiche d'Arouna à relire) : Q1, Q2 et Q4 dépendent de la localisation, de la date et de la couverture nationale. Le jeu data.gouv.fr « Données feux de forêt en Corse du Sud » annonce des points d'éclosion depuis 1973 : à confirmer en ouvrant un fichier.
- **Archives Météo des forêts** (fiche d'Arouna à relire) : indice par département, niveaux 1 à 4, saison de juin à septembre, archives annoncées depuis 2024 sur la page data.gouv.fr. Q2 et Q3 en partie : trop peu d'étés. Q4 en partie : couverture nationale à confirmer.
- **BD Forêt** et **Corine Land Cover** (fiches de la PR #40) : donnent le contexte de végétation, pas de réponse seule. Corine a une maille minimale de 25 ha, trop grossière pour une commune corse. Utiles à Q4 en appoint, à grain égal pour Corine.
- **Admin Express** : référentiel des communes, clé de jointure. Ne répond à aucune question seule.

## Analyse d'écart : ce qui manque

| Besoin | Source trouvée ? | Constat |
|---|---|---|
| Indice quotidien sur plusieurs années (Q2, Q3) | Partielle | Archives Météo des forêts depuis 2024 seulement, à confirmer |
| Départs de feu avec date et localisation (Q1, Q2) | À confirmer | BDIFF et Prométhée à vérifier |
| Seuil actuel de déclenchement | Non | Information interne au SDIS 2A |
| Budget et coût par jour du dispositif renforcé (Q3) | Non | Information interne au SDIS 2A |

## Décision face à une source manquante (propositions à valider par le groupe)

1. Demander au SDIS 2A le seuil actuel, le budget et le coût par jour du dispositif.
2. Pour l'indice sur une période plus longue, examiner l'indice forêt météo de Copernicus et EFFIS, tous deux dans la liste du défi, et noter dans la fiche si leur emploi comme équivalent (proxy) est acceptable.
3. Pour les feux, choisir une source de référence entre BDIFF, Prométhée et interventions SDIS une fois les fiches complètes. Décision à consigner dans le journal des décisions.