print('==' * 20)
print('{: ^40}'.format(' 10 PRIMEIRAS P.A '))
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
soma = p
geral = 1
while geral < 2:
    while c < 11:
        c += 1
        print('{} '.format(soma), end='')
        print(' ► ' if c < 11 else '', end='')
        soma = soma + r
    cont = int(input('\nQuantos termos a mais você quer? '))
    cc = 0
    if cont != 0:
        while cc < cont:
            cc += 1
            print('{} '.format(soma), end='')
            print(' ► ' if cc < cont else '', end='')
            soma = soma + r
    else:
        geral += 2
        print('')
        print('O PROGRAMA FOI FINALIZADO.')
