linguas = {'br': 'portugues', 'eua': 'ingles'}

print(linguas)
print(linguas['br'])

linguas['es'] = 'espanhol'

print(linguas)


for chave in linguas.keys():
    print(chave)

for valor in linguas.values():
    print(valor)

for chave, valor in linguas.items():
    print(chave, valor)
