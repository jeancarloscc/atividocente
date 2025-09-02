"""Elabore um algoritmo que faça a soma dos elementos da diagonal secundária de
uma matriz 5 x 5. No final, exiba os elementos da diagonal secundária e a soma
deles."""
import random
random.seed(42)

matriz_1 = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
matriz_1

soma = 0
n = len(matriz_1)
for i in range(len(matriz_1)):
    for j in range(len(matriz_1[0])):
        if matriz_1[i] == matriz_1[j]:
            print(matriz_1[i][n - 1 - i])
            soma += matriz_1[i][n - 1 - i]
print(f"Soma dos elementos iguais: {soma}")