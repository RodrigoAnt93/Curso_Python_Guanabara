tab = int(input('Digite um número entre 1 e 10 para fazermos sua tabuada: '))
print('-_' * 20)
for c in range (1, 11, 1):
    print(f'{tab} X {c} = {c * tab}')