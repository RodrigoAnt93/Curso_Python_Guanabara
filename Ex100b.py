def contador(* num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print('-' * 40)
    print(f'Os números da lista são ', end='')
    for c in num:
        print(f'{c} ', end='')
    print('')
    print(f'A soma dos valores pares de {num} é {soma}')


contador(1, 5, 2, 7, 8)
contador(5, 6, 7, 8)
contador(2, 6)
contador(2)