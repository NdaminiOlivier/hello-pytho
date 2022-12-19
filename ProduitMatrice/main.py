'''M = [[3,1,5],[9,8,-1],[10,12,2]]
print("M = ",M)
col3 = []
for ligne in M:
    col3.append(ligne[2])
print("col3 = ", col3)'''
M1 = [[1,2],[1,1],[0,4]]
M2 = [[1,1,5]]


M2 = [4]*5

print()
M3 = [[0 for i in range(5)] for i in range(5)]
for element in M3:
    print(element)
print()
M2[2] = 3
print(M2)
print()
M3[1][1] = 2
for element in M3:
    print(element)
print()

Col = [M3[i][-1] for i in range(len(M3))]
'''if len(M1) == len(M2[0]):
    print("M1 = ",M1)
    print("M2 = ",M2)
    print("le produit matriciel ne peut se faire car le nombre de colonne de la premiere n est as égal au nombre de lignes de la deuxieme")
'''