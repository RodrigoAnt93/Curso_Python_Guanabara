maioridade = homem = mulher = 0
while True:
    print('--' * 30)
    print('CADASTRO DE PESSOA')
    print('--' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: M/F  ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida. Sexo: M/F ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
            mulher += 1
    opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Opção inválida. Deseja continuar? S/N  ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Foram cadastradas {maioridade} com 18 anos ou mais.')
print(f'Temos pelo menos {homem} homens cadastrado')
print(f'Temos pelo menos {mulher} cadastrada com menos de 20 anos.')
