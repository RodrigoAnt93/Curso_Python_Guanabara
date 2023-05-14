num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
