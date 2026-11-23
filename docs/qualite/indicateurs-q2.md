# Chiffres de la fiche d'indicateurs Q2

Genere par `src/indicateurs_q2.py` a partir de la couche or de l'entrepot. Ne pas modifier a la main.

- I1 : part des jours de declenchement sans aucun feu.
- I2 : part des feux partis hors des jours de declenchement.
- Jours vises des saisons 2024 et 2025 (du 4 juin au 1er octobre) ; feux de 2026 exclus (D-009).

## 1. Valeurs de depart (saisons 2024 et 2025)

| Departement | Regle de declenchement | Jours declenches | Dont sans feu | I1 | Feux | Feux hors declenchement | I2 |
|---|---|---|---|---|---|---|---|
| 2A | niveau_j1 >= 2 | 183 | 106 | 57.9 % | 139 | 14 | 10.1 % |
| 2A | niveau_j1 >= 3 (retenue) | 17 | 7 | 41.2 % | 139 | 126 | 90.6 % |
| 2A | niveau_j2 >= 3 (prevision a deux jours) | 1 | 0 | 0.0 % | 139 | 137 | 98.6 % |
| 2A | niveau_j1 >= 3 et niveau_j2 >= 3 | 1 | 0 | 0.0 % | 139 | 137 | 98.6 % |
| 2B | niveau_j1 >= 2 | 169 | 114 | 67.5 % | 87 | 8 | 9.2 % |
| 2B | niveau_j1 >= 3 (retenue) | 9 | 3 | 33.3 % | 87 | 79 | 90.8 % |
| 2B | niveau_j2 >= 3 (prevision a deux jours) | 0 | 0 | sans objet | 87 | 87 | 100.0 % |
| 2B | niveau_j1 >= 3 et niveau_j2 >= 3 | 0 | 0 | sans objet | 87 | 87 | 100.0 % |

## 2. Saison par saison (niveau_j1 >= 3)

| Departement | Saison | Jours declenches | Dont sans feu | I1 | Feux | Feux hors declenchement | I2 |
|---|---|---|---|---|---|---|---|
| 2A | 2024 | 3 | 0 | 0.0 % | 76 | 72 | 94.7 % |
| 2A | 2025 | 14 | 7 | 50.0 % | 63 | 54 | 85.7 % |
| 2B | 2024 | 1 | 0 | 0.0 % | 30 | 29 | 96.7 % |
| 2B | 2025 | 8 | 3 | 37.5 % | 57 | 50 | 87.7 % |

## 3. Poids d'un jour dans I1 (2A, niveau_j1 >= 3)

- 7 jours sans feu sur 17 : 41.2 % ; un jour sans feu de moins : 35.3 % ; un de plus : 47.1 %.
- Un jour pese 5.9 points sur 17 jours ; sur 10 jours, il pese 10 points ; sur 3 jours (ete 2024), 33.3 points.

## 4. Jours declenches et feux par saison (niveau_j1 >= 3)

| Departement | Saison | Jours vises | Jours declenches | Feux de l'ete | Jours avec au moins un feu |
|---|---|---|---|---|---|
| 2A | 2024 | 120 | 3 | 76 | 42 |
| 2A | 2025 | 120 | 14 | 63 | 45 |
| 2A | 2026 | 131 | 18 | exclus (D-009) | exclus (D-009) |
| 2B | 2024 | 120 | 1 | 30 | 26 |
| 2B | 2025 | 120 | 8 | 57 | 37 |
| 2B | 2026 | 131 | 9 | exclus (D-009) | exclus (D-009) |

## 5. Part des jours avec feu, jours de declenchement et autres jours (2A, saisons 2024 et 2025)

- Jours de declenchement avec feu : 10 sur 17 (58.8 %).
- Autres jours avec feu : 77 sur 223 (34.5 %).

