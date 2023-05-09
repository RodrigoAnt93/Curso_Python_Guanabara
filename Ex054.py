from datetime import date
ano = date.today().year
contador = 0
contador2 = 0
for c in range(1, 8):
    anonas = int(input('Qual ano você a {}° pessoa nasceu? '.format(c)))
    if (ano - anonas) > 18:
        contador += 1
    else:
        contador2 += 1
print('''\033[1;32m{}\033[m pessoas são maior(es) de idade.
\033[1;31m{}\033[m pessoas são menor(es) de idade.'''.format(contador, contador2))
