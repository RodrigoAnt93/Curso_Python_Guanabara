def leiaInt(v):
    v = input(v)
    if v.isnumeric():
        return v
    else:
        while not v.isnumeric():
            print('\033[1;31mERRO! Você só pode digitar números\033[m')
            v = leiaInt('Digite um valor: ')
        return v



# programa principal
num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')