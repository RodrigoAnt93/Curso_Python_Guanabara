val = int(input('Digite um valor de 0 a 10: '))
while val > 10:
    print('Esse valor é inválido')
    val = int(input('Digite um valor de 0 a 10: '))
print(f'O valor digitado é válido e ele foi {val}')