somaidade = 0
mediaidade = 0
nomevelho = 0
maidade = 0
mulheres = 0
idademulher = 0
for c in range(1, 7):
    print('---- {}° PESSOA ----'.format(c))
    nome = str(input('Qual o nome? ')).strip().upper()
    idade = int(input('Qual idade? '))
    se = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and se in 'Mm':
        maidade = idade
        nomevelho = nome
    if se in 'Mm' and idade > maidade:
        maidade = idade
        nomevelho = nome
    if se in 'Ff' and idade < 20:
        idademulher += 1
mediaidade = somaidade / 6
print('')
print('A idade médida das pessoas cadastradas são {:.0f} anos.'.format(mediaidade))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomevelho.capitalize(), maidade))
print('Foram {} mulheres cadastradas com menos de 20 anos.'.format(idademulher))
