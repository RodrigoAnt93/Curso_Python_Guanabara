lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for p in range(0,3):
    valor = int(input(f'Digite um valor para [0, {p}]: '))
    lista[0][p] = valor
for s in range(0,3):
    valor = int(input(f'Digite um valor para [1, {s}]: '))
    lista[1][s] = valor
for t in range(0, 3):
    valor = int(input(f'Digite um valor para [2, {t}]: '))
    lista[2][t] = valor
print('-=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print('')