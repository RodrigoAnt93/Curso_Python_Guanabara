val = float(input('Qual o valor do produto: R$'))
dvista = val - (val*10/100)
ddeb = val - (val*5/100)
card = val + (val*2/100)

print('O valor do produto é R${}.\nÀ vista fica por R${:.2f}.\nNo débito fica por R${:.2f}.'.format(val, dvista,ddeb))
print('No cartão de crédito fica R${:.2f}.'.format(card))

