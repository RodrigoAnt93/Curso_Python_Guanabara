def ValorPagamento(v, a, f=False):
    global cont_pres
    global total_pago
    valor_atraso = 0
    cal_atraso = v * 3 / 100 + v
    for m in range(a):
        valor_atraso += cal_atraso * 0.1 / 100
    if f == False:
        if a == 0:
            cont_pres += 1
            total_pago += v
            print(f'Como não teve atraso no pagamento, o valor a pagar é RS{v}')
        else:
            cont_pres += 1
            total_pago += (cal_atraso + valor_atraso)
            print(f'O valor calculado com atraso fica R${cal_atraso + valor_atraso:.2f}')
    else:
        print('{:-^40}'.format(' FECHAMENTO '))
        print(f'A quantidade de prestações pagas foi de {cont_pres} e o total pago foi R${total_pago:.2f}')


cont_pres = total_pago = 0
while True:
    valor = float(input('Digite o valor da prestação[999 para encerrar]: R$'))
    if valor == 999:
        ValorPagamento(0, 0, True)
    atrasa = int(input('Dias de atraso: '))
    ValorPagamento(valor, atrasa, False)
    print('--' * 30)