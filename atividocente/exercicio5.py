"""Faça um algoritmo que leia uma matriz 4 x 4, conte e escreva quantos valores
maiores que 10 a matriz possui."""
import random
random.seed(42)

matriz = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
print("Matriz:")
for linha in matriz:
    print(linha)

cont = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 10:
            # print(matriz[i][j])
            cont += 1
print("Quantidade de elementos maiores que 10: ", cont)