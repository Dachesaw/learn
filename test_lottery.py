from random import choice

bilet_nomer = ('a', 'b', 'c', 'd', 'd', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def bilet(*args):
    bilet_nomer = str(choice(args))
    full_bilet = bilet_nomer + bilet_nomer + bilet_nomer + bilet_nomer
    return bilet_nomer
k = 0
while True:
    k += 1
    full_bilet = bilet(*bilet_nomer) + bilet(*bilet_nomer) + bilet(*bilet_nomer) + bilet(*bilet_nomer)
    if full_bilet == 'bad2':
        print(f'Выйгрышный билет: {full_bilet}\nПопытка: {k}')
        break
