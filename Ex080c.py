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
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor foi adicionado na posição {lista.index(n)}')
                break
            pos += 1
print('--' * 20)
print(f'Os valores digitados foram {lista}')
