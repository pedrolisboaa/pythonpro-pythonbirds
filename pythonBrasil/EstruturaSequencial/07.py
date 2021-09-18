"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""


def calcular_area_quadrado(lado):
    return lado * lado


def dobrar_area(area):
    return area * 2


lado = 10
area_quadrado = calcular_area_quadrado(lado)
area_dobrada = dobrar_area(area_quadrado)

print(area_dobrada)