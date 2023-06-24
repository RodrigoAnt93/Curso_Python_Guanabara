cont = soma = 0
while True:
    idade = int(input('Idade: '))
    cont += 1
    soma += idade
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opc not in 'SN':
        print('Opção inválida!')
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    elif opc == 'N':
        break
media = soma / cont
print('')
print('A média de idade cadastrada é {:.1f} anos'.format(media))
if media > 0 or media <= 25:
    print('A turma é JOVEM.')
elif media > 25 or media <= 60:
    print('A turma é ADULTA.')
else:
    print('A turma é IDOSA.')
