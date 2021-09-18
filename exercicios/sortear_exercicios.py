"""
Utilizado para sortear exercicios em uma lista:
"""
from random import randint

numero_de_atividades = int(input('Quantas atividades possuem na lista? '))
quantas_vai_fazer = int(input('Quantas atividades deseja fazer: '))

lista_para_fazer = []

while len(lista_para_fazer) < quantas_vai_fazer:
    atividade_numero = randint(1, numero_de_atividades)

    if atividade_numero not in lista_para_fazer:
        lista_para_fazer.append(atividade_numero)

print(sorted(lista_para_fazer))
