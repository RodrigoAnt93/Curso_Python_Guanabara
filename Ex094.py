banco_dados = []
cadastro = {}
idades = 0
while True:
    cadastro["nome"] = str(input('Nome: ')).strip().capitalize()
    cadastro["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cadastro["sexo"] not in 'MF':
        del cadastro['sexo']
        cadastro["sexo"] = str(input('ERRO! Por favor, digite apenas M ou F: ')).strip().upper()[0]
    cadastro["idade"] = int(input('Idade: '))
    idades += cadastro['idade']
    banco_dados.append(cadastro.copy())
    cadastro.clear()
    opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('ERRO! Deseja continuar: S/N ')).strip().upper()[0]
    if opc == 'N':
        break
print('¨¨' * 20)
print(f'Foram cadastradas {len(banco_dados)} pessoas.')
print(f'A média de idade das pessoas cadastradas é {idades / len(banco_dados):.1f}')
print(f'As mulheres cadastradas foram ', end='')
for d in range(0, len(banco_dados)):
    if banco_dados[d]['sexo'] in 'F':
        print(f'{banco_dados[d]["nome"]} ', end='')
print(f'\nNome das pessoas com idade acima da média: ')
for c in banco_dados:
    if c['idade'] >= (idades / len(banco_dados)):
        for k, v in c.items():
            print(f'   {k} = {v}; ', end='')
        print()
print('--- FIM ---')