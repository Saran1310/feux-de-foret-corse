Fiche d'identité de la source : Interventions réalisées par les services d'incendie et de secours

Rédigée par : Biolohf Tchatchoua (responsable sources)

Fichiers ouverts : les 17 CSV annuels de 2008 à 2024 (interventions2008.csv à interventions2024.csv ; 2012 = interventions__1_.csv, 2013 = interventions.csv).

Rubrique	Valeur
Propriétaire et système	Ministère de l'intérieur (page data.gouv.fr). Données collectées chaque année par la Direction générale de la sécurité civile et de la gestion des crises auprès des services d'incendie et de secours. Système producteur : non vérifiée, non indiqué sur la page.
Mode d'accès et format	Téléchargement de fichiers CSV sur data.gouv.fr (17 fichiers, un par année). Séparateur « ; », encodage Windows (cp1252).
Grain (une ligne = ?)	Un département (ou un service d'incendie) pour une année, avec des totaux par type d'intervention. Pas d'intervention individuelle, ni date, ni commune.
Emprise géographique	Plusieurs départements, dont la Corse-du-Sud (code « 2a ») et la Haute-Corse (« 2b »), présentes dans les 17 fichiers. Outre-mer présent, ainsi que des services particuliers (BMPM, BSPP). 98 à 99 lignes par fichier.
Période réellement couverte par les données	2008 à 2024. La page indique « couverture temporelle non renseignée » : la période vient des fichiers.
Date de dernière mise à jour affichée sur la fiche	2 juillet 2026 (page data.gouv.fr). Ce n'est pas la période couverte.
Fréquence de mise à jour	Collecte annuelle d'après la description de la page. Calendrier exact : non vérifiée.
Volumétrie	17 fichiers de 9 à 30 Ko, 98 à 99 lignes chacun. 70 colonnes (2008-2009), 16 colonnes (2010-2013), 71 colonnes (2014-2024).
Clés disponibles (jointures)	Année, Numéro de département (« 2a », en minuscules, plus des codes comme « BMPM » ou « BSPP »), Département, Région, Zone. Pas de code commune.
Données personnelles	Aucune colonne personnelle : uniquement des totaux d'interventions.
Licence	Licence Ouverte / Open Licence (page data.gouv.fr).
Questions de mon analyse auxquelles elle pourrait répondre	Question 1 : non (aucune localisation sous le département). Questions 2 et 3 : non (pas de jour). Question 4 : en partie, pour comparer la Corse-du-Sud, la Haute-Corse et d'autres départements par année, avec « Feux de végétations » disponible en 2008, 2009 et 2014-2024.
Contenu utile pour le projet (Corse-du-Sud)
« Feux de végétations » : 714 (2008), 894 (2009), 375 (2024). Colonne absente de 2010 à 2013 (fichiers à 16 colonnes).
« Incendies » (tous types de feux) : présente dans les 17 fichiers.
« Total interventions » : présente dans les 17 fichiers.
Limites et pièges relevés
Les colonnes changent selon les périodes : 70 colonnes (2008-2009), 16 (2010-2013), 71 (2014-2024). « Catégorie » devient « Catégorie A » à partir de 2017.
Les milliers sont séparés par une espace (« 2 247 »). Dans le fichier 2024, ce caractère apparaît sous forme de « ? » (« 1?080 »). Nettoyage nécessaire.
La Bouches-du-Rhône apparaît deux fois certaines années (service BMPM et département 13) : la notion de « département » est celle du service d'incendie, pas celle du code INSEE.
Une « intervention » n'est pas un « départ de feu de forêt » : « Incendies » regroupe tous les types de feux. À noter dans le glossaire.
Non vérifiée
Définition exacte de « Feux de végétations » et de « Catégorie A » : documentation non lue dans l'onglet Informations.
Système producteur et calendrier exact de mise à jour : non indiqués sur la page consultée.