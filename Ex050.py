s = 0
for c in range(1, 7):
    n = int(input('Digite o {}° numero: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('Dos valores digitados só os numeros pares foram considerados. A soma desses numeros são \033[1m{}\033[m'.format(s))

