maior = menor = soma = 0
for c in range(1, 11, 1):
    num = int(input(f'Digite o {c}° número: '))
    soma += num
    if c == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('-_' * 20)
print(f'O maior número digitado foi {maior}.')
print(f'O menor número digitado foi {menor}')
print(f'A soma de todos os valores digitado é {soma}')