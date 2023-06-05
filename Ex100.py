from random import randint


def soma(val):
    soma_pares = 0
    for c in val:
        if c % 2 == 0:
            soma_pares += c
    print(f'A soma dos valores pares de {val} é {soma_pares}')
    print('_' * 40)


while True:
    opc = int(input('Quantos números você quer sortear? '))
    num = []
    for c in range(0, opc):
        num.append(randint(1, 9))
    print(f'Sorteando {len(num)} números e foram: ', end='')
    for c in num:
        print(f'{c} ', end='')
    print('')
    soma(num)