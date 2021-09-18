"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""


def calcular_salario(valor_hora, hora_trabalhada):
    salario = str(round(valor_hora * hora_trabalhada, 2)).replace('.', ',')
    return salario


total_de_horas_mes = float(input('Quantas horas você trabalha no mês: '))
valor_por_hora = float(input('Quanto ganha por hora: '))
resultado = calcular_salario(total_de_horas_mes, valor_por_hora)

print(resultado)