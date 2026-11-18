# Fiche d'identité de source : Données feux de forêt en Corse du Sud (DDT 2A)

- **Explorée par :** Arouna Touré
- **Date de l'exploration :** 2026-11-17
- **Page de la source :** https://www.data.gouv.fr/datasets/donnees-feux-de-foret-en-corse-du-sud-de-1973-a-2025-pour-les-departs-de-feux-et-de-1949-a-2025-pour-les-contours-de-feux
- **Méthode :** lecture de la page data.gouv.fr, des métadonnées complètes du jeu (API data.gouv.fr) et du service de téléchargement WFS. L'archive complète (shapefile) n'a pas pu être ouverte dans l'environnement d'exploration : les colonnes ci-dessous viennent de la documentation du producteur.
- **Pourquoi cette source :** complément de la BDIFF pour la Corse-du-Sud. La BDIFF localise les feux à la commune et commence en 2006 ; cette source donne la position du point de départ et remonte à 1973. Elle intègre les données de la BDIFF depuis le 1er janvier 2023.

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | Créateur : DDT 2A (Direction départementale des territoires de Corse-du-Sud). Diffuseur : DDTM Corse-du-Sud, organisation certifiée sur data.gouv.fr. Données moissonnées depuis le catalogue Géo-IDE du ministère. Sources amont selon la documentation : levés de terrain DDT 2A, ONF (programme Marittimo, projet MEDSTAR), base Prométhée, OPENDFCI2A (2021-2022), puis BDIFF depuis 2023 (alimentée par le SIS 2A et la DDT 2A). |
| Mode d'accès et format | Téléchargement de l'archive complète du lot (service Atom, format shapefile). Services cartographiques WMS et WFS. Le WFS ne propose que cinq couches : deux grilles DFCI et trois couches de contours de feux (1949-1980, 1981-1989, 1990-2024). **La couche des points de départ n'est pas servie en WFS** : elle n'est disponible que dans l'archive. Un second lien de téléchargement pointe vers un réseau interne de l'administration et n'est pas accessible au public. |
| Grain (une ligne = ?) | Deux couches principales : **un point de départ de feu** (point d'éclosion) et **un contour de feu** (polygone de surface brûlée). Attributs documentés : numéro Prométhée, identifiant `ID_DDT2A` (numéro Prométhée et date, exemple `6512-1991-05-26`), `SOURCE`, `CODE_CAR` (carreau DFCI), `MODIF`, `LIEU-DIT`, type de feu (`FF` feu de forêt, `AFERPU` autres feux urbains ou péri-urbains), nature de la cause. Liste exacte des colonnes : non vérifiée (archive non ouverte). |
| Emprise géographique | **Corse-du-Sud uniquement** (emprise relevée dans les métadonnées : longitude 8,44 à 9,49, latitude 41,33 à 42,39). Ni la Haute-Corse, ni le reste de la France. |
| Période réellement couverte | Points de départ : **1973 à 2024** selon la description du jeu et le service WFS ; le titre annonce 2025, ce qui n'est pas confirmé. Contours : de 1949 à 2024 d'après le nom des couches WFS (dernière couche : du 1990-01-01 au 2024-12-31) ; 2025 non confirmé. **La précision de localisation varie selon la période** : 1973-1980, centre de la commune ; 1981-1989, centre d'un carreau de 2 km ; 1990-2021, centre d'un sous-carreau de 1 km ou relevé de terrain ; depuis 2021, exports OPENDFCI2A puis BDIFF. |
| Date de dernière mise à jour affichée | Jeu de données : 2026-05-27. Fichiers de téléchargement : 2024-11-15. Services WMS et WFS : 2025-05-20 et 2025-05-21. Ces dates ne correspondent pas à la période couverte. |
| Fréquence de mise à jour | Non renseignée par le producteur ("unknown" dans les métadonnées). Mise à jour annuelle supposée d'après l'historique : non vérifiée. |
| Volumétrie | Non vérifiée : l'archive n'a pas pu être ouverte et sa taille n'est pas indiquée sur la page. |
| Clés disponibles | Identifiant `ID_DDT2A`, numéro Prométhée, date du départ de feu, carreau DFCI (`CODE_CAR`) et géométrie (coordonnées en Lambert 93, EPSG:2154). Jointures possibles : avec la Météo des forêts par la date (département implicite 2A), avec Admin Express par jointure spatiale (point dans commune), avec la grille DFCI par `CODE_CAR`. Présence d'un code commune : non vérifiée. |
| Données personnelles | Aucune donnée nominative décrite dans la documentation. Point de vigilance : localisation précise des départs, lieux-dits et causes (dont les causes volontaires) ; à vérifier à l'ouverture et à agréger avant diffusion. |
| Licence | Licence Ouverte / Open Licence version 2.0 (Etalab). Pas de restriction d'accès public selon INSPIRE. |
| Questions auxquelles elle pourrait répondre | Analyse individuelle : **Q1** et **Q2** (zones de concentration des départs et leur stabilité, sur plus de 50 ans), **Q3** (périodes de l'année, y compris hors saison), **Q4** (causes), **Q6** (grands feux, grâce aux contours), **Q10** (comparaison de 2026 avec l'historique, sous réserve que 2025 et 2026 soient intégrés). En croisement avec la Météo des forêts : Q5 et Q7 pour 2024. Ne répond pas à Q8 (pas de Haute-Corse ni de national). |

## Points d'attention pour le chargement

1. **Précision spatiale hétérogène.** Avant 1990, les points sont placés au centre d'une commune ou d'un carreau de 2 km. Une analyse par commune reste possible ; une analyse plus fine n'est fiable qu'à partir de 1990.
2. **Changement de classification en 2023.** La documentation signale un changement dans les types de feux (`FF` et `AFERPU`) depuis 2023 : les séries avant et après 2023 ne sont pas directement comparables.
3. **Couverture récente incertaine.** Le titre annonce 2025, mais la description et le service WFS s'arrêtent à 2024. L'été 2026 est probablement absent, alors que la commande y fait référence.
4. **Service WFS défectueux.** Une requête sur la couche des contours 1990-2024 renvoie un XML invalide (le nom de la couche contient un espace). Le chargement devra passer par l'archive téléchargée.

## Ce que nous avons découvert

- C'est la source la plus riche pour **localiser les départs de feu en Corse-du-Sud** : plus de 50 ans d'historique, avec cause, source et carreau DFCI.
- Elle complète la BDIFF pour le 2A (localisation ponctuelle, historique depuis 1973, contours des grands feux), mais **ne la remplace pas** pour la comparaison avec la Haute-Corse et le niveau national.
- Les incohérences de période entre le titre, la description et le service (2024 ou 2025) devront être vérifiées à l'ouverture de l'archive.

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Liste exacte des colonnes, présence d'un code commune | Archive shapefile non ouverte dans l'environnement d'exploration ; colonnes reprises de la documentation du producteur. |
| Volumétrie | Archive non ouverte, taille non affichée. |
| Fréquence de mise à jour | Non renseignée par le producteur. |
| Présence des feux de 2025 et 2026 | Titre et description contradictoires ; à vérifier à l'ouverture. |
