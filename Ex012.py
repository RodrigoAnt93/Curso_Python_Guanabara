valor = float(input('Qual o valor pago na compra? R$'))
des = valor*5/100
tol = valor - des
print('Com o desconto de 5% no valor da compra, você ganhou um abatimento de R${}. O valor total a pagar é R${:.2f}.'
.format(des, tol))
