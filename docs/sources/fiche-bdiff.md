# Fiche d'identité de source : BDIFF (Base de données sur les incendies de forêt en France)

- **Explorée par :** Arouna Touré
- **Date de l'exploration :** 2026-11-17
- **Page de la source :** https://bdiff.agriculture.gouv.fr/
- **Fichier ouvert :** export CSV de la consultation publique, avec les critères suivants : date de première alerte du 2006-01-01 au 2025-12-31, département 2A, type de feu "F" (forêt). Documents consultés : page d'accueil, "Mentions légales" et "Définitions" (PDF du site).

## Fiche

| Rubrique | Valeur |
|----------|--------|
| Propriétaire et système | Éditeur : ministère de l'Agriculture et de la Souveraineté alimentaire (sous-direction filières forêt-bois). Conception, développement et hébergement : IGN (hébergeur OVH). La base est alimentée par un réseau de contributeurs ; en Corse-du-Sud, le SIS 2A et la DDT 2A (d'après la documentation de la DDT 2A). |
| Mode d'accès et format | Consultation publique sans compte ("Consultation des incendies"), avec export en CSV. Format relevé : séparateur point-virgule, encodage UTF-8, **trois lignes d'en-tête descriptives** (avertissement, nombre de résultats, critères de sélection) avant la ligne des noms de colonnes. |
| Grain (une ligne = ?) | **Un incendie**, localisé à la commune. 24 colonnes, dont : `Année`, `Numéro`, `Département`, `Code INSEE`, `Nom de la commune`, `Date de première alerte` (date et heure), `Surface parcourue (m2)`, surfaces par type de végétation, `Précision des surfaces`, `Type de peuplement`, `Nature` (cause), dégâts et décès. |
| Emprise géographique | France entière selon la page d'accueil ("territoire français"), à l'échelle de la commune. Export réalisé sur la Corse-du-Sud : 124 communes distinctes. Haute-Corse et national : non extraits à ce stade. |
| Période réellement couverte | Base alimentée depuis 2006. Export 2A : du 2006-01-11 au 2025-12-24. **Le public n'a accès qu'aux données "jusqu'à l'année antérieure à l'année en cours"** (page d'accueil) : la saison 2026 n'est pas disponible en novembre 2026. |
| Date de dernière mise à jour affichée | Non vérifiée : aucune date de mise à jour n'est affichée sur la page d'accueil consultée. |
| Fréquence de mise à jour | Collecte continue de l'année en cours par les contributeurs ; diffusion publique annuelle (année N-1). |
| Volumétrie | Export 2A, 2006-2025, feux de forêt : **4 694 incendies**, 24 colonnes, 474 Ko. Entre 407 (2006) et 86 (2023) incendies par an ; 93 en 2025. Volume national : non vérifié. |
| Clés disponibles | `Code INSEE` de la commune (format texte, exemple `2A004` pour Ajaccio) et `Date de première alerte`. **`Numéro` seul n'est pas unique** (766 doublons) : la clé unique est le couple `Année` + `Numéro` (0 doublon). Jointures possibles : avec la Météo des forêts par département et date, avec Admin Express par code INSEE (attention au millésime du code officiel géographique). |
| Données personnelles | Aucune dans l'export : pas de nom de personne, localisation à la commune seulement. Point de vigilance : la cause "Malveillance" et les décès éventuels sont des informations sensibles, à n'utiliser qu'en agrégé. Les mentions légales rappellent que toute donnée à caractère nominatif doit être utilisée conformément aux recommandations de la CNIL. |
| Licence | **Pas de licence ouverte.** Les mentions légales autorisent l'utilisation à des fins personnelles, associatives ou professionnelles, à condition de : ne pas vendre ni louer les données, respecter leur intégrité ("aucune modification, ni altération"), citer explicitement le site comme source, et mentionner que les droits de reproduction sont réservés. Toute utilisation commerciale ou publicitaire est exclue. |
| Questions auxquelles elle pourrait répondre | Analyse individuelle : **Q1 et Q2** (communes qui concentrent les feux, et leur stabilité sur 20 ans), **Q3** (mois, jour et heure d'alerte, y compris hors saison), **Q4** (causes, avec réserve sur la complétude), **Q6** (grands feux, grâce à la surface parcourue), **Q10** (comparaison des saisons, sans 2026). En croisement avec la Météo des forêts : **Q5 et Q7**. **Q8** possible en refaisant l'export pour la Haute-Corse et le national. |

## Points d'attention pour le chargement

1. **En-tête du fichier.** Les trois premières lignes du CSV ne sont pas des données : il faut les ignorer à la lecture (par exemple `skiprows=3` en Python).
2. **Clé unique.** `Numéro` se répète d'une année à l'autre : utiliser le couple `Année` + `Numéro`.
3. **Changement de formulaire en 2023.** Le fichier l'annonce ("ancienne version du formulaire incendie") et la documentation le confirme : les colonnes de surface par végétation ne sont pas les mêmes avant et après 2023. Exemple : `Précision des surfaces` est vide à 100 % avant 2023 et remplie à 100 % depuis ; `Surfaces non boisées (m2)` suit le chemin inverse. Seule `Surface parcourue (m2)` est complète sur toute la période.
4. **Colonnes vides ou codées.** Quatre colonnes sont entièrement vides dans l'export (`Surface autres terres boisées`, `Surfaces non boisées naturelles`, `Surfaces non boisées artificialisées`, `Précision de la donnée`), ainsi que le détail des décès et des bâtiments. `Type de peuplement` est codé de 1 à 6 sans libellé : la correspondance avec la liste de la documentation reste à confirmer.
5. **Unités.** Les surfaces sont en mètres carrés (et non en hectares) : 1 ha = 10 000 m2.

## Ce que nous avons découvert

- **46,5 % des feux de Corse-du-Sud partent hors de la saison de la Météo des forêts** (2 185 feux sur 4 694 entre octobre et mai). Près de la moitié des départs n'ont donc aucun niveau de danger associé : c'est une limite majeure pour la question du seuil, et une piste d'explication des "feux partis quand l'indice était au plus bas".
- **La cause est inconnue pour 47 % des feux** (2 212 sur 4 694). Parmi les causes connues, "Involontaire (particulier)" arrive en tête (1 003), devant "Malveillance" (767).
- **Les feux sont concentrés** : Ajaccio (327), Porto-Vecchio (317) et Sartène (265) totalisent près de 20 % des départs sur 20 ans.
- **Peu de grands feux** : la surface médiane est de 200 m2 ; 472 feux dépassent 1 ha et 18 dépassent 50 ha.
- **Recouvrement avec la Météo des forêts très faible** : seulement 139 feux en juin-septembre 2024 et 2025, les deux saisons communes aux deux sources.
- **La saison 2026 manque** : elle ne sera publiée qu'en 2027, après la date de rendu.
- **La licence n'est pas ouverte** : l'exigence d'intégrité ("aucune modification") est à discuter avec l'enseignante, puisque le pipeline transforme les données.

## Rubriques non vérifiées

| Rubrique | Raison |
|----------|--------|
| Date de dernière mise à jour | Aucune date affichée sur la page d'accueil consultée. |
| Volumétrie nationale, données de la Haute-Corse | Export limité au département 2A ; à refaire pour 2B et pour la France. |
| Libellés du champ `Type de peuplement` | Codes 1 à 6 sans libellé dans l'export ; correspondance avec la documentation à confirmer. |
