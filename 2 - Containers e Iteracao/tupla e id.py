tupla = (1, 2, 3, 4, 5, 6, 8, 9, 10)
tupla2 = tuple(range(1, 50, 5))
tupla_unica = (10,)

print(tupla2)
print(tupla_unica)

tupla_nome = ('Pedro', 'Lisboa')
nome, sobrenome = tupla_nome

print(nome)
print(sobrenome)

tupla3 = tupla + tupla2
print(tupla3)
print(id(tupla3))