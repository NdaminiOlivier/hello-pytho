import os
M1 = [
    [1, 2, 4],
    [12, 8, 0],
    [7, 4, 6]
]
print("La matrice M1 est :", M1)

#determinons le nombre de colonne de la matrice

colonne1 = []
for Oli in M1:
    colonne1.append(Oli[0])
m = 0
print(colonne1)
for q in M1:
    m += 1
print("le nombre de colonne de la matrice est: ", m)
k = 0

for ligne in range(len(M1)):
    petitLigne = min(M1[ligne])
    while k < m:
        M1[ligne][k] = M1[ligne][k] - petitLigne
        k += 1

print("la matrice reduite est: ", M1)
print(colonne1)





