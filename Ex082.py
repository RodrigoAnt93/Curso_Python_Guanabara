lista_pares = []
lista_impares = []
lista_total = []
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    lista_total.append(num)
    opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    if opc == 'N':
        break
lista_total.sort()
print(f'Todos os valores digitados foram {lista_total}')
print(f'Os valores pares foram {lista_pares}')
print(f'Os valores impares foram {lista_impares}')
