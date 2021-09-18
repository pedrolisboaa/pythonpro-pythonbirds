def contar_caracteres(s):
    caractere_ordenado = sorted(s)
    caractere_anterior = caractere_ordenado[0]
    contagem = 1

    for c in caractere_ordenado[1:]:
        if c == caractere_anterior:
            contagem += 1
        else:
            print(f'{caractere_anterior}: {contagem}')
            caractere_anterior = c
            contagem = 1

    print(f'{caractere_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('pedro')
    print()
    contar_caracteres('abacaxi')