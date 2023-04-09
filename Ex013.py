sal = float(input('Qual o salário do funcionário? R$'))
nsal = sal + (sal*15/100)
print('O salário atual do funcionário é R${}. Com o aumento de 15% o valor passa a ser R${:.2f}'.format(sal, nsal))
