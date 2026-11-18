# Journal des décisions — Corse

Une entrée par décision, la plus récente en bas. On ne supprime jamais une entrée : si une décision change, on ajoute une nouvelle entrée qui remplace l'ancienne et on l'indique.

Dernière mise à jour : 2026-11-17 (D-005, D-006 ajoutées)

## Modèle d'entrée

### D-000 · Titre court
- **Date :** AAAA-MM-JJ
- **Décidé par :** Prénom(s)
- **Contexte :** quel problème ou quelle question ?
- **Options envisagées :** A, B, C
- **Décision :** ce qui est retenu
- **Raison :** pourquoi
- **Conséquences :** ce que ça change pour le projet
- **Liens :** tickets, pull requests, glossaire

---

## Décisions prises

### D-001 · Répartition des rôles
- **Date :** 2026-11-16
- **Décidé par :** Saran DIABAGATE, Biolohf TCHATCHOUA, Ahmed PHILIPPE, Arouna TOURE
- **Contexte :** l'énoncé impose quatre rôles. À quatre, chaque membre en prend un.
- **Options envisagées :** répartition des quatre rôles entre les membres selon les responsabilités nécessaires au projet.
- **Décision :**
  - Chef de projet : Saran DIABAGATE (dépôt, tickets, checkpoints, journal des décisions)
  - Responsable sources : Biolohf TCHATCHOUA (inventaire, fiches d'identité, matrice questions × sources)
  - Responsable qualité et conformité : Ahmed PHILIPPE (règles de qualité, tests, données personnelles)
  - Responsable pipeline et modèle : Arouna TOURE (chargement, consolidation, entrepôt)
- **Raison :** chaque membre a accepté le rôle indiqué ci-dessus. Les motivations de chacun peuvent être ajoutées par la personne concernée, sans reconstruire de justification.
- **Conséquences :** chaque responsable relit et valide les tickets de son domaine. Tout changement de rôle sera écrit dans ce journal, avec la raison.
- **Liens :** README, ticket #4

### D-002 · Méthode de travail
- **Date :** 2026-11-17
- **Décidé par :** Saran DIABAGATE (chef de projet), à confirmer par le groupe
- **Contexte :** l'énoncé évalue l'organisation du groupe : tickets, branches et commits atomiques, historique lisible.
- **Options envisagées :** fusion par « merge commit », par « squash », ou par « rebase ».
- **Décision :**
  - un ticket par tâche, une branche par ticket (`docs/8-journal-decisions`, `analyse/commande-prenom`, etc.) ;
  - des commits petits, un par changement logique, avec le numéro du ticket dans le message ;
  - tout passe par une pull request relue par au moins un autre membre, puis fusionnée dans `main` ;
  - fusion par **merge commit** (pas de squash), **proposition à confirmer par les quatre membres**.
- **Raison :** le merge commit garde chaque commit et montre qui a fait quoi, ce qui répond à la consigne sur la contribution individuelle visible dans l'historique. La consigne du dépôt ne précise pas de méthode de fusion.
- **Conséquences :** on ne pousse jamais directement sur `main`. Chaque pull request ne traite qu'un sujet. Si le groupe ou un enseignant demande une autre méthode, une nouvelle entrée remplacera celle-ci.
- **Liens :** ticket #8, pull request #3

### D-003 · Glossaire version 0
- **Date :** 2026-11-17
- **Décidé par :** Saran DIABAGATE (auteure de la pull request).
- **Relu et approuvé par :** Biolohf TCHATCHOUA et Arouna TOURE.
- **Relecture demandée, non rendue :** Ahmed PHILIPPE.
- **Contexte :** le glossaire est à rendre en fin de S1, avec au moins 8 termes, par pull request.
- **Décision :** fusionner dans `main` un glossaire de 23 termes (pull request #3, effectivement fusionnée), construit à partir des termes inconnus des 4 analyses individuelles. Statut « à vérifier » pour presque tous, car aucune définition n'est encore confirmée dans la documentation des sources.
- **Raison :** le document du cours demande de ne pas gommer les divergences et de garder le statut « à vérifier » tant que la source n'a pas confirmé.
- **Conséquences :** toute modification du glossaire passe par un ticket et une pull request. Les divergences ouvertes sont listées ci-dessous.
- **Liens :** ticket #2, pull request #3 (fusionnée), `docs/glossaire.md`

### D-004 · Questions communes du groupe
- **Date :** 2026-11-17
- **Statut :** proposition de Saran DIABAGATE, **à confirmer par les trois autres membres** (relecture de la pull request #33).
- **Contexte :** les quatre analyses individuelles posent des questions différentes (4, 4, 6 et 10 questions). Il faut un socle commun pour l'inventaire des sources et la matrice questions × sources. Les analyses individuelles ne sont plus modifiées.
- **Options envisagées :**
  - A. garder 4 questions communes (répartition géographique des feux, lien entre niveau de danger et feux, nombre de jours selon le seuil, comparaison Corse-du-Sud / Haute-Corse / France) ;
  - B. ajouter une 5e question : « À quelles périodes de la saison les feux sont-ils les plus fréquents ? ». Elle a été examinée, puis écartée du socle principal, parce qu'elle utilise les mêmes données que la question 1.
- **Décision proposée :** option A, **4 questions communes** :
  1. Où se concentrent les départs de feu en Corse-du-Sud ?
  2. À chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu ?
  3. Combien de jours par été chaque seuil envisagé aurait-il déclenché ?
  4. Le lien entre l'indice et les feux est-il le même en Haute-Corse et dans le reste de la France ?
- **Raison :** ce sont les questions que les quatre analyses ont en commun, et chacune change une décision de la direction. La question sur les périodes de la saison utilise les mêmes données que la question 1 : on conserve la date de chaque feu pour pouvoir y répondre plus tard.
- **Conséquences :** ces questions sont dans `docs/analyse/commande-groupe.md` et servent de base à `docs/sources/inventaire.md` et à la matrice questions × sources. Le coût journalier du dispositif renforcé (question 3) n'a aucune source ouverte : à demander au SDIS.
- **Liens :** `docs/analyse/commande-groupe.md`, glossaire

### D-005 · Répartition des sources de l'exercice 2
- **Date :** 2026-11-17
- **Décidé par :** Saran DIABAGATE (chef de projet), à confirmer par le groupe
- **Contexte :** l'exercice 2 demande une fiche d'identité par source, avec un commit par fiche sur sa propre branche, puis une pull request.
- **Options envisagées :** une branche et un ticket par source, ou une branche et un ticket par personne.
- **Décision :** une branche et un ticket par personne, avec une relecture par le responsable du domaine avant validation :
  - Arouna TOURE : Archives de la Météo des forêts et BDIFF (ticket #26) ; relecture prévue par Biolohf TCHATCHOUA.
  - Biolohf TCHATCHOUA : Interventions SDIS et Prométhée (ticket #27) ; relecture prévue par Saran DIABAGATE.
  - Ahmed PHILIPPE : BD Forêt et Corine Land Cover (ticket #28) ; relecture prévue par Biolohf TCHATCHOUA.
  - Saran DIABAGATE : Admin Express (ticket #29) ; relecture prévue par Biolohf TCHATCHOUA.
  - Inventaire des sources (ticket #19) : rédigé par Saran DIABAGATE et relu par Biolohf TCHATCHOUA.
  - **Statut des relectures :** les relectures prévues ne sont pas considérées comme des validations tant qu'elles n'ont pas été effectivement réalisées et confirmées.
- **Raison :** Tchatchoua, responsable des sources, prend les deux sources de feux. Ahmed, côté qualité, prend le contexte forestier. Admin Express est la source la plus simple : elle donne la clé de jointure (communes et départements), ce qui laisse du temps à la cheffe de projet.
- **Conséquences :** une valeur qu'on n'a pas pu vérifier s'écrit « non vérifiée », avec la raison ; une valeur supposée compte comme une erreur. Une PR qui contient un fichier d'un autre ticket est corrigée avant d'être fusionnée.
- **Liens :** tickets #19, #26, #27, #28, #29 ; pull requests #30, #31, #34

### D-006 · Analyses individuelles dans `main`
- **Date :** 2026-11-17
- **Décidé par :** Saran DIABAGATE (cheffe de projet), à confirmer par le groupe
- **Contexte :** la consigne du dépôt dit que tout le travail doit y passer et que la contribution de chacun doit être visible dans l'historique.
- **Options envisagées :** laisser les analyses individuelles sur leurs branches, ou les fusionner dans `main`.
- **Décision :** fusionner les quatre analyses individuelles dans `main` (`docs/analyse/commande-prenom-nom.md`), par merge commit, après relecture par un autre membre. L'analyse de groupe (`commande-groupe.md`) est un fichier séparé.
- **Raison :** les analyses individuelles montrent qui a fait quoi ; l'analyse de groupe est le résultat commun.
- **Conséquences :** les analyses individuelles sont considérées comme finalisées après leur fusion. Toute correction ultérieure devra passer par un ticket et une pull request, afin de conserver la trace de la modification dans l'historique du dépôt.
- **Liens :** tickets #15 à #18 ; pull requests #1, #24, #25, #35

---

## Décisions en attente de confirmation

Ces entrées sont des propositions de la cheffe de projet, pas encore validées par tout le groupe. Quand un membre confirme, on le note ici avec la date.

| Sujet | Entrée | Personnes concernées | Statut |
|---|---|---|---|
| Méthode de fusion par merge commit | D-002 | Les 4 membres | À confirmer |
| Questions communes du groupe | D-004 | Les 4 membres | À confirmer (pull request #33) |
| Validation du glossaire | D-003 | Ahmed PHILIPPE | Relecture demandée, non rendue |
| Répartition des sources de l'exercice 2 | D-005 | Les 4 membres | À confirmer |
| Analyses individuelles dans `main` | D-006 | Les 4 membres | À confirmer |

---

## Questions ouvertes (à décider par le groupe)

Chaque décision prise ici devra aussi mettre à jour la fiche du glossaire concernée.

| # | Question | Origine | Fiche du glossaire |
|---|---|---|---|
| Q-1 | Que veut dire « danger élevé » : le niveau 3 (orange) seul, ou les niveaux 3 et 4 ? | Tchatchoua, Arouna, Ahmed | Danger élevé |
| Q-2 | L'IFM mesure-t-il un danger météo (Arouna) ou un risque d'éclosion (Ahmed) ? | Arouna, Ahmed | IFM, Danger et risque |
| Q-3 | Qu'appelle-t-on « un feu » : départ de feu, feu de forêt, feu de végétation, intervention ? Quel seuil de surface ? | Saran, Arouna, Tchatchoua | Feu de forêt, Départ de feu |
| Q-4 | Quelle prévision utiliser : J+1 ou J+2 ? | Arouna | Météo des forêts |
| Q-5 | Le périmètre du SDIS 2A est-il le même que celui du département 2A ? | Tchatchoua | Département, SDIS 2A |
| Q-6 | Quelle période de référence pour comparer les saisons (archives depuis juin 2024, feux depuis 2006 ou 1973) ? | Saran, Arouna | Météo des forêts, BDIFF, Prométhée |