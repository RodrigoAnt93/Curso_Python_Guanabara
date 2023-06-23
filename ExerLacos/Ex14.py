impar = par = 0
for c in range(1, 11, 1):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
