n = int(input('Digite o valor do metro: '))

dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10

print('O valor digitado fica:\nQuilometro é: {} \nHectometro é: {}\nDecámetro é: {}'.format(km, hm, dam))
print('Decimetro é: {}\nCentimetro é: {}\nMilimetro é: {}'.format(dm, cm, mm))
