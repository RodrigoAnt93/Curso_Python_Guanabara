from random import randint

while True:
    opc = int(input('Quantos números você quer sortear? '))
    num = []
    for c in range(0, opc):
        num.append(randint(1, 9))
    print(f'Os valores sorteados foram {num} e foi informado {len(num)} valores.')
    print(f'O maior valor sorteado foi {max(num)}')
    print('_' * 50)

