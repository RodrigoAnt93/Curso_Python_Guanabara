cont_prod = valprod = 1
total = 0
while True:
    while valprod != 0:
        valprod = float(input(f'Produto {cont_prod}: R$'))
        total += valprod
        cont_prod += 1
    if valprod == 0:
        print('--' * 20)
        print(f'Total: R${total:.2f} ')
        pago = int(input('Dinheiro: R$'))
        print(f'Troco: R${pago - total:.2f}')
        print('~~' * 20)
        print('FIM!')
        print('~~' * 20)
        print('')
        cont_prod = valprod = 1
        total = 0
