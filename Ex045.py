from random import randint
lista = ('PEDRA', 'PAPEL', 'TESOURA')
print('{:=^40}'.format(' VAMOS JOGAR JOKEMPÔ! '))
print('')
print('''ESCOLHA SUA JOGADA:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
esc = int(input('DIGITE SUA OPÇÃO: '))
cpu = randint(0, 2)
print('-=-' * 20)
print('A CPU ESCOLHEU {}'.format(lista[cpu]))
print('VOCÊ ESCOLHEU {}'.format(lista[esc]))
if cpu == 0:
    if esc == 0:
        print('\033[1;33mVOCÊS EMPATARAM. JOGEM NOVAMENTE!\033[m')
    elif esc == 1:
        print('\033[1;32mVOCÊ VENCEU. PARABÉNS!\033[m')

    elif esc == 2:
        print('\033[1;31mA CPU VENCEU!\033[m')
    else:
        print('\033[7;30mVOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA!\003[m')

elif cpu == 1:
    if esc == 0:
        print('\033[1;31mA CPU VENCEU!\033[m')
    elif esc == 1:
        print('\033[1;33mVOCÊS EMPATARAM. JOGEM NOVAMENTE!\033[m')
    elif esc == 2:
        print('\033[1;32mVOCÊ VENCEU. PARABÉNS!\033[m')
    else:
        print('\033[7;30mVOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA!\003[m')

elif cpu == 2:
    if esc == 0:
        print('\033[1;32mVOCÊ VENCEU. PARABÉNS!\033[m')
    elif esc == 1:
        print('\033[1;31mA CPU VENCEU!\033[m')
    elif esc == 2:
        print('\033[1;33mVOCÊS EMPATARAM. JOGEM NOVAMENTE!\033[m')
    else:
        print('\033[7;30mVOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA!\003[m')