import os
os.system('cls')
lista = [1, 3, 7, 2, 7, 8, 9, 4, 6, 3]
pares = []
impares = []
for x in lista:
    if x % 2 == 0:
       pares.append(x)
    else:
       impares.append(x)
print("LISTA ORIGINAL: ", lista)
print("LISTA PARES   : ", pares)
print("LISTA IMPARES : ", impares)
