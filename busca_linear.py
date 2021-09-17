"""
Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado.
 O programa deve retornar o índice onde o valor foi encontrado, ou -1, caso não encontre o valor.
"""

tamanho_lista = int(input('Digite o tamanho da sua lista:'))
lista = []

for i in range(tamanho_lista):
    inserir_lista = int(input('Digite o número que deseja inserir na lista: '))
    lista.append(inserir_lista)

buscar_na_lista = int(input('Digite número que deseja buscar na lista: '))

if buscar_na_lista in lista:
    print(f'O {buscar_na_lista} está no range {lista.index(buscar_na_lista)}')
else:
    print(-1)
