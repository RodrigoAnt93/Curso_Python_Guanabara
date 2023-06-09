def repet(n):
    for i in range(n):
        i += 1
        print(str(f'{i} ') * i)

n = int(input('Digite o valor a repetir: '))
repet(n)