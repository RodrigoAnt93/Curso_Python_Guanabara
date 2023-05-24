from random import randint
from time import sleep
poules = []
numeros = []
num = c = 0
print('=' * 40)
print('{:^40}'.format(' JOGO DA MEGA SENA '))
print('=' * 40)
vezes = int(input(f'Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f' SORTENDO {vezes} JOGOS ', '-=' * 3)
for sorteio in range(1, vezes + 1):
    for cont in range(1, 7):
        num = (randint(1, 60))
        while num in numeros:
            num = (randint(1, 60))
        numeros.append(num)
    poules.append(numeros[:])
    numeros.clear()
for c in range(0, vezes):
    poules[c].sort()
    print(f'Jogo {c + 1}: {poules[c]}')
    sleep(1)
print('-='*5, f' BOA SORTE! ', '-='*5)