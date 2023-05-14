print('~~' * 30)
print('Vamos jogar PAR ou IMPAR!')
print('~~' * 30)
vit = 0
from random import randint
while True:
    np = int(input('Digite o valor: '))
    pi = str(input('Você que par ou impar P/I? ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Opção inválida. Você que par ou impar P/I? ')).strip().upper()[0]
    cpu = randint(0, 10)
    soma = cpu + np
    if pi == 'P':
        if soma % 2 == 0:
            print(f'A CPU jogou {cpu} e você jogou {np}. Total de {soma} é PAR')
            print('--' * 30)
            print('Você acertou!')
            print('Vamos jogar novamente...')
            print('~~' * 30)
            vit += 1
        else:
            print(f'A CPU jogou {cpu} e você jogou {np}. Total de {soma} é IMPAR')
            print('VOCÊ PERDEU!')
            print('--' * 30)
            break
    elif pi == 'I':
        if soma % 2 != 0:
            print(f'A CPU jogou {cpu} e você jogou {np}. Total de {soma} é IMPAR')
            print('--' * 30)
            print('Você acertou!')
            print('Vamos jogar novamente...')
            print('~~' * 30)
            vit += 1
        else:
            print(f'A CPU jogou {cpu} e você jogou {np}. Total de {soma} é PAR')
            print('VOCÊ PERDEU!')
            print('--' * 30)
            break

print(f'GAMASSE NO OVO! Mas você acertou {vit} vezes')
