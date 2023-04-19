from time import sleep
print('\033[32m-=-' * 20)
print('\033[1;31mVamos calcular sua situação para saber se tem como sair o empréstimo!')
print('\033[32m-=-\033[m' * 20)
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
ano = float(input('Em quantos anos você deseja pagar? '))
val = casa / (ano * 12)
poc = sal * 30/100
sleep(3)
if val <= poc:
    print('O empréstimo foi \033[1;32mAPROVADO\033[m. As parcelas ficaram de R${:.2f} em {:.0f} meses.'.format(val, ano * 12 ))
elif val > poc:
    print('O empréstimo foi \033[1;31mNEGADO\033[m. As parcelas seriam de R${:.2f} e passariam de 30% do seu salário, o que não pode.'.format(val))