print('=' * 30)
print('{: ^30}'.format(' BANCO COLESTEROL '))
print('=' * 30)
print('')
valor = int(input('Qual valor você quer sacar? R$'))
valtotal = valor
valced = 50
totalced = 0

while True:
    if valtotal >= valced:
        valtotal -= valced
        totalced += 1
    else:
        if totalced > 0:
            print('Você sacou {} notas de R${}'.format(totalced, valced))
        if valced == 50:
            valced = 20
        elif valced == 20:
            valced = 10
        elif valced == 10:
            valced = 1
        totalced = 0
        if valtotal == 0:
            break
