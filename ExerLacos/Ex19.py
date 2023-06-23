maior = menor = soma = 0
for c in range(1, 11, 1):
    num = int(input(f'Digite o {c}° número entre 1 e 1000: '))
    if num < 0 or num > 1000:
        print('Opção Inválida.')
        num = int(input(f'Digite o {c}° número entre 1 e 1000: '))
    elif num > 0 and num <= 1000:
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