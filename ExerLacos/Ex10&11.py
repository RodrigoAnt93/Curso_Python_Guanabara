num1 = int(input('Digite o primero número: '))
num2 = int(input('Digite o último número: '))
soma = 0
print('Os números que compõem o espaço do primeiro e o último numeros são:')
for c in range (num1 + 1, num2, 1):
    print(c, end=' ')
    soma += c
print(f'\nE a soma de todos esses números é {soma}')