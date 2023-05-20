valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}° valor: ')))
print(f'O valores digitados foram: {valores}')
print(f'O maior valor foi {max(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print(f'\nO menor valor foi {min(valores)} e ele está na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')