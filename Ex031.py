km = float(input('Quantos KM vai ter sua viagem? '))

if km <=200:

    print('Como sua viagem é menos que 200KM o valor da passagem será: R${:.2f}'.format(km * 0.50))
else:
    print("Como sua viagem passa de 200KM o valor da passagem será: R${:.2f}".format(km * 0.45))

