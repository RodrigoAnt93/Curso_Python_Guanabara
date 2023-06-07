def list_aluno(num, show):
    dados_aluno = {}
    dados_aluno['total'] = len(num)
    dados_aluno['maior'] = max(num)
    dados_aluno['menor'] = min(num)
    dados_aluno['media'] = sum(num) / len(num)
    if show == 'S':
        if dados_aluno['media'] < 5:
            dados_aluno['situação'] = 'RUIM'
        elif 5 < dados_aluno['media'] < 7:
            dados_aluno['situação'] = 'RAZOÁVEL'
        else:
            dados_aluno['situação'] = 'BOM'
    return (dados_aluno)


luno = []
cont = 1
while True:
    luno.append(int(input(f'Digite a {cont}° nota: ')))
    cont += 1
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('_' * 25)
sit = str(input('Você quer saber sua situação? [S/N] ')).strip().upper()[0]
while sit not in 'SN':
    sit = str(input('Você quer saber sua situação? [S/N] ')).strip().upper()[0]

print(list_aluno(luno, sit))
