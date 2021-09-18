"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def fahrenheit_to_celsius(temperatura):
    return 5 * ((temperatura - 32) / 9)


resultado = fahrenheit_to_celsius(120)
print(resultado)