conturm = int(input('Quantas turmas tem na escola? '))
contaluno = 0
for c in range(1, conturm + 1, 1):
    aluno = int(input(f'Quantos alunos tem na {c}° turma? '))
    while aluno > 40:
        print('Opção inválida.')
        aluno = int(input(f'Quantos alunos tem na {c}° turma? '))
    contaluno += aluno
print(f'Existem {contaluno} nessa escola. A média de aluno por turma é {contaluno / conturm}')