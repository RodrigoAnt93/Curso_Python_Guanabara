from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
opc = int(input('Quantos jogadores? '))
for sorte in range(0, opc):
    jogadores[f"Joador{sorte+1}"] = randint(1, 6)
rank = []
for k, v in jogadores.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('~~' * 20)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(rank):
    print(f'O {c+1}° lugar foi {v[0]} com {v[1]}')



