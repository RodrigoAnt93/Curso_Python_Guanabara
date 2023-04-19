from datetime import date
age = int(input('Qual ano você quer saber se é bissexto? '))
bi = (age % 100) + (age % 400)
if age == 0:
    age = date.today().year

if bi == 0:
    print('O ano de {} é bissexto'.format(age))
else:
    print('O ano de {} não é bissexto'.format(age))
