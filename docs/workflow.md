# Méthode de travail

Cette méthode définit les règles de collaboration du groupe sur GitHub. Elle vise à organiser les tâches, suivre les contributions individuelles et conserver un historique clair du projet.

## Tickets

- Une tâche = un ticket (issue), avec un responsable, un domaine et des critères de fin clairement définis.
- Le responsable du domaine concerné vérifie le contenu et valide le travail réalisé.
- Les tickets doivent être suffisamment précis pour que chaque membre comprenne ce qui est attendu.
- Étiquettes suggérées : `organisation`, `sources`, `qualité`, `pipeline`, `documentation`.

## Branches

- La branche `main` contient la version de référence du projet.
- Aucun membre ne pousse directement ses modifications sur `main`.
- Une branche est créée pour chaque ticket, en reprenant son numéro et un résumé de la tâche.
- Exemples : `feat/12-inventaire-sources`, `fix/15-doublons-meteo`, `docs/3-readme`.
- Les branches de travail sont créées à partir de `main` et font l'objet d'une pull request pour intégrer leurs modifications.

## Commits

- Les commits doivent être petits et atomiques : un commit correspond à un changement logique.
- Le message suit le format : `type: résumé court (#ticket)`.
- Exemples :
  - `docs: ajoute le tableau des rôles (#2)`
  - `feat: charge les données Météo des forêts (#14)`
- Chaque membre effectue ses commits avec son propre compte GitHub.
- Les informations Git doivent être configurées individuellement avec `git config user.name` et `git config user.email`.
- Les messages doivent être compréhensibles et permettre de retrouver facilement le ticket associé.

## Pull requests

1. Ouvrir une pull request vers `main`, en précisant le ticket concerné (par exemple : `Closes #12`).
2. La pull request doit traiter un seul sujet et ne contenir que les modifications liées au ticket.
3. Elle doit être relue et approuvée par au moins un autre membre du groupe, idéalement le responsable du domaine concerné.
4. Le responsable du domaine vérifie la conformité du travail avec les critères du ticket.
5. Une personne ne valide pas seule son propre travail : une relecture indépendante est nécessaire.
6. La fusion intervient uniquement après les validations requises.
7. La méthode de fusion retenue est le merge commit (pas de squash), sous réserve de confirmation collective. Voir la décision D-002 dans `docs/decisions.md`.

## Checkpoints

Un checkpoint est réalisé à chaque jalon important du projet. Il peut être matérialisé par un ticket de suivi ou un tag Git, par exemple `checkpoint-1`, `checkpoint-2`, etc.

Chaque checkpoint comprend un court bilan indiquant :

- **Travail réalisé** : tâches et livrables terminés.
- **Travail restant** : tâches qui doivent encore être effectuées.
- **Risques et blocages** : difficultés rencontrées ou points nécessitant une décision.
- **Prochaines étapes** : actions prioritaires avant le prochain jalon.

Les checkpoints permettent au groupe de vérifier régulièrement son avancement et de détecter les retards ou difficultés.