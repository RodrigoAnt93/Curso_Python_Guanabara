def capit(txt):
    print('-' * (len(texto)+ 4))
    print(f'  {txt}')
    print('-' * (len(texto) + 4))


while True:
    texto = str(input('Digite o cabeçalho: ')).strip().title()
    print('')
    capit(texto)
    print('*' * 30)
