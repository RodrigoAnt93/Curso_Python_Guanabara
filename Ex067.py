while True:
    print('==' * 30)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('==' * 30)
    if tab < 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        print(f'{tab} x {cont} = {tab * cont}')
print('Programa de tabuada encerrado. Até mais.')
