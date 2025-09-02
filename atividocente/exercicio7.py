"""Escreva um algoritmo que construa uma matriz 10 por 10 de números reais e
depois de construída, colocar o conteúdo de sua diagonal principal dentro de um
vetor e depois do vetor montado, imprimir o vetor."""

import random
random.seed(42)

matriz = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]
print("Matriz 10x10:")
print(matriz)

vetor = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i] == matriz[j]:
            vetor.append(matriz[i][j])
            
            
print("Vetor construido com elementos da diagonal da matriz 10x10:")
print(vetor)