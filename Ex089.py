alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1°: ')))
    aluno.append(float(input('Nota 2°: ')))
    alunos.append(aluno[:])
    aluno.clear()
    opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    if opc == 'N':
        break
print('↑↓→←' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 15)
for rep in range(0, len(alunos)):
    print(f'{rep+1:<4}{alunos[rep][0].capitalize():<10}{(alunos[rep][1]+alunos[rep][2])/2:>8.1f}')