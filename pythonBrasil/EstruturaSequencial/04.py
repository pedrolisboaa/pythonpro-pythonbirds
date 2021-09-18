"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def media_bimestral(notas):
    return notas / 4


def somar_notas(*args):
    somar = 0
    for i in args:
        somar += i
    return somar

if __name__ == '__main__':

    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    nota3 = int(input('Digite a nota 3: '))
    nota4 = int(input('Digite a nota 4: '))

    soma_total = somar_notas(nota1, nota2, nota3, nota4)
    print(media_bimestral(soma_total))
