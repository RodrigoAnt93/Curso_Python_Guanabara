print('==' * 20)
print('{: ^40}'.format(' 10 PRIMEIRAS P.A '))
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
soma = p
while c < 11:
    c += 1
    print('{} '.format(soma), end='')
    print(' ► ' if c < 11 else '► ACABOU', end='')
    soma = soma + r