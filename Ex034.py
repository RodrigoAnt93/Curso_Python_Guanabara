sal = float(input('Qual o seu salário atual? R$'))
#verificar salário menor que 1.250,00

if sal <= 1250:
    saln = sal * 15 / 100
    print('O salário de R${:.2f} passa a ser R${:.2f}'.format(sal, (saln + sal)))
#verificar salário maior que 1.250,00
else:
    saln = sal * 10 / 100
    print('O salário de R${:.2f} passa a ser R${:.2f}'.format(sal, (sal + saln)))


