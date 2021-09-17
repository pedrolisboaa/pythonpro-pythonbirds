"""
Escreva um programa que cria uma lista de 100 números aleatórios inteiros ordenados e solicita 
um número para o usuário. Use a busca binária para encontrar a posição do número fornecido na lista, 
ou retorne -1 se ele não for encontrado.
"""

#Funções
def numero_aleatorio():
    from random import randint
    numero_aleatorio = randint(1, 1000)
    return numero_aleatorio 

def organizar_lista(lista):
    return sorted(lista)

# algoritmo de busca binária
def busca_binaria(lista, x):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    
    return -1


# Applicação
lista = []

while len(lista) < 100:
    numero = numero_aleatorio()
    if not numero in lista:
        lista.append(numero)


lista_organizada = organizar_lista(lista)
resposta = busca_binaria(lista_organizada, 100)
print(resposta)
