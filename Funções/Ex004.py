def PorN(n):
    if n <= 0:
        return '\033[1;31mNEGATIVO'
    else:
        return '\033[1;32mPOSITIVO'


num = int(input('Digite o valor para saber se é positivo ou negativo: '))
print('__' * 30)
print(f'O valor {num} é {PorN(num)}')