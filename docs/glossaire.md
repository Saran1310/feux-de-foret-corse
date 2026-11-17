# Glossaire — Corse

Dernière mise à jour : 2026-11-17

## BDIFF

- **Définition :** Base de données nationale sur les incendies de forêt en France, tenue par l'IGN et le ministère de l'Agriculture. Elle recense chaque feu avec sa date, sa commune, sa surface et sa cause.
- **Sources et colonnes :** BDIFF (IGN / ministère de l'Agriculture) : date, commune, surface, cause. Noms de colonnes à relever à l'ouverture de la source.
- **Divergences :** Elle n'a pas de coordonnées précises, et l'heure et la cause sont à vérifier. Ses définitions et ses seuils de surface peuvent différer de ceux de Prométhée et des interventions du SDIS (voir « Feu de forêt »).
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un feu, rattaché à une commune. Couverture : France, depuis 2006.
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna. À confirmer dans la documentation de la BDIFF.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Chef de centre

- **Définition :** Officier ou sous-officier qui commande un centre d'incendie et de secours (une caserne) du SDIS. Ce sont des chefs de centre qui disent à la direction que l'indice annonce souvent un danger élevé sans feu, et que des feux partent certains jours où l'indice est au plus bas.
- **Sources et colonnes :** Aucune donnée : c'est un témoignage de la commande, à interroger.
- **Divergences :** Leurs constats sont des impressions, pas des chiffres. Il faut les vérifier avec les données (voir « Fausse alerte / feu manqué »).
- **Règle retenue :** sans objet
- **Unité ou granularité :** Un centre d'incendie et de secours (CIS).
- **Exemple :** À demander au SDIS : quels centres et quels jours ont été cités.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles d'Ahmed et d'Arouna, et commande du SDIS 2A.
- **Ajouté par :** Ahmed PHILIPPE et Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## CODIS

- **Définition :** Centre opérationnel départemental d'incendie et de secours : il coordonne les interventions du département.
- **Sources et colonnes :** Aucune donnée identifiée. Il peut être la porte d'entrée pour les données d'intervention du SDIS.
- **Divergences :** Aucune divergence repérée. Le terme n'apparaît que dans l'analyse d'Arouna.
- **Règle retenue :** sans objet
- **Unité ou granularité :** Un centre par département.
- **Exemple :** À demander au SDIS.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna. À confirmer avec le SDIS.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Concentration des moyens

- **Définition :** Affectation prioritaire des moyens humains et financiers du SDIS sur certaines zones ou certaines périodes, parce que le budget ne permet pas de renforcer le dispositif partout, tout l'été. C'est la première question de la commande.
- **Sources et colonnes :** Aucune donnée : les moyens réellement disponibles et les critères de répartition sont à demander au SDIS.
- **Divergences :** La commande ne dit pas ce qu'est une zone prioritaire. Les critères utilisés par le SDIS sont inconnus.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une zone ou une période (à préciser).
- **Exemple :** À demander au SDIS.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyse individuelle de Saran.
- **Ajouté par :** Saran DIABAGATE, 2026-11-17

## Danger élevé

- **Définition :** Niveau de danger de feu de forêt annoncé par la Météo des forêts. Quand un chef de centre dit que l'indice « annonce un danger élevé », il faut préciser de quel niveau il parle.
- **Sources et colonnes :** Archives de la Météo des forêts (Météo-France, data.gouv.fr) : niveau par département et par jour. Nom de colonne à relever.
- **Divergences :** La carte compte 4 niveaux : 1 vert (faible), 2 jaune (modéré), 3 orange (élevé), 4 rouge (très élevé). « Danger élevé » peut désigner le niveau 3 seul, ou les niveaux 3 et 4. À trancher avec le SDIS, car le seuil actuel est l'objet de la commande.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un niveau (1 à 4) par département et par jour.
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles de Tchatchoua, d'Arouna et d'Ahmed. À confirmer dans la documentation de Météo-France.
- **Ajouté par :** Biolohf TCHATCHOUA, Arouna TOURE et Ahmed PHILIPPE, repris par Saran DIABAGATE, 2026-11-17

## Danger et risque

- **Définition :** Le danger est ce que mesure la météo : des conditions favorables au feu. Le risque est la probabilité qu'un feu parte réellement. Un danger élevé ne veut pas dire qu'un feu va se déclarer.
- **Sources et colonnes :** Notion transversale : elle concerne le niveau de la Météo des forêts et les feux de la base des incendies.
- **Divergences :** Arouna insiste sur cette différence : la plupart des départs sont d'origine humaine. Ahmed décrit l'IFM comme un indicateur du risque d'éclosion. Voir « IFM ».
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Sans objet.
- **Exemple :** Un jour de danger élevé sans aucun feu.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles d'Arouna et de Saran (remarque sur les données).
- **Ajouté par :** Arouna TOURE et Saran DIABAGATE, 2026-11-17

## Départ de feu

- **Définition :** Début d'un incendie de forêt ou de végétation recensé par les secours, quelle que soit la surface brûlée au final (éclosion). C'est l'expression utilisée par la direction du SDIS dans sa commande.
- **Sources et colonnes :** Base des feux (BDIFF, Prométhée) et interventions du SDIS : date, commune, surface. À identifier.
- **Divergences :** La direction parle de départs de feu, une source recense des feux de forêt, une autre des interventions pour incendie. Ce ne sont peut-être pas les mêmes événements. Voir « Feu de forêt ».
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un événement (un départ de feu), avec sa date et sa localisation.
- **Exemple :** À trouver dans une source.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyses individuelles de Saran et d'Ahmed.
- **Ajouté par :** Saran DIABAGATE et Ahmed PHILIPPE, 2026-11-17

## Département

- **Définition :** Territoire administratif de la Corse (2A Corse-du-Sud, 2B Haute-Corse), identifié par un code INSEE. C'est aussi l'échelle à laquelle la Météo des forêts donne son niveau de danger.
- **Sources et colonnes :** Limites administratives (Admin Express, IGN) : codes département et commune.
- **Divergences :** Le périmètre du SDIS 2A peut ne pas être le même que celui du département. Il faut utiliser des codes cohérents : 2A et 2B, pas 20 (ancien code de la Corse).
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un département (2A ou 2B).
- **Exemple :** 2A = Corse-du-Sud ; 2B = Haute-Corse.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles de Tchatchoua et d'Arouna.
- **Ajouté par :** Biolohf TCHATCHOUA et Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## DFCI

- **Définition :** Défense des forêts contre l'incendie : l'ensemble des aménagements de prévention, comme les pistes, les points d'eau et le débroussaillement.
- **Sources et colonnes :** Aucune source identifiée à ce stade.
- **Divergences :** Aucune divergence repérée. Le terme n'apparaît que dans l'analyse d'Arouna et reste à lier à la question de la prévention.
- **Règle retenue :** sans objet
- **Unité ou granularité :** Sans objet.
- **Exemple :** À trouver.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Dispositif renforcé

- **Définition :** Mobilisation supplémentaire du SDIS pendant les périodes à risque : patrouilles, guet, pré-positionnement de véhicules, avec des moyens terrestres ou aériens. Il est déclenché avant tout départ de feu. C'est ce que la direction veut déclencher à partir d'un certain niveau de l'indice.
- **Sources et colonnes :** Aucune source publique. Les déclenchements, les effectifs et le coût journalier sont à demander au SDIS (données internes).
- **Divergences :** La commande ne précise pas ce que le dispositif contient exactement, ni ce qu'il coûte par jour. Les « patrouilles renforcées » n'en sont qu'une partie.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une journée de dispositif, par zone ou par centre (à préciser).
- **Exemple :** À demander au SDIS.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A, analyses individuelles de Tchatchoua, d'Arouna, d'Ahmed et de Saran. À confirmer avec le SDIS.
- **Ajouté par :** Biolohf TCHATCHOUA, Arouna TOURE, Ahmed PHILIPPE et Saran DIABAGATE, 2026-11-17

## Emprise géographique

- **Définition :** Territoire couvert par une donnée ou une analyse, par exemple la Corse-du-Sud seule, la Corse entière ou toute la France.
- **Sources et colonnes :** Chaque source : colonnes de commune, de département ou de zone.
- **Divergences :** Le niveau géographique change selon la source : la Météo des forêts est au département, la BDIFF à la commune, les stations météo sont des points, le zonage de danger est un découpage infra-départemental.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Commune, département ou zone, selon la source.
- **Exemple :** À trouver dans chaque source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle de Saran (colonne « emprise » du tableau des données).
- **Ajouté par :** Saran DIABAGATE, 2026-11-17

## Fausse alerte / feu manqué

- **Définition :** Une fausse alerte est un jour où l'indice annonce un danger élevé sans qu'aucun feu ne parte. Un feu manqué est un feu qui part un jour où l'indice était bas. Ce sont les deux problèmes signalés par les chefs de centre dans la commande.
- **Sources et colonnes :** À construire en croisant les niveaux de la Météo des forêts avec la base des feux, par jour et par zone.
- **Divergences :** Les termes « faux positif » et « faux négatif » viennent des analyses d'Arouna et d'Ahmed. Ils ne sont pas dans la commande. Pour compter, il faut d'abord décider ce que sont un « danger élevé » et un « feu ».
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un jour et un département.
- **Exemple :** À calculer à partir des données.
- **Statut :** proposé
- **Origine de la définition :** Analyses individuelles d'Arouna et d'Ahmed, et commande du SDIS 2A.
- **Ajouté par :** Arouna TOURE et Ahmed PHILIPPE, repris par Saran DIABAGATE, 2026-11-17

## Feu de forêt

- **Définition :** Incendie qui touche un espace boisé ou de végétation. C'est le terme des bases de données, à ne pas confondre avec les « départs de feu » de la direction ni avec les interventions pour incendie.
- **Sources et colonnes :** BDIFF, Prométhée et interventions du SDIS 2A. À comparer.
- **Divergences :** Les définitions et les seuils de surface diffèrent selon les bases : feu de forêt ou feu de végétation, taille minimale, types de feux comptés. À harmoniser avant de compter.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un feu.
- **Exemple :** À trouver dans une source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles d'Arouna et de Tchatchoua, et commande du SDIS 2A.
- **Ajouté par :** Biolohf TCHATCHOUA et Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Guet (GAAr)

- **Définition :** Surveillance de terrain : vigies fixes ou guet aérien. Le GAAr est le guet aérien armé, avec des avions bombardiers d'eau qui volent en surveillance.
- **Sources et colonnes :** Aucune source identifiée. À demander au SDIS.
- **Divergences :** L'analyse d'Arouna marque cette définition « à vérifier ». La commande cite le guet sans le définir.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un moyen de surveillance, par jour et par zone.
- **Exemple :** À demander au SDIS.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna et commande du SDIS 2A.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## IFM (Indice Forêt Météo)

- **Définition :** Indice d'origine canadienne qui estime le danger de feu à partir de la météo : température, humidité de l'air, vent, précipitations et sécheresse de la végétation. La Météo des forêts s'appuie dessus. Il est aussi appelé « indice de danger ».
- **Sources et colonnes :** Météo-France (valeur de l'indice par point ou par zone). Colonne exacte à identifier.
- **Divergences :** Arouna dit qu'il mesure un danger météo, pas la probabilité qu'un feu soit allumé. Ahmed parle d'un indicateur du risque d'éclosion et de propagation. Il existe aussi des indices opérationnels (IFMx, indice de danger intégré) fournis à la Sécurité civile, différents de la carte grand public. À trancher avec la documentation de Météo-France.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une valeur numérique par jour et par zone (à vérifier).
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyses individuelles d'Arouna, d'Ahmed et de Saran. À confirmer dans la documentation de Météo-France.
- **Ajouté par :** Arouna TOURE, Ahmed PHILIPPE et Saran DIABAGATE, 2026-11-17

## Météo des forêts

- **Définition :** Dispositif national de Météo-France qui annonce le niveau de danger de feux de forêt et de végétation, par département, sur une échelle de 4 niveaux (vert, jaune, orange, rouge), pour le jour suivant (J+1) et le surlendemain (J+2), pendant l'été.
- **Sources et colonnes :** Archives de la Météo des forêts sur data.gouv.fr : niveau par département et par jour. Noms de colonnes à relever.
- **Divergences :** La carte publique existe depuis juin 2023, mais les archives disponibles ne commencent qu'en juin 2024 d'après Arouna. Elle ne fonctionne que de juin à septembre et ne donne rien en dehors. Il faut décider quelle prévision on utilise (J+1 ou J+2) : d'après Arouna, c'est J+1 qui sert à déclencher le dispositif. Les chefs de centre trouvent que l'indice annonce souvent un danger élevé sans feu.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un niveau (1 à 4) par département, par jour de prévision et par échéance.
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyses individuelles de Saran, de Tchatchoua, d'Arouna et d'Ahmed. À confirmer dans la documentation de Météo-France.
- **Ajouté par :** Saran DIABAGATE, Biolohf TCHATCHOUA, Arouna TOURE et Ahmed PHILIPPE, 2026-11-17

## OLD

- **Définition :** Obligations légales de débroussaillement : ce que les propriétaires doivent débroussailler autour des constructions.
- **Sources et colonnes :** Aucune source identifiée à ce stade.
- **Divergences :** Aucune divergence repérée. Le terme n'apparaît que dans l'analyse d'Arouna.
- **Règle retenue :** sans objet
- **Unité ou granularité :** Sans objet.
- **Exemple :** À trouver.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Patrouilles renforcées

- **Définition :** Augmentation de la surveillance sur le terrain dans certaines zones pendant les périodes à risque. Elles font partie du « dispositif renforcé » demandé par le SDIS.
- **Sources et colonnes :** Aucune source identifiée. À demander au SDIS.
- **Divergences :** Le SDIS ne précise pas ce que contient exactement le dispositif renforcé (patrouilles, guet, etc.). Conditions de déclenchement à vérifier avec la direction.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une zone et une période (à préciser).
- **Exemple :** À demander au SDIS.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyse individuelle de Saran. À confirmer avec le SDIS.
- **Ajouté par :** Saran DIABAGATE, 2026-11-17

## PPFENI

- **Définition :** Plan de protection des forêts et des espaces naturels contre les incendies.
- **Sources et colonnes :** Aucune source identifiée à ce stade.
- **Divergences :** Aucune divergence repérée. Le terme n'apparaît que dans l'analyse d'Arouna.
- **Règle retenue :** sans objet
- **Unité ou granularité :** Sans objet.
- **Exemple :** À trouver.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Prométhée

- **Définition :** Base de données des incendies de forêt des 15 départements méditerranéens, dont la Corse-du-Sud et la Haute-Corse, depuis 1973. Elle est gérée par la Délégation à la protection de la forêt méditerranéenne.
- **Sources et colonnes :** Prométhée : incendies détaillés et causes. Noms de colonnes à relever.
- **Divergences :** Les conditions d'accès sont à vérifier. Les causes ont été peu renseignées en Corse. Ses définitions et seuils de surface peuvent différer de ceux de la BDIFF (voir « Feu de forêt »).
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un feu.
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna. À confirmer dans la documentation de Prométhée.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17

## Saison feux

- **Définition :** Période de l'été pendant laquelle le SDIS s'attend aux feux de forêt. La commande vise la saison 2027, que la direction attend aussi active que celle de 2026, voire davantage.
- **Sources et colonnes :** La Météo des forêts n'existe que de juin à septembre. Les dates exactes de la saison sont à confirmer avec le SDIS.
- **Divergences :** Les dates de la saison ne sont pas définies dans la commande. Les feux peuvent aussi arriver hors de la période où l'indice est publié.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une saison (une année).
- **Exemple :** Saison 2026 : à utiliser comme référence.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyse individuelle d'Arouna.
- **Ajouté par :** Saran DIABAGATE et Arouna TOURE, 2026-11-17

## SDIS 2A

- **Définition :** Service départemental d'incendie et de secours de la Corse-du-Sud (2A). C'est le client du projet. Le SDIS 2B est celui de la Haute-Corse.
- **Sources et colonnes :** Données d'intervention internes, à demander (non publiques).
- **Divergences :** Le territoire du SDIS et le département (code 2A) peuvent ne pas coïncider. Voir « Département ».
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Un service d'incendie, couvrant un département.
- **Exemple :** SDIS 2A = Corse-du-Sud ; SDIS 2B = Haute-Corse.
- **Statut :** à vérifier
- **Origine de la définition :** Commande du SDIS 2A et analyses individuelles de Saran, d'Ahmed et d'Arouna. À confirmer avec le SDIS.
- **Ajouté par :** Saran DIABAGATE, Ahmed PHILIPPE et Arouna TOURE, 2026-11-17

## Zonage infra-départemental

- **Définition :** Découpage d'un département en zones de danger météo, utilisé pour réguler l'accès aux massifs. Il est plus fin que le niveau départemental de la Météo des forêts.
- **Sources et colonnes :** Zonage de danger météorologique (Météo-France / État) : polygones par zone. À identifier.
- **Divergences :** Les polygones n'ont pas d'historique de niveau, donc on ne peut pas y rattacher les feux passés. L'indice n'existe qu'au grain du département.
- **Règle retenue :** à décider par le groupe (à consigner dans le journal des décisions)
- **Unité ou granularité :** Une zone (polygone).
- **Exemple :** À trouver dans la source.
- **Statut :** à vérifier
- **Origine de la définition :** Analyse individuelle d'Arouna. À confirmer dans la documentation de Météo-France.
- **Ajouté par :** Arouna TOURE, repris par Saran DIABAGATE, 2026-11-17