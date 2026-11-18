# Fiche d'identité de source : CORINE Land Cover

- **Explorée par :** Ahmed Philippe
- **Date de l'exploration :** 2026-11-17
- **Page de la source :** https://www.data.gouv.fr/datasets/corine-land-cover-occupation-des-sols-en-france
- **Méthode :** lecture de la page data.gouv.fr (description, métadonnées et onglet « Fichiers », capture du 2026-11-17), puis de la page du producteur français (SDES, statistiques.developpement-durable.gouv.fr/corine-land-cover-0). **Aucun fichier de données ouvert à ce stade** : les rubriques qui en dépendent sont marquées « non vérifiée ».

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | Programme européen Copernicus, piloté par l'Agence européenne pour l'environnement (39 États). Pour la France : Service des données et études statistiques (SDES) du ministère de la Transition écologique, publié sur data.gouv.fr sous le nom du ministère. Production par interprétation visuelle d'images satellites, à l'échelle du 1/100 000. |
| Mode d'accès et format | Téléchargement de fichiers. Sur le site du SDES : données géographiques en shapefile (archives zip), une archive par millésime pour la métropole et une pour les DROM, sans découpage par région ni département. Statistiques à la commune en CSV ou zip. Documentation en PDF et XLS. **Sur data.gouv.fr** : 5 « fichiers principaux » (Méthodologie, PDF 93,0 Ko ; Données statistiques à la commune, CSV 93,0 Ko ; Accès aux données régionales, « shape » 4,7 Ko ; Interface de téléchargement, « géotiff » 1,2 Ko ; Visualisation des données, HTML 1,2 Ko) et 3 API (WMTS, WMS, WFS). Vu leurs tailles, ce sont des **liens de renvoi**, pas les données : le CSV communal fait 93 Ko sur data.gouv.fr contre 22 Mo chez le SDES. La page affiche l'alerte « Certains fichiers ne sont pas disponibles » et renvoie vers ecologie.data.gouv.fr pour des métadonnées enrichies. |
| Grain (une ligne = ?) | Un polygone d'occupation du sol homogène d'**au moins 25 ha** et 100 m de large (métropole), classé dans une nomenclature de 44 postes sur 3 niveaux (territoires artificialisés, agricoles, forêts et milieux semi-naturels, zones humides, surfaces en eau). Il existe aussi des couches de **changements** entre deux millésimes (unité minimale de 5 ha). Noms des colonnes : non vérifiés. |
| Emprise géographique | 39 pays européens ; pour la France, la métropole et les DOM (pour la Guyane, seule la bande côtière est traitée, d'après data.gouv.fr). Présence de la Corse dans le fichier métropole : non vérifiée. |
| Période réellement couverte | Des photographies à date fixe : **1990, 2000, 2006, 2012 et 2018** pour la métropole (SDES). Le millésime le plus récent décrit l'occupation du sol de 2018. **Attention : la page data.gouv.fr ne cite que 1990, 2000, 2006 et 2012** (avec les changements 1990-2000, 2000-2006 et 2006-2012) ; le millésime 2018 se trouve chez le SDES. |
| Date de dernière mise à jour affichée | Page data.gouv.fr : **17 novembre 2026**. Les ressources ont des dates variées : méthodologie, CSV et API WMS/WMTS « aujourd'hui » ; accès régional le 23 février 2026 ; visualisation le 5 octobre 2026 ; API WFS le 19 mars 2026. Page du SDES : publiée le 27 décembre 2018. Aucune de ces dates ne correspond à la période décrite par les données. |
| Fréquence de mise à jour | Un nouveau millésime tous les 6 ans environ (1990, 2000, 2006, 2012, 2018). Aucun millésime après 2018 n'est annoncé ; une nouvelle génération, CLC+, est en cours de production (images Sentinel à 10 m, seuil de 1 ha, cycle prévu de 3 ans). |
| Volumétrie | Statistiques à la commune pour la métropole : 22,04 Mo (CSV, 5 postes), 10,03 Mo (zip, 15 postes), 13,56 Mo (zip, 44 postes). Taille des fichiers géographiques et nombre de polygones pour la Corse : non vérifiés. |
| Clés disponibles | Fichiers géographiques : **la géométrie uniquement** (jointure spatiale avec Admin Express ou les points de départ de feu). Fichiers statistiques : publiés à l'échelle de la commune, donc probablement un code commune ; nom de colonne et millésime du COG utilisés : non vérifiés. |
| Données personnelles | Aucune. Il s'agit d'occupation du sol à grande maille (25 ha minimum). |
| Licence | « Licence Ouverte / Open Licence », affichée sur la page data.gouv.fr. Le numéro de version n'est pas affiché (la BD Forêt, elle, indique « version 2.0 »). |
| Questions de mon analyse auxquelles elle pourrait répondre | **Q6** (positionnement national) : surfaces de forêts et milieux semi-naturels par département, mesurées de la même façon dans toute la France et en Europe, pour comparer à grain égal. **Q1** : seulement en appoint, car la maille de 25 ha est trop grossière à l'échelle d'une commune corse. Comme la BD Forêt, elle sert de **dénominateur**, pas de réponse seule. Ne répond pas à Q2 à Q5. |

## Ce que nous avons découvert

- **La source du défi est incomplète** : la page data.gouv.fr s'arrête à 2012, alors que le millésime 2018 existe chez le SDES. Il faut prendre la donnée chez le producteur, pas sur la copie.
- **Les tailles et formats affichés par data.gouv.fr ne décrivent pas les données** : un « shape » de 4,7 Ko, un « géotiff » de 1,2 Ko, un CSV de 93 Ko. Les 3 API affichent exactement les mêmes tailles que celles de la BD Forêt (WMTS 3,0 Mo, WMS 937,0 Ko, WFS 4,6 Mo, mise à jour du 19 mars 2026) : ce sont probablement les documents de description des services de la Géoplateforme, communs à plusieurs jeux. Règle à retenir : **ne jamais estimer la volumétrie depuis le catalogue.**
- **Avantage sur la BD Forêt** : un seul millésime pour toute la France, produit avec les mêmes règles. C'est la bonne base pour comparer le 2A au reste du territoire (Q6). La BD Forêt, elle, mélange des années de 2007 à 2018 selon les départements.
- **Question à vérifier dans la nomenclature** : le maquis a-t-il une classe propre dans le groupe « forêts et milieux semi-naturels » ? Si oui, CORINE Land Cover le distinguerait mieux que la BD Forêt, où il semble compris dans les landes.
- **Données anciennes** : 2018, soit 6 à 8 ans avant les feux étudiés (2024 à 2026).

## Points d'attention pour le chargement (responsable qualité)

1. **Choisir un seul millésime (2018)** et le garder en colonne, pour ne pas mélanger des époques.
2. **Unité minimale de 25 ha** : les petites parcelles boisées disparaissent dans des classes voisines. Les surfaces par commune sont des ordres de grandeur, pas des mesures fines.
3. **Ne pas additionner** CORINE Land Cover et BD Forêt : elles mesurent la même chose avec des règles différentes. Le groupe doit en retenir une par usage (décision à consigner dans le journal).

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Version de la Licence Ouverte | Numéro non affiché sur la page data.gouv.fr. |
| Noms des colonnes (code de nomenclature, identifiant, surface) | Fichier non ouvert. |
| Présence de la Corse et système de coordonnées utilisé pour elle | Fichier non ouvert ; non précisé sur la page du SDES. |
| Code et libellé exacts des classes de maquis et de landes | Nomenclature détaillée non lue. |
| Clé de jointure des fichiers statistiques communaux | Fichier non ouvert. |
