num = int(input('Digite um numero para calcular seu fatorial: '))
print('Calculando...')
print(f'{num}!: ', end='')
valor = num
cont = 0
acumulador = 1
while valor >= 1:
    print(f'{valor}', end='')
    print(' X ' if valor > 1 else ' = ', end='' )
    acumulador *= valor
    valor -= 1
    cont += 1
print(f'{acumulador}')