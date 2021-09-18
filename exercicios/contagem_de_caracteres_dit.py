def contar_caracteres(s):
    resultado = {}

    for c in s:
        contagem = resultado.get(c, 0)
        contagem += 1
        resultado[c] = contagem
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('pedro'))
    print()
    print(contar_caracteres('abacaxi'))