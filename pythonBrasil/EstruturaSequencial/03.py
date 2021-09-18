"""
Faça um Programa que peça dois números e imprima a soma.
"""


def soma(*args):
    somar = 0
    for i in args:
        somar += i
    return somar


print(soma(5, 5, 5, 45))