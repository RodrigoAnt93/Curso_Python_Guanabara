valor = float(input('Digite o valor do carro: R$'))
acesso = 0
totalacesso = 0
print('Precisamos saber se seu carro tem acessórios e quais são. Responda com [1] se \033[1;32mSIM\033[m e [2] se \033[1;31mNÃO\033[m')
print('')
arcon = int(input('Seu carro tem ar-condicionado? '))
if arcon == 1:
    acesso = acesso + 3000
    totalacesso = totalacesso + 1
print('')
dh = int(input('Seu carro tem Direção Hidráulica? '))
if dh == 1:
    acesso = acesso + 1500
    totalacesso = totalacesso + 1
print('')
alarme = int(input('Seu carro tem alarme? '))
if alarme == 1:
    acesso = acesso + 500
    totalacesso = totalacesso + 1
print('')
altfal = int(input('Seu carro tem alto-falante? '))
if altfal == 1:
    acesso = acesso + 1000
    totalacesso = totalacesso + 1
print('-=' * 30)
print('O valor inicial do carro foi: R$\033[1;33m{:.2f}\033[m'.format(valor))
print('Foram incluído \033[1;33m{}\033[m acessórios no carro.'.format(totalacesso))
print('O total dos acessórios acrescentado foi \033[1;33mR${:.2f}\033[m'.format(acesso))
print('O total final foi: \033[1;33mR${:.2f}\033[m'.format(valor + acesso))

