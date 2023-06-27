while True:
    num = int(input('Digite um número para saber se ele é primo: '))
    if num <= 2:
        print(f'O número {num} \033[1;32mÉ UM NÚMERO PRIMO\033[m')
    if num > 2:
        if num % 2 == 0:
            print(f'O número {num} \033[1;31mNÃO É UM NÚMERO PRIMO\033[m')
        elif num % 3 == 0:
            print(f'O número {num} \033[1;31mNÃO É UM NÚMERO PRIMO\033[m')
        else:
            print(f'O número {num} \033[1;32mÉ UM NÚMERO PRIMO\033[m')
    print('')