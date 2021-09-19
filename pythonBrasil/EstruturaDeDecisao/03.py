"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""


def calcular_ir(salario):
    if salario <= 900:
        return 0
    if salario <= 1500:
        return salario * 0.05
    if salario <= 2500:
        return salario * 0.1

    return salario * 0.2


valor = float(input('Informo o valor da sua hora de trabalho: '))
hora = float(input('Quantas horas você trabalho esse mês: '))

salario_bruto = valor * hora
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
ir = calcular_ir(salario_bruto)
total_de_desconto = inss + ir
salario_liquido = salario_bruto - total_de_desconto

print(f'Salário Bruto {valor} * {hora} - R$ {salario_bruto}')
print(f'(-) IR ------------------------- R$ {ir}')
print(f'(-) INSS ----------------------- R$ {inss}')
print(f'FGTS --------------------------- R$ {fgts}')
print(f'Total de descontos ------------- R$ {total_de_desconto}')
print(f'Salário Liquido ---------------- R$ {salario_liquido}')

