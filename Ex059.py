from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('')
print('''Opções de operação:
[1] SOMA
[2] MULTIPLICAR
[3] MAIOR NUMERO
[4] ESCOLHER OUTROS NUMEROS
[5] SAIR''')
c = 1
while c < 2:
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1 + n2))
        print('-=' * 20)
        sleep(1)
    elif opcao == 2:
        print('A multiplicação de {} x {} = {}'.format(n1, n2, n1 * n2))
        print('-=' * 20)
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        elif n1 < n2:
            print('O maior numero é o {}'.format(n2))
        print('-=' * 20)
        sleep(1)
    elif opcao == 4:
        n11 = int(input('Digite o primeiro numero: '))
        n22 = int(input('Digite o segundo numero: '))
        n1 = n11
        n2 = n22
    elif opcao == 5:
        c += 1
        print('Você saiu do programa. Até mais!')
    else:
        print('Essa opção é inválida. Escolha uma opção válida.')
        print('-=' * 20)
        sleep(1)



