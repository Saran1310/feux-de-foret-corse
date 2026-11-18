# Inventaire des sources

- **Projet :** feux-de-foret-corse (SDIS 2A, saison 2027)
- **Version :** v0, exercice 2 (mise en commun)
- **Date :** 2026-11-18
- **Rédigé par :** Arouna Touré, à partir des fiches de chaque membre
- **Relecture :** Biolohf Tchatchoua (responsable sources)

Chaque ligne renvoie à la fiche d'identité de la source dans `docs/sources/`. Les questions citées sont celles retenues par le groupe dans `docs/analyse/commande-groupe.md` : **Q1** où se concentrent les départs de feu en Corse-du-Sud ; **Q2** à chaque niveau de la Météo des forêts, quelle part des jours compte au moins un départ de feu ; **Q3** combien de jours par été chaque seuil déclencherait ; **Q4** le lien entre l'indice et les feux est-il le même en Haute-Corse et dans le reste de la France.

## Tableau

| Source | Explorée par | Pertinente pour nos questions ? | Ce que nous avons découvert |
|--------|--------------|---------------------------------|-----------------------------|
| Archives de la Météo des forêts ([fiche](fiche-meteo-des-forets.md)) | Arouna Touré | **Oui**, Q2, Q3, Q4 : seule source du niveau de danger, au grain jour x département, pour toute la France métropolitaine. | Historique de trois saisons seulement (2024 à 2026), soit 371 bulletins pour la Corse-du-Sud, de juin à septembre. Le schéma change selon l'année (`nom_dep` / `dep_nom`, code `1` / `01`). La colonne `date` est la date de publication : le jour prévu est le lendemain. |
| BDIFF ([fiche](fiche-bdiff.md)) | Arouna Touré | **Oui**, Q1, Q2, Q4 : un incendie par ligne, à la commune, avec date et heure d'alerte, pour toute la France. | Export 2A ouvert : 4 694 feux de 2006 à 2025. 46,5 % partent hors de la saison de la Météo des forêts ; cause inconnue pour 47 %. La saison 2026 ne sera publiée qu'en 2027. Clé unique : `Année` + `Numéro`. Licence non ouverte (exigence d'intégrité). |
| Données feux de forêt en Corse du Sud, DDT 2A ([fiche](fiche-feux-foret-corse-du-sud-ddt2a.md)) | Arouna Touré | **En partie**, Q1 : localisation du point de départ en Corse-du-Sud depuis 1973. Inutile pour Q4 (2A seulement). | Reprend la BDIFF depuis 2023. Précision de localisation variable selon la période (centre de commune avant 1981). Données arrêtées à 2024 malgré un titre annonçant 2025. Archive non ouverte ; service WFS défectueux. |
| Prométhée ([fiche](fiche-promethee.md)) | Biolohf Tchatchoua | **Incertaine**, Q1 potentiellement. Toutes les rubriques restent non vérifiées. | Accès aux données soumis à conditions ; aucun export ouvert. Décrit en partie les mêmes feux que la BDIFF et la source DDT 2A, qui en reprend déjà le numéro Prométhée. |
| Interventions réalisées par les services d'incendie et de secours ([fiche](fiche-interventions-sdis.md)) | Biolohf Tchatchoua | **En partie**, Q4 : comparaison annuelle de la Corse-du-Sud, de la Haute-Corse et des autres départements. Inutile pour Q1 à Q3 (ni commune, ni date). | Grain département x année. "Feux de végétations" absent de 2010 à 2013. Colonnes variables selon les années (70, 16 puis 71). Code `2a` en minuscules ; le "département" est celui du service d'incendie. Une intervention n'est pas un départ de feu. |
| Admin Express ([fiche](fiche-admin-express.md)) | Saran Diabagate | **Oui**, comme référentiel pour Q1 et Q4 : rattacher chaque feu à sa commune et à son département. | 124 communes en Corse-du-Sud, comme dans l'export BDIFF : la jointure par `code_insee` est cohérente. Plusieurs éditions et variantes : il faudra fixer celle utilisée. Les codes `2A` / `2B` doivent être lus en texte. |
| BD Forêt V2 ([fiche](fiche-bd-foret.md)) | Ahmed-Philippe | **En partie**, Q1 : dénominateur pour rapporter les feux à la surface boisée de chaque commune. Ne répond à aucune question seule. | Photographies de 2011 pour la Corse-du-Sud ; taux de boisement de 79 %. Aucune clé administrative : jointure spatiale obligatoire. Le maquis semble compris dans les landes. Le fichier de data.gouv.fr est un lien de renvoi, pas les données. |
| Corine Land Cover ([fiche](fiche-corine-land-cover.md)) | Ahmed-Philippe | **En partie**, Q4 : dénominateur pour comparer les départements à grain égal (même règle dans toute la France). | La copie data.gouv.fr s'arrête à 2012 ; le millésime 2018 est chez le SDES. Maille de 25 ha, trop grossière pour la commune. Ne pas cumuler avec la BD Forêt. |

## Synthèse

### Quelles questions de nos analyses n'ont encore aucune source ?

- **Le coût du dispositif renforcé** (Q3) : la Météo des forêts permet de compter les jours d'activation par seuil, mais aucune source ne donne le coût journalier ni le contenu du dispositif. À demander au SDIS 2A, comme le seuil actuellement appliqué.
- **Les départs de feu de la saison 2026** (toutes les questions) : la BDIFF ne la publiera qu'en 2027, et la source DDT 2A s'arrête à 2024. Seule la Météo des forêts couvre 2026.
- **Le danger à l'échelle infra-départementale** (Q1 et Q2) : aucune source ne donne l'historique du niveau de danger par zone ; la Météo des forêts reste départementale.
- **L'heure réelle de départ du feu** : la BDIFF ne donne que l'heure d'alerte au CODIS.

### Quelle source nous a surpris, et pourquoi ?

**La BDIFF.** Près de la moitié des feux de Corse-du-Sud (46,5 %) partent entre octobre et mai, quand la Météo des forêts n'est pas publiée. Le seuil de déclenchement, qui ne s'applique qu'en été, ne peut donc concerner qu'une partie des départs de feu : c'est une piste directe pour expliquer les "feux partis quand l'indice était au plus bas" signalés par les chefs de centre. Autre surprise : sa licence n'est pas une licence ouverte.

Les catalogues aussi ont surpris : sur data.gouv.fr, plusieurs fichiers annoncés (BD Forêt, Corine Land Cover) ne sont que des liens de renvoi, et leurs tailles ne décrivent pas les données.

### Quelle source semble utile mais inexploitable dans le temps du projet ?

**Prométhée.** Elle couvre les 15 départements méditerranéens et pourrait enrichir la comparaison 2A / 2B, mais l'accès aux données est soumis à conditions et aucun export n'a pu être ouvert. Comme la BDIFF et la source DDT 2A décrivent en grande partie les mêmes feux, le groupe peut s'en passer pour la v1.

Parmi les sources du défi non explorées, les modèles météo **AROME et ARPEGE** sont dans le même cas : utiles pour Q2 (vent, humidité), mais trop volumineux pour être traités avant le 11 décembre.

## Sources du défi non explorées

| Source | Raison |
|--------|--------|
| NASA FIRMS, EFFIS, Copernicus EWDS (IFM) | Non retenues en v0 : la BDIFF et la Météo des forêts couvrent déjà les feux et le danger ; à reconsidérer pour Q4 si la comparaison nationale manque de données. |
| AROME, ARPEGE | Volume trop important pour le temps du projet. |
| Images Pyronear | Hors sujet : images pour la détection automatique, pas de série de feux. |
| BD TOPO, BD ORTHO, MNS LiDAR HD, OCS-GE, Carroyage DFCI | Non retenues en v0 ; le carroyage DFCI pourrait servir à Q1 avec la source DDT 2A (colonne `CODE_CAR`). |
| Obligations légales de débroussaillement, GASPAR, festivals, trafic routier | Aucune question du groupe ne les mobilise à ce stade. |
