"""Faça um algoritmo que leia um vetor de 10 valores inteiros e positivos. A partir
do vetor original, criar um segundo vetor da seguinte forma: os elementos de
índice par receberão os respectivos valores divididos por 2; e os elementos de
índice ímpar receberão os respectivos valores multiplicados por 3. Imprima os
dois vetores.
"""
import random
vetor = [random.randint(1, 20) for _ in range(10)]
vetor_novo = []

for i in vetor:
    if i % 2 == 0:
        par = i / 2
        vetor_novo.append(par)
    else:
        impar = i * 3
        vetor_novo.append(impar)

print("Vetor original:", vetor)
print("Vetor novo:", vetor_novo)