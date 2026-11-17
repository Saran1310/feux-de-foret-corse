# Fiche d'identité — Admin Express (IGN)

Fiche remplie par : Saran DIABAGATE
Date de vérification : 2026-11-17
Ticket : #29

Règle : une rubrique non vérifiée s'écrit « non vérifiée », avec la raison. Aucune valeur supposée.

| # | Rubrique | Valeur | Comment vérifié |
|---|---|---|---|
| 1 | Propriétaire | Institut national de l'information géographique et forestière (IGN) | Page du jeu de données sur data.gouv.fr (organisation éditrice) |
| 2 | Accès et format | Le jeu de données est sur https://www.data.gouv.fr/datasets/admin-express/. Le fichier à télécharger est un **shapefile** (lien vers geoservices.ign.fr/adminexpress). Il est aussi proposé en **services web** : 217 entrées WFS, 19 WMS, 16 WMTS. Le WFS est interrogeable sans téléchargement (data.geopf.fr/wfs/ows, couche `ADMINEXPRESS-COG.LATEST:commune`). Contenu de l'archive téléchargeable : **non vérifiée** (archive non téléchargée). | Liste des ressources sur data.gouv.fr ; requêtes réelles au WFS |
| 3 | Grain | Une ligne par **commune** (couche `commune`) et une ligne par **département** (couche `departement`). Colonnes de la couche commune : `cleabs`, `nom_officiel`, `nom_officiel_en_majuscules`, `statut`, `code_insee`, `population`, `date_du_recensement`, `organisme_recenseur`, `code_insee_du_canton`, `code_insee_de_l_arrondissement`, `code_insee_du_departement`, `code_insee_de_la_region`, `code_siren`, `codes_siren_des_epci`, `code_postal`, `superficie_cadastrale`, `geometrie`. | Message d'erreur du WFS listant les colonnes ; exemples de lignes lus |
| 4 | Emprise | France métropolitaine et départements d'outre-mer (description du producteur). Couche commune : 34 877 communes. Corse-du-Sud (`2A`) : 124 communes. | Description data.gouv.fr ; `numberMatched` du WFS (34 877 et 124) |
| 5 | Période réelle | Le jeu de données déclare une couverture du **2017-01-01 au 2026-10-15** (plusieurs éditions annuelles, par exemple `ADMINEXPRESS-COG.2017` à `.2024`). Chaque édition est une photographie de l'état administratif à une date : il n'y a pas d'historique à l'intérieur d'une édition. La population affichée porte la date de recensement `2023-01-01`. | Champ « couverture temporelle » de data.gouv.fr ; valeurs lues dans les lignes |
| 6 | Date de mise à jour | **2026-10-19** (dernière mise à jour du jeu de données). Les ressources ont été modifiées jusqu'au 2026-11-05. | data.gouv.fr |
| 7 | Fréquence de mise à jour | **Mensuelle** (`monthly`) | data.gouv.fr |
| 8 | Volumétrie | 34 877 lignes dans la couche commune (WFS), dont 124 en Corse-du-Sud. Taille du fichier à télécharger : **non vérifiée** (taille non indiquée par data.gouv.fr, archive non téléchargée). | WFS (`numberMatched`) |
| 9 | Clés de jointure | `code_insee` pour la commune (exemple : `2A006` pour Alata). `code_insee_du_departement` pour le département : la Corse-du-Sud s'écrit `2A` (texte, pas un nombre). | Lignes réelles lues dans le WFS |
| 10 | Données personnelles | Aucune dans les colonnes observées de la couche commune (entités administratives, populations agrégées, codes). Autres couches : **non vérifiée**. | Liste des colonnes |
| 11 | Licence | Licence Ouverte v2.0 (identifiant `lov2` sur data.gouv.fr) | data.gouv.fr |
| 12 | Questions auxquelles elle répond | Source de référence pour **localiser** : rattacher un événement à sa commune et à son département (Q1, où se concentrent les départs de feu) et séparer la Corse-du-Sud (`2A`) de la Haute-Corse (`2B`) et du reste de la France (Q4). Elle ne contient aucune donnée sur les feux ni sur la météo. | Questions retenues dans `docs/analyse/commande-groupe.md` |

## Points de vigilance

- Les codes `2A` et `2B` sont du texte. Un tableur ou une lecture automatique peut les transformer (par exemple lire `2A` comme une date) : à lire en texte.
- Le jeu de données contient plusieurs éditions et plusieurs variantes (ADMIN EXPRESS, COG, COG CARTO, CARTO PE, CARTOPLUS PE). Il faudra noter laquelle on utilise.
- Le système de coordonnées du shapefile n'est **pas vérifié** (le WFS renvoie des coordonnées en longitude/latitude).

## Sources consultées

- https://www.data.gouv.fr/datasets/admin-express/
- Service WFS de l'IGN : https://data.geopf.fr/wfs/ows (couches `ADMINEXPRESS-COG.LATEST:commune` et `:departement`)