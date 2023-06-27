tab = int(input('Mostrar a tabuada de: '))
inicio = int(input('Começando por: '))
fim = int(input('Terminando em: '))
while fim <= inicio:
    fim = int(input('Opção inváida. Terminando em: '))
print('--' * 20)
print(f'A tabuada de {tab} começando por {inicio} e terminado em {fim} fica:')
for c in range(inicio, fim + 1):
    print(f'{tab} X {c} = {tab * c}')
