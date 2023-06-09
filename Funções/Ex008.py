def con_num(n):
    n = str(n)
    return len(n)


num = int(input('Digite um número: '))
print('-' * 35)
print(f'O número {num} tem {con_num(num)} caracteres.')