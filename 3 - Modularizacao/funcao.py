def falar_ola():
    return 'Olá mundo!'


def gritar_seu_nome(nome):
    return f'{nome.upper()}!!!!!!'


def calcular_imc(peso=0, altura=0):
    imc = peso / altura ** 2
    return f'Seu IMC = {imc:.2f}'


falar = falar_ola()
print(falar)

imc = calcular_imc(130, 1.90)
print(imc)

gritar_nome = gritar_seu_nome('Pedro')
print(gritar_nome)