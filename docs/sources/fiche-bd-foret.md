# Fiche d'identité de source : BD Forêt® (version 2)

- **Explorée par :** Ahmed Philippe
- **Date de l'exploration :** 2026-11-17
- **Page de la source :** https://www.data.gouv.fr/datasets/bd-foret-r
- **Méthode :** lecture de la page data.gouv.fr (onglets « Fichiers » et « Informations », captures du 2026-11-17), de la fiche du producteur sur cartes.gouv.fr (catalogue de l'IGN : description, aperçu cartographique, ressources et liens), de la notice départementale de la BD Forêt V2 pour la Corse-du-Sud (IGN, diffusée sur le géoportail de la Corse, geo.isula.corsica) et d'une présentation de l'IGN sur ses données forestières (janvier 2021). **Aucun fichier de données ouvert à ce stade** : les rubriques qui en dépendent sont marquées « non vérifiée ».

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | IGN (Institut national de l'information géographique et forestière). Données produites par photo-interprétation des images aériennes infrarouge couleur de la BD ORTHO®. Le jeu provient d'un portail externe (cartes.gouv.fr, jeu `IGNF_BD-FORET`), moissonné par data.gouv.fr. Contact : contact.geoservices@ign.fr. |
| Mode d'accès et format | Deux voies. **1) Téléchargement** : la page data.gouv.fr propose « Télécharger BD Forêt® V1 - V2 » (annoncé comme shapefile de 112,8 Ko, ce qui est la taille d'une page de renvoi, pas des données) et « Documentation BD Forêt® » (PDF, 1,2 Ko) ; le vrai téléchargement passe par le lien « BD FORET® – Téléchargement » de cartes.gouv.fr. Format et taille des fichiers départementaux : non vérifiés. **2) Services web** : 6 API listées sur data.gouv.fr (WMTS, WMS et WFS pour la V1 et la V2). La couche WFS de la V2 s'appelle `LANDCOVER.FORESTINVENTORY.V2:formation_vegetale` ; elle permettrait d'interroger directement les polygones d'une zone sans télécharger tout le département (à tester). Documentation : descriptifs de contenu et de livraison (PDF) en lien sur cartes.gouv.fr. |
| Grain (une ligne = ?) | Un polygone de végétation homogène (« plage cartographiée ») d'au moins 0,5 ha (5 000 m²), auquel est attribué un type de formation végétale. Attributs annoncés par l'IGN : `ID`, `CODE_TFV` (code du type de formation végétale), `TFV` (libellé), `TFV_G11` (regroupement en 11 classes), `ESSENCE`. Présence exacte de ces colonnes dans le fichier : non vérifiée. |
| Emprise géographique | France métropolitaine, produite et livrée par département. Corse-du-Sud (2A) : couverte (notice départementale). Haute-Corse (2B) : toute l'île apparaît couverte sur l'aperçu cartographique de cartes.gouv.fr, à confirmer dans le fichier. Grain géographique : le polygone ; aucun code commune annoncé. |
| Période réellement couverte | **Une photographie à une date, pas une série.** Au niveau national, la V2 assemble des millésimes de 2007 à 2018 selon les départements. Pour la Corse-du-Sud : photographies aériennes de **2011**, données diffusées en **2017** (notice IGN). Millésime 2B : non vérifié. |
| Date de dernière mise à jour affichée | Page data.gouv.fr, onglet « Informations » : **17 novembre 2026** (création de la fiche : 1er avril 2022). Les ressources ont des dates différentes : lien de téléchargement mis à jour il y a 12 jours, documentation il y a 20 jours, couche WFS de la V2 le 13 mai 2026. Sur cartes.gouv.fr : « publié il y a plus de 4 ans ». Ces dates concernent le catalogue et les liens, pas les données (photos de 2011 pour le 2A). |
| Fréquence de mise à jour | **Contradictoire selon le catalogue** : « Sans régularité » sur data.gouv.fr, « Mise à jour continue » sur cartes.gouv.fr. Dans les faits, la V2 n'est plus reproduite : l'IGN prépare une V3, et publie depuis 2025 un « Masque Forêt v1 » plus récent (images 2021 à 2023), qui localise les surfaces de forêt. Son niveau de détail par rapport à la BD Forêt reste à vérifier. |
| Volumétrie | Pour la Corse-du-Sud, la surface cartographiée est de 371 670 ha pour un département de 403 739 ha (notice IGN). Nombre de polygones et taille des fichiers : non vérifiés (fichier non ouvert). |
| Clés disponibles | Aucune clé administrative annoncée (pas de code commune ni de code département dans les attributs listés par l'IGN ; le département est porté par le découpage des fichiers). Jointure possible uniquement **par la géométrie** : croisement spatial avec les limites communales ou départementales (Admin Express) ou avec les points de départ de feu. |
| Données personnelles | Non vérifiée : aucun fichier n'a encore été ouvert. D'après la documentation de l'IGN, les polygones décrivent la couverture végétale, pas les propriétaires ; à confirmer à l'ouverture du fichier. |
| Licence | Licence Ouverte / Open Licence version 2.0 (Etalab), affichée sur la page data.gouv.fr. |
| Questions du groupe auxquelles elle pourrait répondre | Numérotation des 4 questions communes (`docs/analyse/commande-groupe.md`, décision D-004). **Q1** (où se concentrent les départs de feu) : en appui, pour calculer la surface boisée par commune et rapporter les départs de feu à la forêt exposée. Elle ne répond à aucune question seule : elle sert de **dénominateur** aux indicateurs construits avec la base des feux. Ne répond pas à Q2, Q3 ni Q4. |

## Ce que nous avons découvert

- **Ordre de grandeur pour la Corse-du-Sud** (notice IGN, photos de 2011) : taux de boisement de 79 %. La forêt fermée couvre 276 095 ha (68 %), la forêt ouverte 42 213 ha (10 %), les landes 53 362 ha (13 %), les autres couvertures 32 069 ha (8 %).
- **Le maquis n'apparaît pas sous ce nom** : il est probablement compris dans « landes » (dont la classe « lande ligneuse », 49 884 ha). Ce point compte pour nous : si une part importante des feux corses touche le maquis (à vérifier dans la base des feux), rapporter les feux à la « forêt » seule sous-estimerait la surface exposée. À trancher dans le glossaire (terme « Feu de forêt »).
- **Décalage temporel** : les données décrivent la végétation de 2011, alors que les feux à analyser datent surtout de 2024 à 2026. Les zones brûlées entre-temps ont pu changer de couverture.
- **Trois périodes différentes pour la même donnée** : la description parle d'une production de 2007 à 2018 ; l'onglet « Informations » de data.gouv.fr affiche une couverture du 1er janvier 2006 au 1er avril 2022 ; cartes.gouv.fr nomme ses couches « BD Forêt v2 (2006-2019) ». Aucune ne dit quelle année décrit la Corse : seule la notice départementale le fait (2011). Règle à retenir : **toujours lire le millésime du département, jamais la période globale du catalogue.**
- **Fréquence contradictoire** entre les deux catalogues (« sans régularité » contre « mise à jour continue »), alors que la V2 n'est plus reproduite.
- **Le fichier « shapefile » de data.gouv.fr n'en est pas un** : 112,8 Ko, la même taille que la « fiche produit » HTML. C'est un lien de renvoi vers le catalogue de l'IGN.

## Points d'attention pour le chargement (responsable qualité)

1. **Pas de clé administrative** : il faut une jointure spatiale avec Admin Express (même millésime du COG que les autres sources).
2. **Millésime différent selon le département** : une comparaison entre départements mélangerait des photos de 2007 à 2018. Le millésime de chaque département doit être conservé comme colonne.
3. **Périmètre « forêt » à définir** : décider quelles classes de `TFV` comptent comme surface exposée (forêt fermée, forêt ouverte, landes ?). C'est une décision de groupe à consigner dans le journal.

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Données personnelles | Aucun fichier ouvert ; la documentation seule ne suffit pas à l'affirmer. |
| Format exact et liste réelle des colonnes | Fichier départemental non ouvert ; colonnes connues seulement par la documentation IGN. |
| Volumétrie (nombre de polygones, taille) | Fichier non ouvert. |
| Couverture et millésime de la Haute-Corse (2B) | Notice départementale 2B non consultée. |
| Système de coordonnées utilisé pour la Corse | Non indiqué dans les documents lus ; à lire dans le fichier `.prj`. |
| Descriptif de contenu officiel (BD Forêt® version 2.0) | Lien repéré sur cartes.gouv.fr, document non lu. |
| Fichiers par département (nom, format, taille) | Le lien « BD FORET® – Téléchargement » de cartes.gouv.fr ne s'est pas ouvert depuis un téléphone le 2026-11-17 ; à refaire depuis un ordinateur. |
