def soma(*args):
    auxiliar = 0
    for i in args:
        auxiliar += i

    return auxiliar


def f(*args, **kwargs):
    print(args)
    print(kwargs)


args = (1, 2, 3, 4, 56)
kwargs = {'nome': 'Pedro', 'sobrenome': 'Lisboa'}

print(soma(5, 5, 5, 5))
f(1, 2, 3, nome='Pedro', sobrenome='Lisboa')
print(f(*args, **kwargs))