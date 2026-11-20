# Calculs du diagnostic et de l'objectif KPI

Genere par `src/calcul_diagnostic.py` a partir des fichiers bruts de `data/raw/`.

## Volet seuil : Meteo des forets x BDIFF

### Corse-du-Sud (2A)

- Jours vises : 240 (du 2024-06-04 au 2025-10-01, saisons 2024 et 2025)
- Criteres de l'export BDIFF : Critères de sélection => ; Date de première alerte, de : 2006-01-01 00:00:00 ; Date de première alerte, jusqu'à : 2025-12-31 23:59:00 ; Département(s) : 2A ; Type de feu : F
- Feux ces jours-la : 139
- Feux sur juin-septembre calendaire 2024 et 2025 (periode de la matrice) : 139

| Niveau niveau_j1 | Jours | Jours avec au moins un feu | Part des jours avec feu | Feux |
|---|---|---|---|---|
| 1 | 57 | 10 | 17.5 % | 14 |
| 2 | 166 | 67 | 40.4 % | 112 |
| 3 | 17 | 10 | 58.8 % | 13 |
| 4 | 0 | 0 | sans objet | 0 |

- Jours de danger eleve (niveau_j1 >= 3) : 17, dont sans aucun feu : 7 (41.2 %) ; avec un jour sans feu de moins ou de plus : 35.3 % ou 47.1 %
- Feux partis un jour de danger faible (niveau_j1 = 1) : 14 sur 139 (10.1 %)

| Regle de declenchement | Jours declenches | Dont sans feu | Feux hors declenchement |
|---|---|---|---|
| niveau_j1 >= 2 | 183 | 106 (57.9 %) | 14 (10.1 %) |
| niveau_j1 >= 3 | 17 | 7 (41.2 %) | 126 (90.6 %) |
| niveau_j1 >= 3 et niveau_j2 de la veille >= 3 | 1 | 0 (0.0 %) | 137 (98.6 %) |
| niveau_j1 >= 4 | 0 | 0 (sans objet) | 139 (100.0 %) |

- Jours de danger eleve par saison (toutes saisons de l'indice) : 2024 : 3, 2025 : 14, 2026 : 18

Detail par saison (feux et jours declenches) :

| Seuil | Saison | Jours declenches | Feux couverts | Part des feux couverts |
|---|---|---|---|---|
| niveau_j1 >= 2 | 2024 | 71 | 62 sur 76 | 81.6 % |
| niveau_j1 >= 2 | 2025 | 112 | 63 sur 63 | 100.0 % |
| niveau_j1 >= 2 | 2026 | 128 | feux exclus (ticket #61) | sans objet |
| niveau_j1 >= 3 | 2024 | 3 | 4 sur 76 | 5.3 % |
| niveau_j1 >= 3 | 2025 | 14 | 9 sur 63 | 14.3 % |
| niveau_j1 >= 3 | 2026 | 18 | feux exclus (ticket #61) | sans objet |

### Haute-Corse (2B)

- Jours vises : 240 (du 2024-06-04 au 2025-10-01, saisons 2024 et 2025)
- Criteres de l'export BDIFF : Critères de sélection => ; Date de première alerte, de : 2006-01-01 00:00:00 ; Date de première alerte, jusqu'à : 2025-12-31 23:59:00 ; Département(s) : 2B ; Type de feu : F
- Feux ces jours-la : 87
- Feux sur juin-septembre calendaire 2024 et 2025 (periode de la matrice) : 88

| Niveau niveau_j1 | Jours | Jours avec au moins un feu | Part des jours avec feu | Feux |
|---|---|---|---|---|
| 1 | 71 | 8 | 11.3 % | 8 |
| 2 | 160 | 49 | 30.6 % | 71 |
| 3 | 9 | 6 | 66.7 % | 8 |
| 4 | 0 | 0 | sans objet | 0 |

- Jours de danger eleve (niveau_j1 >= 3) : 9, dont sans aucun feu : 3 (33.3 %) ; avec un jour sans feu de moins ou de plus : 22.2 % ou 44.4 %
- Feux partis un jour de danger faible (niveau_j1 = 1) : 8 sur 87 (9.2 %)

| Regle de declenchement | Jours declenches | Dont sans feu | Feux hors declenchement |
|---|---|---|---|
| niveau_j1 >= 2 | 169 | 114 (67.5 %) | 8 (9.2 %) |
| niveau_j1 >= 3 | 9 | 3 (33.3 %) | 79 (90.8 %) |
| niveau_j1 >= 3 et niveau_j2 de la veille >= 3 | 0 | 0 (sans objet) | 87 (100.0 %) |
| niveau_j1 >= 4 | 0 | 0 (sans objet) | 87 (100.0 %) |

- Jours de danger eleve par saison (toutes saisons de l'indice) : 2024 : 1, 2025 : 8, 2026 : 9

Detail par saison (feux et jours declenches) :

| Seuil | Saison | Jours declenches | Feux couverts | Part des feux couverts |
|---|---|---|---|---|
| niveau_j1 >= 2 | 2024 | 67 | 25 sur 30 | 83.3 % |
| niveau_j1 >= 2 | 2025 | 102 | 54 sur 57 | 94.7 % |
| niveau_j1 >= 2 | 2026 | 119 | feux exclus (ticket #61) | sans objet |
| niveau_j1 >= 3 | 2024 | 1 | 1 sur 30 | 3.3 % |
| niveau_j1 >= 3 | 2025 | 8 | 7 sur 57 | 12.3 % |
| niveau_j1 >= 3 | 2026 | 9 | feux exclus (ticket #61) | sans objet |

- Jours de danger eleve, Corse-du-Sud et Haute-Corse ensemble (saisons communes) : 26

## Volet zones : BDIFF par commune

### Concentration et stabilite des feux par commune (Corse-du-Sud)

- Feux : 4694 (2006-2025), communes touchees : 124
- Trois premieres communes : Ajaccio 327, Porto-Vecchio 317, Sartène 265, soit 909 feux (19.4 %)
- Part des feux dans les 10 premieres communes : 38.5 %
- Nombre de communes pour atteindre la moitie des feux : 17 sur 124 (13.7 %)
- Feux 2006-2015 : 3009 ; feux 2016-2025 : 1685
- Communes presentes dans les 10 premieres des deux periodes : 8 (Ajaccio, Sartène, Porto-Vecchio, Zonza, Appietto, Alata, Bonifacio, Bastelica)
- Correlation de rang de Spearman entre les deux periodes (toutes communes, nombre de feux par commune) : 0.89
- Surface brulee : trois premieres communes : Fozzano 3227 ha, Quenza 3221 ha, Sartène 1321 ha, soit 7769 ha sur 13133 (59.2 %) ; hors des 20 communes qui ont le plus de feux : Fozzano, Quenza
