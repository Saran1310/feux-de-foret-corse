# Fiche d'identité de source : Archives de la Météo des forêts

- **Explorée par :** Arouna Touré
- **Date de l'exploration :** 2026-11-17
- **Page de la source :** https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets
- **Méthode :** lecture de la page data.gouv.fr et du contenu des trois fichiers CSV (aperçu et API tabulaire de data.gouv.fr, avec un filtre sur la Corse-du-Sud). Mise à jour le 2026-11-18 après le profilage des trois fichiers téléchargés (`src/profilage.py`, rapport `docs/qualite/profil-mdf.md`).

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | Météo-France, producteur certifié sur data.gouv.fr. La documentation renvoie au portail documentaire de Météo-France (rubrique "Données expertisées"). Système de production interne : non vérifié, il n'est pas décrit sur la page. |
| Mode d'accès et format | Téléchargement direct sur data.gouv.fr. Trois fichiers de données au format CSV compressé (.csv.gz), un par saison : 2024, 2025 et 2026. Trois fichiers de documentation : ZIP, PDF et GeoJSON des contours des départements. Les CSV sont aussi interrogeables par l'API tabulaire de data.gouv.fr. |
| Grain (une ligne = ?) | Un bulletin publié pour un département : une date et heure de publication, un département, et deux niveaux de danger de 1 à 4 (niveau prévu pour le lendemain et pour le surlendemain). Colonnes : `date`, `num_dep`, `niveau_j1`, `niveau_j2`, `nom_dep`. |
| Emprise géographique | France métropolitaine, à l'échelle du département : 96 départements (11 520 lignes pour 120 jours de bulletins en 2025). Corse-du-Sud (2A) et Haute-Corse (2B) présentes dans les trois fichiers, avec 371 bulletins chacune (profilage). Aucune donnée infra-départementale. |
| Période réellement couverte | Dates de publication relevées pour la Corse-du-Sud : du 2024-06-03 au 2024-09-30, du 2025-06-03 au 2025-09-30, du 2026-05-28 au 2026-10-05. Aucune donnée d'octobre à mai, ni avant juin 2024, alors que le dispositif existe depuis juin 2023. |
| Date de dernière mise à jour affichée | Jeu de données : 2026-10-05. Par fichier : 2026-10-05 (saison 2026), 2026-06-25 (saison 2025), 2026-06-24 (saison 2024). Documentation : 2026-09-09. Ces dates ne correspondent pas à la période couverte. |
| Fréquence de mise à jour | Un bulletin par jour pendant la saison, publié vers 16 h 50 en 2025 et 2026, à 18 h 00 en 2024. Hors saison, aucune mise à jour : data.gouv.fr affiche l'avertissement "Fréquence de mise à jour non respectée". |
| Volumétrie | 35 616 lignes et 5 colonnes au total : 11 520 lignes pour 2024, 11 520 pour 2025, 12 576 pour 2026. Tailles des fichiers téléchargés le 2026-11-18, relevées avec `Get-ChildItem` : 40 309, 43 511 et 49 870 octets (environ 39, 42 et 49 Ko) ; la page data.gouv.fr affiche 441,0 Ko, 441,0 Ko et 470,3 Ko, ce qui correspond à la taille décompressée. Pour la Corse-du-Sud seule : 371 bulletins (120, 120 et 131). |
| Clés disponibles | Code département (`num_dep`) et date. Jointures possibles avec la BDIFF (département et date du feu) et avec les référentiels géographiques (GeoJSON fourni, Admin Express). Voir les points d'attention ci-dessous. |
| Données personnelles | Aucune. Les niveaux de danger sont agrégés au département. |
| Licence | Licence Ouverte / Open Licence version 2.0 (Etalab) : réutilisation libre avec mention de la source (Météo-France). |
| Questions auxquelles elle pourrait répondre | Analyse individuelle : Q5 (part de feux couverts et de fausses alertes par seuil), Q6 (même analyse pour les grands feux), Q7 (nombre de jours d'activation par seuil), Q8 (comparaison 2A, 2B et national). Toutes nécessitent un croisement avec une base des feux. Ne répond pas à Q3 pour la période hors saison, ni à Q1 à une échelle plus fine que le département. |

## Points d'attention pour le chargement

1. **Code département non homogène.** L'Ain est codé `1` en 2024 et 2025, mais `01` en 2026. Le code doit être normalisé sur deux caractères avant toute jointure. Le profilage compte 2 160 lignes concernées (départements 1 à 9, saisons 2024 et 2025).
2. **Schéma variable selon l'année.** La colonne du nom de département s'appelle `nom_dep` en 2024 et 2026, mais `dep_nom` en 2025. Les trois fichiers doivent être harmonisés avant d'être empilés.
3. **La date est une date de publication.** La colonne `date` contient la date et l'heure de publication avec fuseau horaire (exemple dans le fichier : `2026-05-28T14:50:07Z`, soit 16 h 50 à Paris ; l'aperçu de data.gouv.fr affiche la même date convertie, `2026-05-28T16:50:07+02:00`). Le jour concerné par `niveau_j1` est le lendemain de cette date, celui concerné par `niveau_j2` le surlendemain.
4. **Dates en UTC, séparateur différent en 2026.** Les trois fichiers écrivent la date en UTC (`Z`) : `2024-06-04T16:00:00Z` (18 h 00 à Paris) en 2024, `2025-06-03T14:50:06Z` (16 h 50 à Paris) en 2025 et 2026. Les dates doivent être converties à l'heure de Paris avant d'en extraire le jour. Le séparateur change aussi : virgule en 2024 et 2025, point-virgule en 2026.
5. **Deux prévisions pour un même jour.** Chaque jour reçoit une prévision à J+2, puis une à J+1. Le groupe doit choisir laquelle sert de référence ; la prévision J+1 est proposée, car c'est elle qui sert à déclencher le dispositif.

## Ce que nous avons découvert

- L'historique est très court : trois saisons, soit 371 jours de bulletins pour la Corse-du-Sud. C'est insuffisant pour fixer un seuil sur le seul département : la comparaison avec la Haute-Corse et le niveau national devient nécessaire.
- La source est légère et facile à charger, mais elle demande un travail d'harmonisation entre les années.

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Système de production interne | Non décrit sur la page data.gouv.fr. |
| Contenu de la documentation (ZIP, PDF) | Non ouverte dans le temps de l'exercice. |
| API Météo-France "DonneesPubliquesMeteoForets" citée par le défi | Non explorée dans le temps de l'exercice. |
