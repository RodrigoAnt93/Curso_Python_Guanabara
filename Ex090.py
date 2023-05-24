aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('=-' * 15)
if aluno["media"] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno['situação'] = 'Recuperação'
elif 0 <= aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')