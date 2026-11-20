# 🔥 Feux de forêt – Corse

## Présentation du projet

Ce projet vise à développer un outil d'aide à la décision destiné au SDIS 2A (Service départemental d'incendie et de secours de Corse-du-Sud), dans le cadre de la préparation de la saison des feux de forêt 2027.

L'objectif est d'exploiter différentes sources de données afin de mieux comprendre les risques d'incendie, d'identifier les zones les plus exposées et d'accompagner la préparation opérationnelle.

## Périmètre géographique

- Corse-du-Sud (2A)
- Haute-Corse (2B)
- Comparaison avec le reste du territoire national.

## Organisation de l'équipe

| Rôle | Responsable | Missions |
|---|---|---|
| Chef de projet | Saran DIABAGATE | Coordination, dépôt, tickets et décisions |
| Responsable sources | TCHATCHOUA BIOLOHF | Inventaire et documentation des sources |
| Responsable qualité et conformité | PHILIPPE Ahmed| Qualité des données, tests et conformité |
| Responsable pipeline et modèle | TOURE Arouna | Chargement, consolidation et entrepôt |

## Organisation du dépôt

- `docs/` : documentation du projet.
- `docs/analyse/` : analyses individuelles de la commande.
- `docs/sources/` : documentation des sources.
- `data/` : organisation des données.
- `data/raw/` : couche bronze, copie exacte des fichiers sources, jamais modifiée (voir `docs/donnees-brutes.md`).
- `src/` : code source.
- `tests/` : tests du projet.

## Sources et licences

Les analyses de ce dépôt sont faites à partir de la base BDIFF (Base de données sur les incendies de forêts en France), https://bdiff.agriculture.gouv.fr. Droits de reproduction réservés et strictement limités. Les exports de la BDIFF sont conservés sans modification dans `data/raw/` ; tout ce qui est calculé ensuite est fait à partir de la base BDIFF et n'est pas la base de la BDIFF.

Les niveaux de danger viennent des Archives de la Météo des forêts de Météo-France, publiées sur data.gouv.fr sous Licence Ouverte 2.0 (https://www.etalab.gouv.fr/licence-ouverte-open-licence).

Procédure d'obtention, vérification des fichiers et impact des mises à jour : `docs/donnees-brutes.md`.

## Méthode de travail

Le groupe utilise Git et GitHub pour organiser le travail :

- Une branche par fonctionnalité ou tâche.
- Des commits réguliers et explicites.
- Des tickets pour suivre les tâches.
- Des Pull Requests pour relire et valider les modifications.
- Un journal des décisions pour conserver les choix importants.
