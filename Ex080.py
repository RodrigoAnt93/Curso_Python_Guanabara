lista = []
cont = 0
for c in range(0, 5):
    listan = int(input('Digite um valor: '))
    if c == 0:
        lista.append(listan)
        print(f'O valor foi adicionado no 0...')
    else:
        lista.append(listan)
        lista.sort()
        if listan >= max(lista):
            print('O valor foi adicionado no final')
        else:
            print(f'O valor foi adicionado na {lista.index(listan)} posição')
print('**' * 20)
print(f'Os valores informados foram {lista}')