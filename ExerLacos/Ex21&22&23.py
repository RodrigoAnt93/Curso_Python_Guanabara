num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1, 1):
    if num % c == 0:
        print(f'\033[1;32m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[1;31m{c}\033[m', end= ' ')

if cont > 2:
    print(f'\nO número {num} foi divisível {cont} vezes e por isso ele \033[1;33mNÃO É UM NÚMERO PRIMO\033[m')
else:
    print(f'\nO número {num} foi divisível {cont} vezes e por isso ele \033[1;34mÉ UM NÚMERO PRIMO\033[m')