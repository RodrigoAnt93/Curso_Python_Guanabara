from random import randint
sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = 0
print(f'Os números sorteados foram : {sorteio}')
for c in range(0, len(sorteio)):
    if c == 0:
        maior = sorteio[c]
        menor = sorteio[c]
    if maior < sorteio[c]:
        maior = sorteio[c]
    elif sorteio[c] < menor:
        menor = sorteio[c]
print(f'O maior número sorteado foi o {maior}')
print(f'O menor número sorteado foi o {menor}')