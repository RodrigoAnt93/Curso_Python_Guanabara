print('=-' * 20)
print('{: ^40}'.format(' 10 TERMOS DE UMA PA '))
print('=-' * 20)
base = int(input('Base: '))
razao = int(input('Razão: '))
dec = base + (10 - 1) * razao
for c in range(base, dec + 1, razao):
    print(f'{c}', end=' -> ')
print('ACABOU!')