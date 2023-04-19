num = int(input('Digite um numero inteiro: '))
print('''Escolha uma opção para fazermos a conversão:
[1] \033[1:31mBINÁRIO\033[m
[2] \033[1:32mOCTAL\033[m
[3] \033[1:33mHEXADECIMAL\033[m''')
opc = int(input('Digite uma opção: '))
if opc == 1:
    print('{} convertido para um numero \033[1:31mBINÁRIO\033[m fica: \033[1:31m{}\033[m'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para um numero \033[1:32mOCTAL\033[m fica: \033[1:32m{}\033[m'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para \033[1:33mHEXADECIMAL\033[m fica: \033[1:33m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')