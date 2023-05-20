from random import choice

bilet_nomer = ('a', 'b', 'c', 'd', 'd', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def bilet(*args):
    bilet_nomer = str(choice(args))
    return bilet_nomer

win_tic = bilet(*bilet_nomer) + bilet(*bilet_nomer) + bilet(*bilet_nomer) + bilet(*bilet_nomer)
print(win_tic.upper())


