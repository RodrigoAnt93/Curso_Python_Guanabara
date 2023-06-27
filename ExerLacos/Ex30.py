valpao = float(input('Qual o valor do pão? '))
quanpao = int(input('Seram quantos pães? '))
for c in range(1, quanpao + 1 ):
    print(f'{c} - R$ {valpao * c:.2f}')