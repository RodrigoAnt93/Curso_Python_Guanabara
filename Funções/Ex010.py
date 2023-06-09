from random import randint
from time import sleep
d1 = randint(1, 6)
d2 = randint(1, 6)
d_t = d1 + d2
print('{:-^40}'.format(' JOGO DE CRAPS '))
sleep(1)
print('Jogando o primeiro dado...', end='')
sleep(2)
print(f'Caiu {d1}')
sleep(1)
print('Jogando o segunda dado...', end='')
sleep(2)
print(f'Caiu {d2}')
sleep(2.5)
print(f'Você conseguiu um numero {d_t}.')
print('_' * 30)
sleep(0.8)
list_ponto = []
if d_t == 7 or d_t == 11:
    print(f'Você consegiu um número {d_t} e com isso venceu o jogo! \033[1;32mPARABÉNS!!!')
elif d_t == 2 or d_t == 3 or d_t == 12:
    print(f'Você consegiu um número {d_t} e com isso você \033[1;31mPERDEU\033[m o jogo. Que pena...')
else:
    print('''Humm... Você conseguiu um PONTO!! 
Agora você vai ter que jogar os dados mais vezes até conseguir os números (4, 5, 6, 8, 9, 10)
Se você tirar um "7" antes de conseguir esses números, você perde.''')
    print('_' * 90)
    sleep(10)
    while True:
        d3 = randint(1, 6)
        d4 = randint(1, 6)
        d_t1 = d3 + d4
        sleep(0)
        print('Jogando o primeiro dado...', end='')
        sleep(0)
        print(f'Caiu {d3}')
        sleep(0)
        print('Jogando o segunda dado...', end='')
        sleep(0)
        print(f'Caiu {d4}')
        sleep(0)
        print(f'Você conseguiu um número {d_t1}')
        print('_' * 30)
        if d_t1 == 20:
            list_ponto.append(d_t1)
            break
        else:
            sleep(2)
            print('O número não foi \033[1;31m7\033[m, então vamos continuar...')
            print('_' * 30)
            if d_t1 == 4 or d_t1 == 5 or d_t1 == 6 or d_t1 == 8 or d_t1 == 9 or d_t1 == 10:
                if d_t1 not in list_ponto:
                    list_ponto.append(d_t1)
                    list_ponto.sort()
                    print(f'Você tirou esses números já: \033[1;34m{list_ponto}\033[m')
                    print('_' * 30)
        if [4, 5, 6, 8, 9, 10] in list_ponto[0]:
            break
if len(list_ponto) > 0:
    if (4, 5, 6, 8, 9, 10) in list_ponto:
        print('Você conseguiu todos os números antes de cair um 7, você mandou bem demais!! Parabéns você \033[1;32mVENCEU!!')
    else:
        print('''Falei que você não poderia tirar um 7 antes de completar os outros número...'
Lamento mas você \033[1;31mPERDEU!!''')