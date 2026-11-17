# Analyse de la commande - SDIS 2A (Saison feux 2027)

* **Auteur :** Ahmed PHILIPPE
* **Commanditaire :** Direction du SDIS de la Corse-du-Sud (2A)
* **Échéance de restitution :** 11 décembre 2026

---

## 1. Questions décisionnelles

*Règle : chaque question doit orienter un arbitrage opérationnel ou budgétaire concret du SDIS 2A.*

1. **Priorisation géographique des moyens :** Quelles communes ou secteurs de Corse-du-Sud (2A) concentrent historiquement le plus grand nombre de départs de feu et les surfaces brûlées les plus importantes en période estivale ?
   * *Décision associée :* Affecter en priorité les effectifs humains (patrouilles, guet) et les moyens financiers/matériels sur les zones à plus forte sinistralité plutôt que de les répartir uniformément sur tout le département.
2. **Saisonnalité et créneaux critiques :** Quelles semaines de l'été et quelles plages horaires présentent le pic d'éclosion des feux en 2A ?
   * *Décision associée :* Concentrer le budget des renforts saisonniers sur les fenêtres temporelles critiques au lieu de maintenir un dispositif maximal sur tout l'été.
3. **Fiabilité de la météo des forêts (faux positifs et faux négatifs) :** Quel est le taux de concordance réel entre chaque niveau d'alerte de la Météo des forêts et les départs de feu constatés en Corse-du-Sud (notamment les feux survenus lorsque l'indice était au plus bas et les alertes élevées sans départ de feu) ?
   * *Décision associée :* Évaluer l'ampleur des fausses alertes (coût humain/financier inutile) et des angles morts (risque opérationnel non couvert) afin de justifier une révision du seuil de déclenchement.
4. **Calibrage du seuil de déclenchement :** À partir de quel niveau de l'indice Météo des forêts (ou quelle combinaison indice + facteurs locaux comme le vent/la sécheresse) le dispositif renforcé offre-t-il le meilleur ratio coût/couverture des départs de feu ?
   * *Décision associée :* Fixer le nouveau seuil officiel de déclenchement des patrouilles et du guet pour la saison 2027.
5. **Comparaison régionale (2A vs 2B) :** Le comportement de l'indice Météo des forêts et son pouvoir prédictif diffèrent-ils entre la Corse-du-Sud (2A) et la Haute-Corse (2B) ?
   * *Décision associée :* Déterminer si le SDIS 2A doit adopter un seuil spécifique à son territoire ou harmoniser ses règles de déclenchement à l'échelle de l'île (zone de défense / région Corse).
6. **Positionnement national :** Comment la sinistralité et la distribution des niveaux d'alerte de la Corse-du-Sud se situent-elles par rapport aux autres départements français (notamment le pourtour méditerranéen) ?
   * *Décision associée :* Argumenter les demandes de dotations budgétaires et de renforts nationaux auprès de la sécurité civile en objectivant la spécificité du risque en 2A.

---

## 2. Termes inconnus (à intégrer au glossaire du groupe)

* **SDIS 2A :** Service Départemental d'Incendie et de Secours de la Corse-du-Sud (2A).
* **Météo des forêts :** Dispositif national de prévention (porté par Météo-France et les ministères concernés) évaluant quotidiennement le niveau de danger d'incendie de forêt et de végétation par département selon une échelle de vigilance (vert, jaune, orange, rouge).
* **Indice forêt météo (IFM) :** Indicateur météorologique composite sous-jacent servant à estimer le risque d'éclosion et de propagation d'un feu à partir de la température, de l'humidité de l'air, de la vitesse du vent et des précipitations.
* **Dispositif renforcé (patrouilles, guet) :** Mobilisation préventive supplémentaire de sapeurs-pompiers, de forestiers-sapeurs ou de moyens terrestres/aériens (vigies, patrouilles de surveillance, pré-positionnement de véhicules) déclenchée avant même tout départ de feu.
* **Chef de centre :** Officier ou sous-officier commandant un Centre d'Incendie et de Secours (CIS) local au sein du maillage territorial du SDIS.
* **Départ de feu (éclosion) :** Début d'un incendie de forêt ou de végétation recensé par les secours, indépendamment de la surface finale parcourue.

---

## 3. Besoins métier et analytiques

* **Cartographie et hiérarchisation du risque en 2A :** Identifier les secteurs géographiques et les périodes où concentrer les moyens humains et financiers pour maximiser l'efficacité de la lutte préventive.
* **Audit de performance du seuil actuel :** Mesurer objectivement les écarts entre les prévisions de la Météo des forêts et la réalité du terrain (faux positifs = alerte élevée sans feu ; faux négatifs = feu déclaré malgré un indice bas).
* **Simulation de scénarios de déclenchement :** Comparer plusieurs seuils candidats pour l'été 2027 en croisant le nombre de jours d'activation (impact budgétaire et fatigue des équipes) avec le pourcentage de feux effectivement couverts.
* **Benchmark territorial (régional et national) :** Disposer d'une analyse comparative entre le 2A, le 2B et le reste de la France métropolitaine pour situer le niveau d'exposition du département.
* **Support d'aide à la décision livrable avant le 11 décembre :** Produire une restitution claire, chiffrée et argumentée permettant à la Direction du SDIS 2A d'arbitrer son budget et ses consignes opérationnelles avant le printemps 2027.

---

## 4. Données idéales recherchées

| Question / Besoin | Donnée idéale | Grain (résolution) | Période historique | Fraîcheur | Emprise géographique |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1 & 2. Localisation et temporalité des feux** | Historique des incendies de forêt et de végétation (date, heure d'alerte, commune/coordonnées, surface brûlée, cause) | Événement (1 ligne = 1 feu) / Commune / Jour | Minimum 5 à 10 dernières années (incluant l'été 2026) | Consolidée annuellement (à jour post-été 2026) | Département 2A (prioritaire), 2B et France entière |
| **3 & 4. Comportement de la Météo des forêts et calibration du seuil** | Historique quotidien des niveaux de vigilance Météo des forêts et valeurs de l'indice IFM | Jour × Département (idéalement zone météo / massif) | Toute l'historique disponible du dispositif (dont étés 2024 à 2026) | Quotidienne (archivée post-saison 2026) | Départements 2A, 2B et ensemble des départements métropolitains |
| **4. Analyse des feux par indice bas (explication météo fine)** | Observations météorologiques locales (vent moyen/rafales, humidité, température, cumul de pluie) | Horaire ou quotidienne × Station météo | 5 à 10 dernières années (incluant été 2026) | Consolidée post-été 2026 | Corse-du-Sud (2A) et Haute-Corse (2B) |
| **1 & 4. Dimensionnement et coût du dispositif renforcé** | Historique des déclenchements du dispositif renforcé du SDIS 2A (effectifs engagés, heures de patrouille/guet, coût journalier moyen) | Jour × Centre de secours (CIS) ou secteur | 3 à 5 dernières saisons estivales | Consolidée post-été 2026 | Département 2A (SDIS Corse-du-Sud) |
| **1 & 6. Contexte territorial et couverture forestière** | Occupation des sols / surfaces boisées et maillage des Centres d'Incendie et de Secours (CIS) | Commune / Département | Dernier millésime disponible | Annuelle / pluriannuelle | Corse (2A, 2B) et départements métropolitains |