soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1

print('De 1 à 500 tem {} múltiplos de 3 e a soma de todos é {}.'.format(cont, soma))
