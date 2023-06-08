print('==' * 20)
print('{: ^40}'.format(' 10 PRIMEIRAS P.A '))
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        print(' ► ' if cont < 11 else '', end='')
        cont += 1
        termo = termo + r
    print('PAUSA')
    mais = int(input('\nQuantos termos a mais você quer? '))
print('FIM')
