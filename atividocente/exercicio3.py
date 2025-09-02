"""Escreva um algoritmo que realiza a soma de duas matrizes 2 x 3."""

import random
random.seed(42)
matriz_1 = [[random.randint(1, 20) for _ in range(3)] for _ in range(2)]
matriz_2 = [[random.randint(1, 20) for _ in range(3)] for _ in range(2)]

print("Matriz 1:")
for linha in matriz_1:
    print(linha)

print("Matriz 2:")
for linha in matriz_2:
    print(linha)

resultado = [[random.randint(0, 0) for _ in range(3)] for _ in range(2)]
for linha in resultado:
    print(linha)

for i in range(len(matriz_1)):
    for j in range(len(matriz_1[0])):
        resultado[i][j] = matriz_1[i][j] + matriz_2[i][j]

for r in resultado:
    print(r)
