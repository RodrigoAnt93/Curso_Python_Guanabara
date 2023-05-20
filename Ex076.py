lista = ('Caderno', 20.95,
         'Caneta', 2,
         'Mochila', 159.99,
         'Mouse', 19.99,
         'Apontador', 5.5,
         'Borracha', 1.25)
print('--' * 20)
print(f'{"Lista de Produtor":^40}')
print('--' * 20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')