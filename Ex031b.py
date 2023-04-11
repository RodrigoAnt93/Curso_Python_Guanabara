med =float(input('Qual foi sua média de nota no ENEM: '))
if med >= 650:
    nota = 'APROVADO'
else:
    nota = 'REPROVADO'
print('Com essa média de nota você está {} nesse curso'.format(nota))
