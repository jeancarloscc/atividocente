"""Faça um algoritmo que crie dois vetores de 10 elementos gerados de forma
aleatória, cada. Depois de criar os vetores, o código deve gerar um terceiro vetor
formado pela diferença dos dois vetores originais; um quarto vetor deve ser
formado pela soma dos dois vetores originais e, por último, um quinto vetor deve
ser formado pela multiplicação dos dois vetores originais."""

import random
random.seed(42)

vetor1 = [random.randint(1, 20) for _ in range(10)]
vetor2 = [random.randint(1, 20) for _ in range(10)]

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)

vetor_diferenca = [a - b for a, b in zip(vetor1, vetor2)]
vetor_soma = [a + b for a, b in zip(vetor1, vetor2)]
vetor_multiplicacao = [a * b for a, b in zip(vetor1, vetor2)]

print("Vetor Diferença:", vetor_diferenca)
print("Vetor Soma:", vetor_soma)
print("Vetor Multiplicação:", vetor_multiplicacao)
