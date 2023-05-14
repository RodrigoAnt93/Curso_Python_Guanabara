print('--' * 20)
print('{: ^40}'.format('MERCADÃO DO OBESO'))
print('--' * 20)
valsoma = contmil = cont = maiorval = 0
nomeprod = ' '
while True:
    prod = str(input('\033[1;32mQual o nome do produto: \033[m')).strip()
    val = float(input('\033[1;33mQual o valor do produto: R$\033[m'))
    print('')
    valsoma += val
    cont += 1
    if val >= 1000:
        contmil += 1
    if cont == 1 or maiorval < val:
        maiorval += val
        nomeprod = prod
    opc = str(input('Deseja cadastrar mais produtos? [S/N] ')).strip().upper()[0]
    print('')
    while opc not in 'SN':
        print('\033[1;31mOpção Inválida.\033[m')
        print('')
        opc = str(input('Deseja cadastrar mais produtos? [S/N] ')).strip().upper()[0]
        print('')
    if opc == 'N':
        break
print('{:-^40}'.format(' FIM DA LISTA! '))
print(f'O total da compra foi {valsoma:.2f}')
print(f'Temos {contmil} produtos acima de R$1000')
print(f'O produto mais caro é {nomeprod} e custa {maiorval:.2f}')
