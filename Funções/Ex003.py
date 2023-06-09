def soma_tudo(a, b, c):
    s = a + b + c
    return s


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
print('_' * 40)
print(f'O valor soma total dos valores é {soma_tudo(n1, n2, n3)}')