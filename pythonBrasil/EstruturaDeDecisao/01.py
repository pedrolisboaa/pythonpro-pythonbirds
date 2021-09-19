"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
vogais = ['a', 'e', 'i', 'o', 'u']

letra = input('Digite uma letra: ')

if letra.lower() in vogais:
    print('VOGAL!')
else:
    print('CONSOANTE!')