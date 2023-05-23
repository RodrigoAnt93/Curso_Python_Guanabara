lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    if opc == 'N':
        break
for pos in lista:
    if pos % 2 == 0:
        pares.append(pos)
    else:
        impares.append(pos)
print('**' * 20)
lista.sort()
print(f'Todos os numeros digitados foram {lista}')
print(f'Os números impares digitados foram {impares}')
print(f'Os numeros pares digitados foram {pares}')