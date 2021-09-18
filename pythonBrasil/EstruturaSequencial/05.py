"""
Faça um Programa que converta metros para centímetros.
"""


def converter_m_cm(m):
    return m * 100


metros = float(input('Quantos metros deseja converter? '))
resultado = converter_m_cm(metros)
print(f'{metros}m = {resultado}cm')
