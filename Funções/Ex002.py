def repet(n):
    c = 1
    while c <= n:
        for i in range(c):
            i += 1
            print(f'{i} ', end='')
        print('')
        c += 1
num = int(input('Digite um valor para repetir: '))
repet(num)