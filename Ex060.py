num = int(input('Digite um numero para calcular se fatorial: '))
c = num
f = 1
print('')
print('O valor fatorial de {}! é:'.format(num))
while c >= 1:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(' {}'.format(f))