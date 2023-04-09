d = float(input('Quantos dias você ficou com o carro? '))
k = float(input('Quantos KM você rodou com o carro? '))
vd = d * 60
vk = k * 0.15
t = vk + vd
print('O total a pagar sobre o aluguel é R${:.2f}.'.format(t))




