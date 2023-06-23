print('{:.^40}'.format(' SEQUÊNCIA DE FIBONÁCCI! '))
num = int(input('Digite quantas vezes você quer que a sequência aconteça: '))
valor1 = valor2 = 1
print('a sequência fica assim: 0,1,1',end=',')

for c in range(4, num + 1, 1):
    valor3 = valor1 + valor2
    print(valor3, end='')
    print(',' if c < num else '.', end='')
    valor1 = valor2
    valor2 = valor3