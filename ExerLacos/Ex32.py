soma = maior = menor = 0
for c in range(1, 7 + 1):
    temp = float(input(f'Temperatura {c}° dia: '))
    soma += temp
    if c == 1:
        maior = temp
        menor = temp
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
print(f'A maior temperatura registrada foi {maior:.1f}°')
print(f'A menor temperatura registrada foi {menor:.1f}°')
print(f'A média da temperatura registrada é {soma / 7:.1f}°')
