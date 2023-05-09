n = int(input('Digite um número: '))
tol = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tol = tol +1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c) ,end=' ')
print('\n\033[mEsse numero se dividiu em {} vezes'.format(tol))
if tol > 2:
    print('Por isso esse numero \033[31mNÃO É PRIMO')
else:
    print('Por isso esse numero \033[32mÉ PRIMO')
