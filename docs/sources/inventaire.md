# Inventaire des sources

Projet : feux-de-foret-corse · Commanditaire : Direction du SDIS 2A · Ticket : #19

Rédigé par : Saran DIABAGATE (cheffe de projet) et Arouna TOURE · À relire par : Biolohf TCHATCHOUA (responsable sources)
Date : 2026-11-18

Cet inventaire rassemble les huit fiches d'identité de `docs/sources/`. Les questions sont les quatre questions communes de [`docs/analyse/commande-groupe.md`](../analyse/commande-groupe.md) :

- **Q1** : où se concentrent les départs de feu en Corse-du-Sud ?
- **Q2** : à chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu ?
- **Q3** : combien de jours par été chaque seuil envisagé aurait-il déclenché ?
- **Q4** : le lien entre l'indice et les feux est-il le même en Haute-Corse et dans le reste de la France ?

Règle : ce qui n'a pas été vérifié est écrit « non vérifiée ». Les fiches d'Ahmed et d'Arouna citent les questions de leurs analyses individuelles (Q1 à Q10) ; elles sont converties ici en questions du groupe.

## Tableau

| Source | Explorée par | Pertinente pour nos questions ? | Ce que nous avons découvert |
|---|---|---|---|
| [Archives de la Météo des forêts](fiche-meteo-des-forets.md) (Météo-France) | Arouna TOURE | **Oui, Q2, Q3 et Q4.** Elle donne le niveau de danger (1 à 4) par jour et par département. Seule, elle ne dit rien sur les feux : il faut la croiser avec une base des feux. | Trois saisons seulement (2024, 2025, 2026), soit 371 bulletins pour la Corse-du-Sud. Aucune donnée d'octobre à mai. Les trois fichiers ont des codes de département et des noms de colonnes différents : à harmoniser. Haute-Corse : non vérifiée. |
| [BDIFF](fiche-bdiff.md) (ministère de l'Agriculture) | Arouna TOURE | **Oui, Q1** (feux localisés à la commune, 2006-2025). **Q2, Q3 et Q4** en croisement avec la Météo des forêts, par département et par date. Pour Q4, il faut refaire l'export pour la Haute-Corse et la France. | 4 694 feux en Corse-du-Sud de 2006 à 2025. 46,5 % partent en dehors de la saison de la Météo des forêts. Cause inconnue dans 47 % des cas. Seulement 139 feux dans les deux saisons communes avec la Météo des forêts. La saison 2026 n'est pas publiée. **Licence non ouverte** : « aucune modification ni altération » des données. |
| [Données feux de forêt en Corse-du-Sud, DDT 2A](fiche-feux-foret-corse-du-sud-ddt2a.md) | Arouna TOURE | **Oui, Q1** (position du point de départ et contours des feux, depuis 1973). Complète la BDIFF pour le 2A seulement. Ne répond pas à Q4 (ni Haute-Corse, ni national). | La précision de localisation change selon l'époque (centre de la commune avant 1980, carreau de 1 à 2 km ensuite). Le service WFS ne sert pas les points de départ et renvoie une erreur sur une couche. L'archive complète n'a pas été ouverte : la liste des colonnes est non vérifiée. |
| [Interventions des services d'incendie et de secours](fiche-interventions-sdis.md) (ministère de l'Intérieur) | Biolohf TCHATCHOUA | **Contexte seulement.** Un grain annuel et départemental : aucune date, aucune commune, donc aucune réponse directe à Q1 à Q4. Elle permet de situer le 2A et le 2B année par année (colonne « Feux de végétations »). | 17 fichiers annuels (2008 à 2024). Les colonnes changent selon les périodes (70, 16, puis 71). Une « intervention » n'est pas un départ de feu de forêt. « Feux de végétations » est absente de 2010 à 2013. |
| [Prométhée](fiche-promethee.md) | Biolohf TCHATCHOUA | **Peut-être, Q1.** À confirmer : aucune rubrique de la fiche n'a pu être vérifiée. | Source ajoutée par le groupe (absente de la liste du défi). Les SDIS y saisissent les feux : elle recoupe en partie la BDIFF et les interventions. L'accès direct aux données est soumis à conditions. |
| [Admin Express](fiche-admin-express.md) (IGN) | Saran DIABAGATE | **Oui, comme référentiel**, pour Q1 (rattacher un feu à sa commune et à son département) et Q4 (séparer 2A, 2B et le reste de la France). Elle ne contient ni feux ni météo. | 34 877 communes, dont 124 en Corse-du-Sud. Clé : `code_insee` pour la commune, `2A` (texte) pour le département. Interrogeable en WFS sans téléchargement. Licence Ouverte v2.0. Recoupement : l'export BDIFF compte aussi 124 communes en Corse-du-Sud, ce qui confirme que la jointure par `code_insee` est cohérente. |
| [BD Forêt](fiche-bd-foret.md) (IGN) | Ahmed PHILIPPE | **Appoint pour Q1 et Q4.** Ne répond à aucune question seule : elle sert de dénominateur (surface boisée par commune, feux par km² de forêt). Pas de code commune : jointure spatiale. | Pour la Corse-du-Sud, ce sont des photos aériennes de 2011. Les catalogues donnent trois périodes différentes. Le « shapefile » de data.gouv.fr fait 112,8 Ko : c'est un lien de renvoi, pas les données. Le maquis semble compris dans les « landes ». |
| [Corine Land Cover](fiche-corine-land-cover.md) (SDES, Copernicus) | Ahmed PHILIPPE | **Appoint pour Q4**, pour comparer les départements avec les mêmes règles. Trop grossière pour Q1 (25 ha minimum). | Millésimes 1990, 2000, 2006, 2012 et 2018. La page data.gouv.fr s'arrête à 2012 : le millésime 2018 est chez le SDES. Les tailles affichées sur data.gouv.fr ne décrivent pas les données. |

## Réponses en groupe

### Quelles questions de nos analyses n'ont encore aucune source ?

- **Le coût journalier du dispositif renforcé (Q3).** Aucune source ouverte ne le donne. Il faut le demander au SDIS 2A, comme le « seuil actuel », la définition d'« un feu » et le budget disponible (voir `commande-groupe.md`).
- **Les feux de l'été 2026.** La BDIFF ne publie que jusqu'à l'année précédente, les interventions s'arrêtent en 2024 et la couverture de 2025 et 2026 dans la source DDT 2A n'est pas confirmée. Nous avons la météo de 2026, mais pas les feux correspondants.
- **Q4 (Haute-Corse et reste de la France).** Les sources existent (BDIFF et Météo des forêts couvrent la France), mais aucune extraction n'a encore été faite : la présence de la Haute-Corse dans la Météo des forêts est non vérifiée, et l'export BDIFF ne porte que sur le 2A. La question n'a donc pas encore de source **vérifiée**.
- **Le niveau de danger à l'échelle infra-départementale (Q1 et Q2).** La Météo des forêts ne publie qu'un niveau par département ; aucune source ne donne l'historique du danger par zone.
- **L'heure réelle de départ du feu.** La BDIFF ne donne que la date et l'heure d'alerte au CODIS, qui peut être postérieure au départ.

### Quelle source nous a surpris, et pourquoi ?

- **La BDIFF** : 46,5 % des feux de Corse-du-Sud partent en dehors de la saison de la Météo des forêts, et seulement 139 feux tombent dans les saisons communes aux deux sources. Cela limite fortement ce que Q2 et Q3 peuvent démontrer.
- **Les catalogues data.gouv.fr** : plusieurs « fichiers » annoncés (shapefile de la BD Forêt, CSV de Corine Land Cover) ont la taille d'une page de renvoi, pas celle des données. On ne peut pas estimer une volumétrie depuis le catalogue.

### Quelle source semble utile mais inexploitable dans le temps du projet ?

- **Prométhée** : utile pour localiser les feux, mais l'accès direct est soumis à conditions et aucune rubrique de sa fiche n'a pu être vérifiée, y compris la licence. Ses données recoupent en partie la BDIFF et la source DDT 2A, déjà plus accessibles. Nous la gardons en réserve.
- **À surveiller** : la source DDT 2A, dont l'archive complète n'a pas été ouverte et dont le service WFS est défectueux, et la BDIFF, dont la licence non ouverte est à discuter avec l'enseignante, puisque notre pipeline transformera les données.
- **AROME et ARPEGE** (sources du défi non explorées) : les modèles météo de Météo-France pourraient expliquer les feux partis à indice bas (vent, humidité), mais leur volume est trop important pour le temps du projet.

## Sources du défi non explorées

Lecture dans l'autre sens : ces sources figurent dans la liste du défi mais ne servent, à ce stade, aucune de nos quatre questions.

| Source | Raison |
|---|---|
| NASA FIRMS, EFFIS, Copernicus EWDS (IFM) | Non retenues en v0 : la BDIFF et la Météo des forêts couvrent déjà les feux et le danger. À reconsidérer pour Q4 si la comparaison nationale manque de données. |
| AROME, ARPEGE | Volume trop important pour le temps du projet. |
| Images Pyronear | Hors sujet : images pour la détection automatique, pas une série de feux. |
| BD TOPO, BD ORTHO, MNS LiDAR HD, OCS-GE | Non retenues en v0 : la BD Forêt et Corine Land Cover suffisent comme dénominateurs. |
| Carroyage DFCI | Non explorée ; pourrait servir à Q1 avec la source DDT 2A (colonne `CODE_CAR`). |
| Obligations légales de débroussaillement, GASPAR, festivals, trafic routier | Aucune de nos quatre questions ne les mobilise à ce stade. |
