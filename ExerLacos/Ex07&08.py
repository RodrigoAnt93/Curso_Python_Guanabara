soma = maior = 0

for c in range (1, 6, 1):
    play = int(input(f'Digite {c}° valor: '))
    soma += play
    if c == 1:
        maior += play
    if play > maior:
        maior = play

print(f'O maior valor digitado foi {maior}.')
print(f'A soma de todos os valores é {soma} e sua média é {soma / 5}')
