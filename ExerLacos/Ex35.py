mais_alto = mais_baixo = mais_gordo = mais_magro = cont = 0
cod_alto = cod_baixo = cod_gordo = cod_magro = 0
print('-=' * 20)
print('{: ^40}'.format(' CADASTRO ACADEMIA '))
print('-=' * 20)
while True:
    cod = int(input('Digite seu código: '))
    alt = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    cont += 1
    if cont == 1:
        mais_alto = alt
        cod_alto = cod
        mais_baixo = alt
        cod_baixo = cod
        mais_gordo = peso
        cod_gordo = cod
        mais_magro = peso
        cod_magro = cod
    if alt > mais_alto:
        mais_alto = alt
        cod_alto = cod
    elif alt < mais_baixo:
        mais_baixo = alt
        cod_baixo = cod
    if peso > mais_gordo:
        mais_gordo = peso
        cod_gordo = cod
    elif peso < mais_magro:
        mais_magro = peso
        cod_magro = cod
    print('')
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        print('--' * 20)
        break
    print('--' * 20)

print(f'O aluno codigo {cod_alto} é o aluno mais alto com uma altura de {mais_alto:.2f}')
print(f'O aluno código {cod_baixo} é o aluno mais baixo com uma altura de {mais_baixo:.2f}')
print(f'O aluno código {cod_gordo} é o aluno mais pasado com um peso de {mais_gordo:.1f}Kg')
print(f'O aluno código {cod_magro} é o aluno menos pesado com um peso de {mais_magro:.1f}Kg')
print('Fim!')

