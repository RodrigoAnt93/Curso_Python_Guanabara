def fatorial(num, show=False):
    f = 1
    if show:
        for c in range(num, 0, -1):
            print(f'{c} ', end='')
            if c > 1:
                print('X ', end='')
            else:
                print('= ', end='')
            f *= c
        return f'{f}!'
    else:
        for c in range(num, 0, -1):
            f *= c
        return f'{f}!'

fac = int(input('Fatorial: '))
opc = str(input('Detalhado? [S/N] ')).strip().upper()[0]
while opc not in 'SN':
    opc = str(input('Detalhado? [S/N] ')).strip().upper()[0]
if opc == 'S':
    opc = True
else:
    opc = False
print('-' * 40)
print(fatorial(fac, opc))