
while True:
    valor = str(input(f'digite: ')).strip()
    valorR = valor.replace(',', '').replace('.', '')
    if valorR.isnumeric():
        valor = valor.replace(',', '.')
        valor = float(valor)
        break
    else:
        print(f'\033[1;31mERRO: "{valor}" não é um preço inválido\033[m')
