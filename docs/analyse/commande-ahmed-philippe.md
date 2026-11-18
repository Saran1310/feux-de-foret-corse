# Analyse de la commande - SDIS 2A (Saison feux 2027)

* **Auteur :** Ahmed PHILIPPE
* **Commanditaire :** Direction du SDIS de la Corse-du-Sud (2A)
* **Échéance de restitution :** 11 décembre 2026

---

## 1. Questions décisionnelles

*Règle : chaque question doit orienter un arbitrage opérationnel ou budgétaire concret du SDIS 2A.*

1. **Priorisation géographique des moyens :** Quelles communes ou secteurs de Corse-du-Sud (2A) concentrent historiquement le plus grand nombre de départs de feu et les surfaces brûlées les plus importantes en période estivale ?
   * *Décision associée :* Affecter en priorité les effectifs humains (patrouilles, guet) et les moyens financiers/matériels sur les zones à plus forte sinistralité plutôt que de les répartir uniformément sur tout le département.
2. **Saisonnalité et créneaux critiques :** Quelles semaines de l'été et quelles plages horaires présentent le pic d'éclosion des feux en 2A ?
   * *Décision associée :* Concentrer le budget des renforts saisonniers sur les fenêtres temporelles critiques au lieu de maintenir un dispositif maximal sur tout l'été.
3. **Fiabilité de la météo des forêts (faux positifs et faux négatifs) :** Quel est le taux de concordance réel entre chaque niveau d'alerte de la Météo des forêts et les départs de feu constatés en Corse-du-Sud (notamment les feux survenus lorsque l'indice était au plus bas et les alertes élevées sans départ de feu) ?
   * *Décision associée :* Évaluer l'ampleur des fausses alertes (coût humain/financier inutile) et des angles morts (risque opérationnel non couvert) afin de justifier une révision du seuil de déclenchement.
4. **Calibrage du seuil de déclenchement :** À partir de quel niveau de l'indice Météo des forêts (ou quelle combinaison indice + facteurs locaux comme le vent/la sécheresse) le dispositif renforcé offre-t-il le meilleur ratio coût/couverture des départs de feu ?
   * *Décision associée :* Fixer le nouveau seuil officiel de déclenchement des patrouilles et du guet pour la saison 2027.
5. **Comparaison régionale (2A vs 2B) :** Le comportement de l'indice Météo des forêts et son pouvoir prédictif diffèrent-ils entre la Corse-du-Sud (2A) et la Haute-Corse (2B) ?
   * *Décision associée :* Déterminer si le SDIS 2A doit adopter un seuil spécifique à son territoire ou harmoniser ses règles de déclenchement à l'échelle de l'île (zone de défense / région Corse).
6. **Positionnement national :** Comment la sinistralité et la distribution des niveaux d'alerte de la Corse-du-Sud se situent-elles par rapport aux autres départements français (notamment le pourtour méditerranéen) ?
   * *Décision associée :* Argumenter les demandes de dotations budgétaires et de renforts nationaux auprès de la sécurité civile en objectivant la spécificité du risque en 2A.

---

## 2. Termes inconnus (à intégrer au glossaire du groupe)

* **SDIS 2A :** Service Départemental d'Incendie et de Secours de la Corse-du-Sud (2A).
* **Météo des forêts :** Dispositif national de prévention (porté par Météo-France et les ministères concernés) évaluant quotidiennement le niveau de danger d'incendie de forêt et de végétation par département selon une échelle de vigilance (vert, jaune, orange, rouge).
* **Indice forêt météo (IFM) :** Indicateur météorologique composite sous-jacent servant à estimer le risque d'éclosion et de propagation d'un feu à partir de la température, de l'humidité de l'air, de la vitesse du vent et des précipitations.
* **Dispositif renforcé (patrouilles, guet) :** Mobilisation préventive supplémentaire de sapeurs-pompiers, de forestiers-sapeurs ou de moyens terrestres/aériens (vigies, patrouilles de surveillance, pré-positionnement de véhicules) déclenchée avant même tout départ de feu.
* **Chef de centre :** Officier ou sous-officier commandant un Centre d'Incendie et de Secours (CIS) local au sein du maillage territorial du SDIS.
* **Départ de feu (éclosion) :** Début d'un incendie de forêt ou de végétation recensé par les secours, indépendamment de la surface finale parcourue.

---

## 3. Besoins métier et analytiques

* **Cartographie et hiérarchisation du risque en 2A :** Identifier les secteurs géographiques et les périodes où concentrer les moyens humains et financiers pour maximiser l'efficacité de la lutte préventive.
* **Audit de performance du seuil actuel :** Mesurer objectivement les écarts entre les prévisions de la Météo des forêts et la réalité du terrain (faux positifs = alerte élevée sans feu ; faux négatifs = feu déclaré malgré un indice bas).
* **Simulation de scénarios de déclenchement :** Comparer plusieurs seuils candidats pour l'été 2027 en croisant le nombre de jours d'activation (impact budgétaire et fatigue des équipes) avec le pourcentage de feux effectivement couverts.
* **Benchmark territorial (régional et national) :** Disposer d'une analyse comparative entre le 2A, le 2B et le reste de la France métropolitaine pour situer le niveau d'exposition du département.
* **Support d'aide à la décision livrable avant le 11 décembre :** Produire une restitution claire, chiffrée et argumentée permettant à la Direction du SDIS 2A d'arbitrer son budget et ses consignes opérationnelles avant le printemps 2027.

---

## 4. Données idéales recherchées

| Question / Besoin | Donnée idéale | Grain (résolution) | Période historique | Fraîcheur | Emprise géographique |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1 & 2. Localisation et temporalité des feux** | Historique des incendies de forêt et de végétation (date, heure d'alerte, commune/coordonnées, surface brûlée, cause) | Événement (1 ligne = 1 feu) / Commune / Jour | Minimum 5 à 10 dernières années (incluant l'été 2026) | Consolidée annuellement (à jour post-été 2026) | Département 2A (prioritaire), 2B et France entière |
| **3 & 4. Comportement de la Météo des forêts et calibration du seuil** | Historique quotidien des niveaux de vigilance Météo des forêts et valeurs de l'indice IFM | Jour × Département (idéalement zone météo / massif) | Toute l'historique disponible du dispositif (dont étés 2024 à 2026) | Quotidienne (archivée post-saison 2026) | Départements 2A, 2B et ensemble des départements métropolitains |
| **4. Analyse des feux par indice bas (explication météo fine)** | Observations météorologiques locales (vent moyen/rafales, humidité, température, cumul de pluie) | Horaire ou quotidienne × Station météo | 5 à 10 dernières années (incluant été 2026) | Consolidée post-été 2026 | Corse-du-Sud (2A) et Haute-Corse (2B) |
| **1 & 4. Dimensionnement et coût du dispositif renforcé** | Historique des déclenchements du dispositif renforcé du SDIS 2A (effectifs engagés, heures de patrouille/guet, coût journalier moyen) | Jour × Centre de secours (CIS) ou secteur | 3 à 5 dernières saisons estivales | Consolidée post-été 2026 | Département 2A (SDIS Corse-du-Sud) |
| **1 & 6. Contexte territorial et couverture forestière** | Occupation des sols / surfaces boisées et maillage des Centres d'Incendie et de Secours (CIS) | Commune / Département | Dernier millésime disponible | Annuelle / pluriannuelle | Corse (2A, 2B) et départements métropolitains |

---

## 5. Confrontation aux sources

Sources : les 8 fiches d'identité du groupe (exercice 2). Abréviations des colonnes :
**BDIFF** = `fiche-bdiff.md` · **DDT 2A** = `fiche-feux-foret-corse-du-sud-ddt2a.md` · **MdF** = `fiche-meteo-des-forets.md` · **Interv. SDIS** = `fiche-interventions-sdis.md` · **Prométhée** = `fiche-promethee.md` · **Admin Express** = `fiche-admin-express.md` · **BD Forêt** = `fiche-bd-foret.md` · **CLC** = `fiche-corine-land-cover.md`.

### Matrice

| Question | BDIFF | DDT 2A | MdF | Interv. SDIS | Prométhée | Admin Express | BD Forêt | CLC |
|---|---|---|---|---|---|---|---|---|
| 1. Priorisation géographique | **partiel** : un feu par ligne avec `Code INSEE`, `Date de première alerte`, `Surface parcourue (m2)` ; mais 2006-2025 seulement, l'été 2026 manque (rubrique « Période ») | **partiel** : point de départ et contours depuis 1973 (rubrique « Grain ») ; s'arrête à 2024, colonnes non vérifiées dans le fichier | **absent** : aucun feu, et pas plus fin que le département | **absent** : pas de localisation sous le département (rubrique « Grain ») | **inconnu** : grain et colonnes non vérifiés | **absent** : aucune donnée de feu ; sert de référentiel (`code_insee`) | **partiel** : surface boisée par commune par jointure spatiale (rubrique « Clés ») ; photos de 2011 | **partiel** : occupation du sol 2018, maille de 25 ha trop grossière à la commune (rubrique « Grain ») |
| 2. Saisonnalité et créneaux | **partiel** : `Date de première alerte` donne la date et l'heure ; mais l'été 2026 manque (rubrique « Période ») | **partiel** : date du départ dans `ID_DDT2A` ; heure non documentée, s'arrête à 2024 | **absent** : aucun feu | **absent** : totaux annuels, pas de date (rubrique « Grain ») | **inconnu** : non vérifié | **absent** | **absent** | **absent** |
| 3. Fiabilité de la Météo des forêts | **partiel** : feux datés par `Date de première alerte` ; seulement 139 feux en commun avec la MdF (juin-sept. 2024-2025), 2026 absente (rubrique « Ce que nous avons découvert ») | **partiel** : en commun avec la MdF sur 2024 seulement (rubrique « Période ») | **partiel** : `niveau_j1` par `num_dep` et `date`, mais 3 saisons de juin à septembre seulement, rien avant juin 2024 (rubrique « Période ») | **absent** : grain annuel, impossible à croiser jour par jour | **inconnu** : non vérifié | **absent** : référentiel | **absent** | **absent** |
| 4. Calibrage du seuil (coût / couverture) | **partiel** : feux couverts par seuil calculables avec la MdF, sur 2 saisons communes | **partiel** : même limite, 2024 seulement | **partiel** : nombre de jours au-dessus de chaque niveau calculable avec `niveau_j1` ; pas de vent ni de sécheresse | **absent** : aucun coût, aucun déclenchement du dispositif | **inconnu** : non vérifié | **absent** | **absent** | **absent** |
| 5. Comparaison 2A / 2B | **partiel** : base nationale selon la documentation, mais seul le 2A a été extrait (rubrique « Emprise ») | **absent** : Corse-du-Sud uniquement (rubrique « Emprise ») | **partiel** : 2A présent ; 2B non vérifié (rubrique « Emprise ») ; 3 saisons | **partiel** : `Feux de végétations` par département, dont « 2a » et « 2b », mais annuel et absent de 2010 à 2013 | **inconnu** : non vérifié | **absent** : référentiel (`code_insee_du_departement`) | **absent** | **absent** |
| 6. Positionnement national | **partiel** : national selon la documentation, mais non extrait (rubrique « Volumétrie ») ; licence non ouverte | **absent** : 2A uniquement | **partiel** : 96 départements, `niveau_j1` par `num_dep` ; mais 2024-2026 seulement, l'année 2023 du dispositif manque | **partiel** : `Feux de végétations` par département et par an (2008-2009, 2014-2024) ; une intervention n'est pas un départ de feu | **inconnu** : 15 départements méditerranéens annoncés, non vérifié | **absent** : référentiel | **partiel** : surface boisée par département, mais millésimes de 2007 à 2018 selon le département | **partiel** : surface forestière comparable partout (millésime 2018 unique) ; colonnes non vérifiées |

**Lecture dans les deux sens.**
- *Question vers sources* : aucune question n'a de source « complet ». Le manque le plus net est la question 4 : ni le coût du dispositif renforcé, ni le vent ou la sécheresse ne figurent dans aucune source.
- *Source vers questions* : Admin Express ne répond à aucune question seule, mais elle est indispensable comme référentiel de jointure : elle reste. Prométhée est « inconnu » partout : il faut la vérifier avant de la garder ou de l'écarter.

### Écarts avec la section 4

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1 | BDIFF | 1 feu, commune ou coordonnées → 1 feu à la commune, sans coordonnées | 5 à 10 ans, été 2026 inclus → 2006-2025, sans 2026 | consolidée après l'été 2026 → diffusion annuelle de l'année N-1 | 2A, 2B, France → 2A extrait, 2B et France à extraire |
| 2 | BDIFF | = (date et heure d'alerte présentes) | 5 à 10 ans, été 2026 inclus → 2006-2025, sans 2026 | consolidée après l'été 2026 → année N-1 | = pour le 2A |
| 3 | MdF croisée avec la BDIFF | jour × département, idéalement zone ou massif → jour × département | tout l'historique du dispositif (depuis 2023) → 2024-2026 pour l'indice, 2024-2025 en commun avec les feux | quotidienne → quotidienne en saison seulement (juin à septembre) | 2A, 2B, France → France métropolitaine (2B non vérifié) |
| 4 | MdF croisée avec la BDIFF | jour × centre de secours, avec coûts → jour × département, sans coûts ; station météo horaire → aucune source | 3 à 5 saisons → 2 saisons communes | consolidée après l'été 2026 → 2026 absente côté feux | 2A → = |
| 5 | MdF croisée avec la BDIFF | = (jour × département) | tout l'historique → 2024-2025 en commun | = | 2A et 2B → 2A vérifié, 2B à vérifier dans les deux sources |
| 6 | MdF (niveaux) et Interv. SDIS (sinistralité) | commune ou département → département ; année seulement pour les interventions | dernier millésime et historique → 2024-2026 (niveaux) ; 2008-2024 avec un trou de 2010 à 2013 (interventions) | annuelle → 2026 pour les niveaux, 2024 pour les interventions | France → = |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1 et 2 | L'été 2026 (absent de la BDIFF jusqu'en 2027) | **collecter** | Le SDIS 2A, commanditaire, saisit lui-même ses feux : il peut nous transmettre la saison 2026. | Un délai de réponse. Sans réponse, on travaille sur 2006-2025 et on l'écrit dans la restitution. |
| 1, 2, 3, 4, 5, 6 | Prométhée : toutes les cellules « inconnu » | **vérifier d'abord** | La règle de l'exercice : un « inconnu » appelle une vérification avant toute décision. L'accès au site est soumis à conditions. | Du temps pour Biolohf ; si l'accès est refusé, on écarte la source. |
| 3 | Un historique commun très court (2 saisons, 139 feux) ; 46,5 % des feux partent hors saison de la MdF | **approximer**, en plus de collecter 2026 | Utiliser l'indice FWI continu de Copernicus EWDS (calculé chaque jour depuis 1940) comme proxy des niveaux de la MdF, pour tester la relation indice / feux sur 20 saisons. | Le FWI d'EWDS mesure mal les niveaux officiels : calcul européen sur une grille d'environ 25 km, différent du calcul de Météo-France. La source n'est pas dans l'inventaire : il faut l'y ajouter. |
| 4 | Le coût et les déclenchements du dispositif renforcé | **collecter** | Seul le SDIS 2A détient ces données (déjà noté par le groupe dans la décision D-004). | Dépend du SDIS. En attendant : **approximer** le coût par le nombre de jours au-dessus de chaque seuil (`niveau_j1`), ce qui suppose un coût identique chaque jour. |
| 4 | Le vent et la sécheresse locaux | **renoncer** pour cette version | Aucune source de l'inventaire ne les fournit ; les modèles AROME et ARPEGE sont trop lourds pour le temps du projet. On calibre le seuil sur l'indice seul. | Le seuil ne tiendra pas compte des conditions locales ; à rouvrir si une source d'observations par station est ajoutée. |
| 5 | La Haute-Corse n'est vérifiée ni dans la BDIFF ni dans la MdF | **vérifier d'abord**, puis **collecter** | Refaire l'export de la BDIFF pour le 2B et contrôler le 2B dans la MdF : les deux sont publics. | Un export et une requête de plus ; faible coût. |
| 6 | La sinistralité nationale comparable | **collecter**, et **approximer** en attendant | Collecter : export national de la BDIFF (public). Approximer : `Feux de végétations` des interventions SDIS par département. | Le proxy mesure mal : une intervention n'est pas un départ de feu, la colonne manque de 2010 à 2013, et la Bouches-du-Rhône apparaît deux fois certaines années. La BDIFF n'a pas de licence ouverte : à valider avec l'enseignante. |
