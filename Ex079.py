valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não irei adicionar...')
        opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
        while opc not in 'SN':
            opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
        if opc == 'N':
            break
    elif valor not in valores:
        valores.append(valor)
        print('Valor armazenado com sucesso...')
        opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
        while opc not in 'SN':
            opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
        if opc == 'N':
            break
print('*-' * 20)
print(f'Os valores adicionados foram {sorted(valores)}')