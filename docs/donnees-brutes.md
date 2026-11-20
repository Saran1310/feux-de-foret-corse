# Données brutes : couche bronze, licences et reproductibilité

- **Rédigé par :** Arouna TOURE (responsable pipeline)
- **Date :** 2026-11-20
- **Fichiers concernés :** `data/raw/` (couche bronze, versionnée), `data/manifeste.csv`, `src/donnees_brutes.py`, `.gitattributes`

## Principe : une copie exacte des sources, jamais modifiée

Le pipeline suit une architecture en trois couches :

- **bronze** : `data/raw/`, copie exacte des fichiers tels qu'exportés ou téléchargés ;
- **argent** : données nettoyées et enrichies (feature engineering), en gardant les valeurs d'origine à côté ;
- **or** : tables d'analyse et indicateurs du tableau de bord.

Les couches argent et or sont construites par le pipeline (ticket #23). La couche bronze n'est jamais modifiée, ni à la main ni par un script : aucune date, aucun lieu, aucune ligne ajoutée ou complétée. C'est ce qui permet de suivre l'origine de chaque chiffre (lineage) et de respecter la licence de la BDIFF (voir « Licences et citation »).

Avec l'accord de l'enseignante (20 novembre 2026), les fichiers bruts de la BDIFF sont versionnés dans le dépôt : la restriction de la licence porte sur l'usage commercial et sur la modification des données présentées comme celles de la BDIFF, pas sur une analyse faite à partir de la base.

## Les cinq fichiers de la couche bronze

| Fichier | Source | Licence | Comment l'obtenir à nouveau |
|---|---|---|---|
| `bdiff_2A_2006_2025.csv` | BDIFF, Corse-du-Sud | Droits de reproduction réservés et strictement limités | Export manuel, procédure ci-dessous |
| `bdiff_2B_2006_2025.csv` | BDIFF, Haute-Corse | Droits de reproduction réservés et strictement limités | Export manuel, procédure ci-dessous |
| `mdf_2024.csv.gz` | Archives de la Météo des forêts, saison 2024 | Licence Ouverte 2.0 (Etalab) | `python src/donnees_brutes.py telecharger` |
| `mdf_2025.csv.gz` | Archives de la Météo des forêts, saison 2025 | Licence Ouverte 2.0 (Etalab) | même commande |
| `mdf_2026.csv.gz` | Archives de la Météo des forêts, saison 2026 | Licence Ouverte 2.0 (Etalab) | même commande |

Le détail de chaque fichier (date, taille, nombre de lignes, empreinte SHA-256, critères d'export) est dans `data/manifeste.csv`.

## Vérifier que la couche bronze est intacte

Depuis la racine du dépôt :

```
python src/donnees_brutes.py verifier
```

La commande compare chaque fichier de `data/raw/` au manifeste : `OK` si le fichier est identique octet par octet à celui qui a servi aux résultats du dépôt, `DIFFERENT` ou `MANQUANT` sinon. Elle s'arrête avec un code d'erreur au moindre écart. L'empreinte SHA-256 change dès qu'un seul octet change : c'est la preuve qu'aucune valeur n'a été modifiée.

Le fichier `.gitattributes` demande à Git de ne jamais convertir les fins de ligne dans `data/raw/` : sans lui, un clone sous Windows pourrait changer les octets des CSV et casser cette vérification.

Le manifeste a été produit une seule fois avec `python src/donnees_brutes.py manifeste`, à partir des fichiers de référence. Il ne doit être régénéré que si le groupe décide de changer de données de référence (décision à consigner dans `docs/decisions.md`).

## Procédure d'export de la BDIFF

Pour refaire les exports, par exemple pour vérifier si la base a été mise à jour :

1. Ouvrir https://bdiff.agriculture.gouv.fr, partie consultation publique des incendies.
2. Saisir les critères :
   - date de première alerte du **01/01/2006** au **31/12/2025** ;
   - département **2A** (puis refaire l'export avec **2B**), un seul département par export ;
   - type de feu **F** (forêt).
3. Lancer la recherche, puis l'export. La deuxième ligne du fichier exporté indique le nombre d'incendies : **4 694** pour le 2A et **4 992** pour le 2B lors de nos exports.
4. Enregistrer le fichier CSV sans l'ouvrir dans Excel (Excel peut modifier les codes et les dates).
5. Le comparer à la couche bronze avec la commande `verifier`, après l'avoir placé dans `data/raw/` sous le même nom ; pour revenir à la version de référence ensuite : `git restore data/raw/`.

Contrôle : les trois premières lignes du fichier rappellent les critères d'export. `src/calcul_diagnostic.py` les relit et s'arrête si le département, la période ou le type de feu ne correspondent pas.

## Mises à jour des sources et impact

Les sources peuvent changer entre nos exports et l'évaluation du projet.

| Source | Ce qui peut changer | Impact |
|---|---|---|
| BDIFF | Corrections des années passées (causes complétées, surfaces revues) ; publication de l'année 2026 en 2027 | Un nouvel export peut donner d'autres nombres de feux et d'autres pourcentages que ceux du dépôt |
| Météo des forêts | Republication d'un fichier ; changement de format (déjà observé : `nom_dep` devenu `dep_nom` en 2025, séparateur point-virgule en 2026) | Résultats différents, ou échec du chargement si le format change encore |

Dates relevées pour nos fichiers de référence : sur data.gouv.fr, fichiers de la Météo des forêts mis à jour le 24 juin 2026 (saison 2024), le 25 juin 2026 (saison 2025) et le 5 octobre 2026 (saison 2026) ; dates de nos exports et téléchargements dans `data/manifeste.csv`.

Pour savoir si la Météo des forêts a changé : `python src/donnees_brutes.py telecharger --comparer` télécharge la version actuelle de chaque saison dans un dossier temporaire et la compare au manifeste, sans toucher à la couche bronze.

Si une source a changé, les fichiers du dépôt restent la référence de nos résultats. Adopter les nouvelles données est une décision du groupe : remplacer les fichiers de `data/raw/`, relancer les scripts, régénérer le manifeste et consigner la décision dans `docs/decisions.md`.

## Licences et citation

- **BDIFF** : utilisation autorisée à des fins personnelles, associatives ou professionnelles, sans vente, location ni usage commercial ou publicitaire. La reproduction doit respecter l'intégrité des données (« aucune modification, ni altération »), citer explicitement le site https://bdiff.agriculture.gouv.fr et mentionner que les droits de reproduction sont réservés et strictement limités (mentions légales du site, section 7). Dans ce dépôt : les exports sont reproduits tels quels dans la couche bronze ; tout ce qui est calculé ensuite est présenté comme « fait à partir de la base BDIFF », jamais comme la base de la BDIFF.
- **Météo des forêts** : Licence Ouverte / Open Licence version 2.0 (https://www.etalab.gouv.fr/licence-ouverte-open-licence), réutilisation libre avec mention de la source.

Mention à placer sous chaque graphique et dans le tableau de bord :

> Fait à partir de la base BDIFF, https://bdiff.agriculture.gouv.fr (droits de reproduction réservés et strictement limités), et des Archives de la Météo des forêts de Météo-France, data.gouv.fr (Licence Ouverte 2.0).
