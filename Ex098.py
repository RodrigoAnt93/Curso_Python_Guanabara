from time import sleep


def rept(i, m, f):
    if f == 0:
        f += 1
    if f < 0:
        f = abs(f)
    if i > m:
        print(f'Contagem de {i} a {m} de {f} em {f}:')
        for c in range(i, m - 1, -f):
            print(f'{c} ', end='')
            sleep(0.8)
        print('Fim!')
    elif m > i:
        print(f'Contagem de {i} a {m} de {f} em {f}:')
        for c in range(i, m + 1, f):
            print(f'{c} ', end='')
            sleep(0.8)
        print('Fim!')


print('=-' * 20)
print('Contagem de 1 a 10 de 1 em 1:')
for c in range(1, 11):
    print(f'{c} ', end='')
    sleep(0.5)
print('Fim!')
print('=-' * 20)
print("Contagem de 10 a 0 de 2 em 2:")
for c in range(10, 0, -2):
    print(f'{c} ', end='')
    sleep(0.5)
print('Fim!')
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem:')
ini = int(input('INÍCIO: '))
mei = int(input('MEIO: '))
fim = int(input('FIM: '))
print('_' * 50)
rept(ini, mei, fim)