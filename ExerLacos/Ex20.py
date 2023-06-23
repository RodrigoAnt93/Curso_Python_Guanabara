num = 0
valor = 0
cont = 0
acumulador = 1
while True:
    num = int(input('Digite um numero para calcular seu fatorial: '))
    if num > 16 or num < 0:
        print('Opção inválida!')
        num = int(input('Digite um numero para calcular seu fatorial: '))
    elif num <= 16 or num > 0:
        valor = num
        while valor >= 1:
            print(f'{valor}', end='')
            print(' X ' if valor > 1 else ' = ', end='' )
            acumulador *= valor
            valor -= 1
    print(f'{acumulador}')
    print('')
    num = valor = 0
    acumulador = 1