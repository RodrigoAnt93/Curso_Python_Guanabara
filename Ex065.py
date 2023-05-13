c1 = c2 = c3 = 0
while c1 != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    c1 = n
    if n == 999:
        print('Você digitou {} numeros e a soma deles é {}.'.format(c2, c3))
    else:
        c2 += 1
        c3 += n