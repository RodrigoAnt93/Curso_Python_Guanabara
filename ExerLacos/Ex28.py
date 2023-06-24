cd = int(input('Você comprou quantos CDs? '))
total = 0
for c in range(1, cd + 1, 1):
    valcd = float(input(f'Quanto você pagou no {c}° CD? '))
    total += valcd
print(f'Você gastou R${total:.2f} em cds. O valor médio gasto em cada CD foi R${total / cd:.2f}')