"""Elabore um algoritmo que construa uma matriz de nome MAT de 5 linhas e 5
colunas de números inteiros. Em seguida, escreva a soma dos elementos de cada
linha e se a soma dos elementos é par ou ímpar. Por fim, escreva a soma dos
elementos de cada coluna e se a soma dos elementos é par ou ímpar."""

import random
random.seed(42)

mat = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
print("Matriz:")
for linha in mat:
    print(linha)

for linha in mat:
    soma_linha = sum(linha)
    if soma_linha % 2 == 0:
        print(f"Soma da linha {linha} é par: {soma_linha}")
    else:
        print(f"Soma da linha {linha} é ímpar: {soma_linha}")
        
for i in range(len(mat)):
    soma_linha = 0
    for j in range(len(mat[i])):
        soma_linha = soma_linha + mat[i][j]
    print(f"Soma da linha {i}: {soma_linha}")
