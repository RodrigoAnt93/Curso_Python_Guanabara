from random import randint
sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os números sorteados foram : ', end='')
for c in sorteio:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
