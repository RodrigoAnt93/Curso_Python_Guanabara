lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Opção inválida. Deseja continuar? S/N ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores na ordem decrescente são {lista}')
if lista.count(5) != 0:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')