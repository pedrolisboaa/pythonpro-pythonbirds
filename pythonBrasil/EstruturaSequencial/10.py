"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""


def funcao_um(n1, n2):
    return (n1 * 2) + (n2 / 2)


def funcao_dois(n1, n2):
    return n1 * 3 + n2


def funcao_tres(n):
    return n ** 3



numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite um número inteiro: '))
numero_3 = float(input('Digite um número real: '))

print(funcao_um(numero_1, numero_2))
print(funcao_dois(numero_1, numero_3))
print(funcao_tres(numero_3))