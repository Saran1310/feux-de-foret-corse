# Fiche d'identité de source : CORINE Land Cover

- **Explorée par :** Ahmed Philippe
- **Date de l'exploration :** 2026-11-17, complétée le 2026-11-18 après relecture
- **Page de la source :** https://www.data.gouv.fr/datasets/corine-land-cover-occupation-des-sols-en-france
- **Méthode :** lecture de la page data.gouv.fr (description, métadonnées et onglet « Fichiers », capture du 2026-11-17), puis de la page du producteur français (SDES, statistiques.developpement-durable.gouv.fr/corine-land-cover-0).
- **Fichier ouvert (2026-11-18) :** `clc_etat_com_n1.csv`, statistiques communales de métropole au niveau 1 de la nomenclature (5 postes), téléchargé sur le site du SDES. Les fichiers géographiques (shapefile) n'ont pas été ouverts.

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | Programme européen Copernicus, piloté par l'Agence européenne pour l'environnement (39 États). Pour la France : Service des données et études statistiques (SDES) du ministère de la Transition écologique, publié sur data.gouv.fr sous le nom du ministère. Production par interprétation visuelle d'images satellites, à l'échelle du 1/100 000. |
| Mode d'accès et format | Téléchargement de fichiers. Sur le site du SDES : données géographiques en shapefile (archives zip), une archive par millésime pour la métropole et une pour les DROM, sans découpage par région ni département. Statistiques à la commune en CSV ou zip. Documentation en PDF et XLS. **Format relevé du CSV communal** : séparateur point-virgule, encodage UTF-8, fins de ligne Windows, et **quatre lignes d'en-tête** avant les données (libellés longs, types, unités, puis noms courts des colonnes). **Sur data.gouv.fr** : 5 « fichiers principaux » (Méthodologie, PDF 93,0 Ko ; Données statistiques à la commune, CSV 93,0 Ko ; Accès aux données régionales, « shape » 4,7 Ko ; Interface de téléchargement, « géotiff » 1,2 Ko ; Visualisation des données, HTML 1,2 Ko) et 3 API (WMTS, WMS, WFS). Vu leurs tailles, ce sont des **liens de renvoi**, pas les données : le CSV communal fait 93 Ko sur data.gouv.fr contre 22 Mo chez le SDES. La page affiche l'alerte « Certains fichiers ne sont pas disponibles » et renvoie vers ecologie.data.gouv.fr pour des métadonnées enrichies. |
| Grain (une ligne = ?) | Un polygone d'occupation du sol homogène d'**au moins 25 ha** et 100 m de large (métropole), classé dans une nomenclature de 44 postes sur 3 niveaux (territoires artificialisés, agricoles, forêts et milieux semi-naturels, zones humides, surfaces en eau). Il existe aussi des couches de **changements** entre deux millésimes (unité minimale de 5 ha). **Fichier statistique communal (niveau 1)** : une ligne = **une commune × un millésime × une version de la base**, avec 8 colonnes : `NUM_COM` (code INSEE de la commune), `ANNEE`, `base` (exemple : « CLC 2018 », « CLC 2012 révisée »), puis `CLC_1` à `CLC_5`, la superficie en hectares de chacun des 5 postes (1 territoires artificialisés, 2 territoires agricoles, **3 forêts et milieux semi-naturels**, 4 zones humides, 5 surfaces en eau). Aucune valeur manquante. |
| Emprise géographique | 39 pays européens ; pour la France, la métropole et les DOM (pour la Guyane, seule la bande côtière est traitée, d'après data.gouv.fr). **Corse présente** dans le fichier métropole : 124 communes en Corse-du-Sud (codes `2A…`) et 236 en Haute-Corse (`2B…`), pour chaque millésime. |
| Période réellement couverte | Des photographies à date fixe : **1990, 2000, 2006, 2012 et 2018** pour la métropole (SDES), toutes présentes dans le fichier ouvert. Le millésime le plus récent décrit l'occupation du sol de 2018. **Attention : la page data.gouv.fr ne cite que 1990, 2000, 2006 et 2012** (avec les changements 1990-2000, 2000-2006 et 2006-2012) ; le millésime 2018 se trouve chez le SDES. |
| Date de dernière mise à jour affichée | Page data.gouv.fr : **17 novembre 2026** (relevée sur la fiche, champ « Dernière mise à jour », capture du 2026-11-17). Les ressources ont des dates variées : méthodologie, CSV et API WMS/WMTS « aujourd'hui » ; accès régional le 23 février 2026 ; visualisation le 5 octobre 2026 ; API WFS le 19 mars 2026. Page du SDES : publiée le 27 décembre 2018. Aucune de ces dates ne correspond à la période décrite par les données. |
| Fréquence de mise à jour | Un nouveau millésime tous les 6 ans environ (1990, 2000, 2006, 2012, 2018). Aucun millésime après 2018 n'est annoncé ; une nouvelle génération, CLC+, est en cours de production (images Sentinel à 10 m, seuil de 1 ha, cycle prévu de 3 ans). |
| Volumétrie | Fichier ouvert (`clc_etat_com_n1.csv`, 5 postes) : 23,1 Mo, **286 048 lignes** de données, 35 756 communes. Pour la Corse-du-Sud, millésime 2018 : 124 lignes, total de 403 750 ha, dont **349 029 ha de forêts et milieux semi-naturels** (86 %). Autres fichiers annoncés par le SDES : 10,03 Mo (zip, 15 postes), 13,56 Mo (zip, 44 postes). Fichiers géographiques et nombre de polygones : non vérifiés. |
| Clés disponibles | Fichiers géographiques : **la géométrie uniquement** (jointure spatiale avec Admin Express ou les points de départ de feu). Fichier statistique : `NUM_COM`, code INSEE de la commune en texte (exemple : `2A004` pour Ajaccio), **dans le code officiel géographique (COG) de 2010** (indiqué par la ligne des types : `cog_commune_2010`). **`NUM_COM` + `ANNEE` n'est pas une clé unique** (107 268 doublons) : 2000, 2006 et 2012 existent en version d'origine et en version « révisée ». La clé unique est `NUM_COM` + `base`. |
| Données personnelles | **Aucune dans le fichier statistique ouvert** : uniquement des surfaces agrégées par commune (colonnes `CLC_1` à `CLC_5`). Fichiers géographiques : non vérifiés. |
| Licence | « Licence Ouverte / Open Licence », affichée sur la page data.gouv.fr. Le numéro de version n'est pas affiché (la BD Forêt, elle, indique « version 2.0 »). |
| Questions du groupe auxquelles elle pourrait répondre | Numérotation des 4 questions communes (`docs/analyse/commande-groupe.md`, décision D-004). **Q1** (où se concentrent les départs de feu) : seulement en appui, comme dénominateur (feux rapportés à la surface boisée), et la maille de 25 ha est trop grossière à l'échelle d'une commune corse ; la BD Forêt est plus précise pour cet usage. Ne répond pas à Q2, Q3 ni Q4. **Pertinence faible : source à écarter ou à interroger.** Elle servirait surtout à comparer la surface boisée des départements, ce qu'aucune question commune ne demande pour l'instant. |

## Ce que nous avons découvert

- **La source du défi est incomplète** : la page data.gouv.fr s'arrête à 2012, alors que le millésime 2018 existe chez le SDES. Il faut prendre la donnée chez le producteur, pas sur la copie.
- **Les tailles et formats affichés par data.gouv.fr ne décrivent pas les données** : un « shape » de 4,7 Ko, un « géotiff » de 1,2 Ko, un CSV de 93 Ko. Les 3 API affichent exactement les mêmes tailles que celles de la BD Forêt (WMTS 3,0 Mo, WMS 937,0 Ko, WFS 4,6 Mo, mise à jour du 19 mars 2026) : ce sont probablement les documents de description des services de la Géoplateforme, communs à plusieurs jeux. Règle à retenir : **ne jamais estimer la volumétrie depuis le catalogue.**
- **Avantage sur la BD Forêt** : un seul millésime pour toute la France, produit avec les mêmes règles. C'est la bonne base pour comparer la surface boisée du 2A à celle des autres départements, si le groupe en a besoin un jour. La BD Forêt, elle, mélange des années de 2007 à 2018 selon les départements.
- **Question à vérifier dans la nomenclature** : le maquis a-t-il une classe propre dans le groupe « forêts et milieux semi-naturels » ? Si oui, CORINE Land Cover le distinguerait mieux que la BD Forêt, où il semble compris dans les landes.
- **Données anciennes** : 2018, soit 6 à 8 ans avant les feux étudiés (2024 à 2026).
- **Deux versions pour un même millésime** : pour 2000, 2006 et 2012, le fichier contient la version d'origine et une version « révisée » qui ne donnent pas les mêmes surfaces. Exemple, Ajaccio (`2A004`), poste 3 : 5 067,4 ha en « CLC 2012 », 4 996,7 ha en « CLC 2012 révisée ». Sommer sans filtrer sur `base` compterait ces communes deux fois.
- **Codes communes de 2010** : le fichier utilise le découpage communal de 2010 (35 756 communes), alors qu'Admin Express utilise le découpage actuel (34 877 communes). Les communes fusionnées depuis ne se joindront pas directement. En Corse, le nombre de communes est le même (124 en 2A), mais l'égalité des codes reste à contrôler.
- **Le niveau 1 ne distingue pas le maquis** : le poste 3 regroupe forêts, maquis, landes et milieux ouverts. Pour séparer le maquis, il faut le fichier détaillé à 44 postes.

## Points d'attention pour le chargement (responsable qualité)

1. **Choisir un seul millésime (2018)** et le garder en colonne, pour ne pas mélanger des époques. Filtrer sur `base = "CLC 2018"`, pas seulement sur `ANNEE`.
2. **Lire le fichier en sautant les 3 premières lignes** (libellés longs, types, unités) et prendre la 4e comme en-tête (noms courts `NUM_COM`, `ANNEE`, `base`, `CLC_1` à `CLC_5`) et lire `NUM_COM` en texte, pour ne pas perdre `2A` et `2B` ni les zéros de tête (`01001`).
3. **Passer du COG 2010 au COG actuel** avant toute jointure avec Admin Express ou la BDIFF (table de passage de l'INSEE).
4. **Unité minimale de 25 ha** : les petites parcelles boisées disparaissent dans des classes voisines. Les surfaces par commune sont des ordres de grandeur, pas des mesures fines.
5. **Ne pas additionner** CORINE Land Cover et BD Forêt : elles mesurent la même chose avec des règles différentes. Le groupe doit en retenir une par usage (proposition de décision D-008).

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Version de la Licence Ouverte | Numéro non affiché sur la page data.gouv.fr. |
| Fichiers géographiques (colonnes, système de coordonnées, nombre de polygones) | Seul le fichier statistique a été ouvert. |
| Code et libellé exacts des classes de maquis et de landes | Absents du fichier ouvert (niveau 1, 5 postes) ; il faut ouvrir le fichier à 44 postes ou la nomenclature. |
| Égalité des codes communes corses entre le COG 2010 et le COG actuel | Même nombre de communes (124 en 2A), codes non comparés un par un. |
