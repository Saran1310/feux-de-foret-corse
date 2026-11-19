# Journal des décisions (Corse)

Une entrée par décision, la plus récente en bas. On ne supprime jamais une entrée : si une décision change, on ajoute une nouvelle entrée qui remplace l'ancienne et on l'indique.

Dernière mise à jour : 2026-11-19 (D-009 à D-013 ajoutées, D-009 mise à jour)

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
  - **Statut des relectures :** une relecture prévue ne vaut validation qu'une fois faite et confirmée.
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
- **Conséquences :** les analyses individuelles sont considérées comme finalisées après leur fusion. Toute correction ultérieure devra passer par un ticket et une pull request, pour garder la trace dans l'historique du dépôt.
- **Liens :** tickets #15 à #18 ; pull requests #1, #24, #25, #35

### D-007 · Millésime retenu pour CORINE Land Cover
- **Date :** 2026-11-18
- **Décidé par :** Ahmed PHILIPPE (proposition), à confirmer par le groupe
- **Contexte :** CORINE Land Cover existe en plusieurs millésimes (1990, 2000, 2006, 2012, 2018). La page data.gouv.fr ne propose que 1990 à 2012 ; le millésime 2018 est publié par le producteur français (SDES).
- **Options envisagées :** A. prendre 2012 sur data.gouv.fr ; B. prendre 2018 sur le site du SDES ; C. mélanger plusieurs millésimes.
- **Décision :** option B, un seul millésime : **2018**, téléchargé chez le SDES. Le millésime est conservé comme colonne dans l'entrepôt.
- **Raison :** c'est le plus proche des feux étudiés (2024-2026), et un seul millésime évite de mélanger des époques.
- **Conséquences :** l'occupation du sol décrite a 6 à 8 ans de retard sur les feux ; à signaler dans la restitution. À réviser si CLC+ (nouvelle génération) est publié avant le rendu.
- **Liens :** tickets #28 et #43, pull request #40, `docs/sources/fiche-corine-land-cover.md`

### D-008 · Ne pas additionner CORINE Land Cover et BD Forêt
- **Date :** 2026-11-18
- **Décidé par :** Ahmed PHILIPPE (proposition), à confirmer par le groupe
- **Contexte :** CORINE Land Cover et la BD Forêt mesurent toutes deux la surface boisée, avec des règles différentes (maille de 25 ha contre 0,5 ha, millésime 2018 contre 2007-2018 selon le département).
- **Options envisagées :** A. additionner ou fusionner les deux ; B. retenir une seule source par usage.
- **Décision :** option B. Pour la surface boisée par commune (Q1), la **BD Forêt** ; pour comparer les départements (Q4), **CORINE Land Cover**, homogène dans toute la France. Les deux ne sont jamais additionnées.
- **Raison :** additionner deux mesures de la même chose compte deux fois les mêmes surfaces, et le total ne correspond à aucune des deux définitions.
- **Conséquences :** chaque indicateur de surface cite sa source ; un indicateur communal et un indicateur départemental de surface boisée ne sont pas comparables entre eux.
- **Liens :** tickets #28 et #43, pull request #40, `docs/sources/fiche-bd-foret.md`, `docs/sources/fiche-corine-land-cover.md`

### D-009 · Feux de 2026 exclus de l'analyse
- **Date :** 2026-11-18
- **Décidé par :** Arouna TOURE (proposition, commentaire sur la pull request #46) et Saran DIABAGATE (cheffe de projet) ; formulation écrite par Biolohf TCHATCHOUA dans la matrice
- **Contexte :** les feux de la saison 2026 manquent dans la BDIFF (diffusion publique jusqu'à l'année antérieure). La matrice disait d'abord « collecter, à défaut approximer » : demander ces feux au SDIS 2A, et utiliser la BDIFF 2006-2025 sans réponse.
- **Options envisagées :** A. collecter les feux de 2026 auprès du SDIS ; B. approximer avec la BDIFF 2006-2025, sans 2026 ; C. renoncer à 2026 (position d'Ahmed PHILIPPE dans sa relecture de la pull request #46).
- **Décision :** option B, **approximer**. La BDIFF 2006-2025 sert de base, les feux de 2026 sont exclus. L'exclusion ne concerne que les feux : la saison 2026 de la Météo des forêts est complète (bulletins du 28 mai au 5 octobre 2026) et reste utilisée.
- **Raison :** l'année 2026 n'est pas terminée, et 46,5 % des feux du 2A ont lieu hors de juin-septembre (fiche BDIFF) : il manque donc les feux d'octobre à décembre. Des chiffres transmis par le SDIS seraient provisoires et ne se comparent pas aux 20 années complètes : même collectés, ils ne combleraient pas le manque. Ahmed y voit un renoncement à 2026. Nous retenons « approximer » parce que Q1 reçoit une réponse, approchée par 2006-2025 ; seules les données de 2026 sont écartées.
- **Conséquences :** les évolutions de 2026 ne sont pas visibles, ce qu'il faudra écrire dans la restitution. Les sections 5 individuelles sont mises en accord avec cette décision (ticket #61) : la matrice (#64), la section de Saran DIABAGATE (#62) et celle de Biolohf TCHATCHOUA (#59) sont fusionnées ; celle d'Ahmed PHILIPPE (#48) est en cours de relecture.
- **Liens :** ticket #61, pull requests #46, #48, #59, #62 et #64, `docs/sources/matrice.md` (décision 1)

### D-010 · Seuil de déclenchement : approximer avec deux saisons communes
- **Date :** 2026-11-18
- **Décidé par :** Biolohf TCHATCHOUA (matrice, pull request #46), relue par Arouna TOURE
- **Contexte :** la question Q2 demande la part des jours avec au moins un feu à chaque niveau de la Météo des forêts. L'historique des niveaux couvre trois saisons : juin-septembre 2024 et 2025, 28 mai-5 octobre 2026, et seuls 139 feux du 2A tombent dans la période commune à la BDIFF (juin-septembre 2024 et 2025).
- **Options envisagées :** collecter un historique plus long (aucune source ouverte identifiée) ; approximer avec la période commune ; renoncer à la question.
- **Décision :** **approximer** : croiser `niveau_j1` (prévision J+1) avec les feux de la BDIFF sur juin-septembre 2024 et 2025, et compléter avec le 2B (Q4).
- **Raison :** c'est le seul croisement possible avec les sources ouvertes. On prend `niveau_j1` parce que c'est la prévision qui déclenche le dispositif. Ce choix est provisoire tant que la question ouverte Q-4 (J+1 ou J+2) n'est pas tranchée par le groupe.
- **Conséquences :** avec 139 feux pour le 2A, les taux sont fragiles : le résultat sera présenté comme une tendance exploratoire, pas comme un seuil opérationnel. Les 46,5 % de feux hors saison restent hors du champ de l'indice. La colonne `date` de la Météo des forêts est une date de publication : il faut associer chaque feu au bulletin publié la veille (décalage documenté dans la fiche Météo des forêts, points 3 et 5).
- **Liens :** ticket #20, pull request #46, `docs/sources/matrice.md` (décision 2), `docs/sources/fiche-meteo-des-forets.md`

### D-011 · Coût journalier et seuil actuel : à demander au SDIS 2A
- **Date :** 2026-11-18
- **Décidé par :** Biolohf TCHATCHOUA (matrice, pull request #46), relue par Arouna TOURE
- **Contexte :** la question Q3 demande combien de jours par été chaque seuil aurait déclenché, et à quel coût. Aucune source ouverte ne contient le coût journalier du dispositif renforcé ni le seuil actuellement utilisé (voir D-004).
- **Options envisagées :** collecter auprès du SDIS ; approximer le coût ; renoncer au coût.
- **Décision :** **collecter** le coût journalier et le seuil actuel auprès du SDIS 2A. Le nombre de jours par seuil se calcule déjà avec la Météo des forêts.
- **Raison :** seul le SDIS 2A détient ces informations.
- **Conséquences :** dépend d'une réponse du SDIS avant le 11 décembre ; sans elle, le résultat est exprimé en jours et non en euros.
- **Liens :** ticket #20, `docs/sources/matrice.md` (décision 3)

### D-012 · Comparaison 2A, 2B et France : approximer avec la Haute-Corse
- **Date :** 2026-11-18
- **Décidé par :** Biolohf TCHATCHOUA (matrice, pull request #64)
- **Contexte :** la matrice proposait d'abord de vérifier la présence du 2B dans la Météo des forêts et d'exporter la BDIFF pour le 2B, puis d'approximer (les cellules « inconnu » appellent une vérification avant toute décision).
- **Options envisagées :** vérifier puis approximer ; renoncer à la comparaison avec la Haute-Corse et le reste de la France.
- **Décision :** **approximer**, après vérification. Le profilage (pull request #52) montre 371 bulletins pour la Haute-Corse dans la Météo des forêts, et la BDIFF a été exportée pour le 2B (4 992 feux, 2006-2025). La comparaison 2A / 2B est possible. L'export de la France entière reste à faire si le groupe garde cette comparaison.
- **Raison :** la vérification demandée par l'exercice est faite, et le 2B est présent dans les deux sources.
- **Conséquences :** comparaison limitée à deux saisons communes ; sans export national, pas de comparaison avec le reste de la France.
- **Liens :** tickets #20 et #51, pull requests #52 et #64, `docs/qualite/profil-mdf.md`, `docs/qualite/profil-bdiff-2b.md`

### D-013 · La BDIFF comme source de référence pour les feux
- **Date :** 2026-11-18
- **Décidé par :** Biolohf TCHATCHOUA (matrice, pull request #46), relue par Arouna TOURE
- **Contexte :** deux sources décrivent les feux du 2A : la BDIFF et le jeu de la DDT 2A, qui reprend la BDIFF depuis 2023.
- **Options envisagées :** BDIFF seule ; DDT 2A seule ; les deux.
- **Décision :** la **BDIFF** est la source de référence pour les feux (Q1 à Q4). La DDT 2A est gardée en complément pour la localisation.
- **Raison :** la BDIFF est la seule base nationale documentée, avec la date et la commune de chaque feu (la couverture nationale n'est pas encore vérifiée : l'export de la France entière n'est pas fait).
- **Conséquences :** en cas de désaccord depuis 2023, la BDIFF prévaut. La licence de la BDIFF n'est pas ouverte (« aucune modification ni altération ») : voir la question ouverte Q-7. Le dénominateur de surface boisée suit D-007 et D-008.
- **Liens :** ticket #20, pull request #46, `docs/sources/matrice.md` (décisions 5 et 6), `docs/sources/fiche-bdiff.md`

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
| Millésime 2018 de CORINE Land Cover | D-007 | Les 4 membres | À confirmer (ticket #43) |
| Ne pas additionner CORINE Land Cover et BD Forêt | D-008 | Les 4 membres | À confirmer (ticket #43) |
| Feux de 2026 exclus | D-009 | Ahmed PHILIPPE (avait proposé « renoncer » ; sa section 5 est alignée sur « approximer », commit 0725b14) | À confirmer (ticket #61) |
| Décisions de la matrice : seuil, coût, 2B, source de référence | D-010 à D-013 | Les 4 membres | À confirmer (ticket #56) |

---

## Questions ouvertes (à décider par le groupe)

Chaque décision prise ici devra aussi mettre à jour la fiche du glossaire concernée.

| # | Question | Origine | Fiche du glossaire |
|---|---|---|---|
| Q-1 | Que veut dire « danger élevé » : le niveau 3 (orange) seul, ou les niveaux 3 et 4 ? | Tchatchoua, Arouna, Ahmed | Danger élevé |
| Q-2 | L'IFM mesure-t-il un danger météo (Arouna) ou un risque d'éclosion (Ahmed) ? | Arouna, Ahmed | IFM, Danger et risque |
| Q-3 | Qu'appelle-t-on « un feu » : départ de feu, feu de forêt, feu de végétation, intervention ? Quel seuil de surface ? | Saran, Arouna, Tchatchoua | Feu de forêt, Départ de feu |
| Q-4 | Quelle prévision utiliser : J+1 ou J+2 ? (J+1 retenu provisoirement dans D-010) | Arouna | Météo des forêts |
| Q-5 | Le périmètre du SDIS 2A est-il le même que celui du département 2A ? | Tchatchoua | Département, SDIS 2A |
| Q-6 | Quelle période de référence pour comparer les saisons (archives depuis juin 2024, feux depuis 2006 ou 1973) ? | Saran, Arouna | Météo des forêts, BDIFF, Prométhée |
| Q-7 | La licence de la BDIFF (« aucune modification, ni altération ») permet-elle de transformer les données dans le pipeline ? À demander à l'enseignante. | Fiche BDIFF | BDIFF |
| Q-8 | L'énoncé de l'exercice 3 cite `docs/journal-des-decisions.md` ; le dépôt utilise `docs/decisions.md`. À signaler à l'enseignante. | Saran | Sans objet |