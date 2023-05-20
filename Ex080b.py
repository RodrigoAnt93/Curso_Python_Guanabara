lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('O valor foi adicionado na posição 0')
    elif n <= min(lista):
        lista.insert(min(lista), n)
        print(f'O valor foi adicionado na posição {lista.index(n)}')
    elif n >= max(lista):
        lista.insert(max(lista), n)
        print(f'O valor foi adicionado na posição {lista.index(n)}')
    else:
        if n <= lista[1]:
            lista.insert(1, n)
            print(f'O valor foi adicionado na posição {lista.index(n)}')
        elif n <= lista[2]:
            lista.insert(2, n)
            print(f'O valor foi adicionado na posição {lista.index(n)}')
        elif n <= lista[3]:
            lista.insert(3, n)
            print(f'O valor foi adicionado na posição {lista.index(n)}')
print('--' * 20)
print(f'Os valores digitados foram {lista}')
