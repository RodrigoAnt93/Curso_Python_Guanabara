lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_ter = maior_seg = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
            pares += lista[l][c]
print(f'A soma dos valores pares é {pares} ')
for c in range(0, 3):
    soma_ter += lista[c][2]
print(f'A soma dos valores da terceira coluna é {soma_ter}')
print(f'O maior valor da segunda linha é {max(lista[1])}')