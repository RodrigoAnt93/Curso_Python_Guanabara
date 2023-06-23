valor1 = valor2 = 1
print('a sequência fica assim: 0 -> 1 -> 1',end=' -> ')
soma = 0
while soma <= 500:
    valor3 = valor1 + valor2
    print(valor3, end=' -> ')
    soma = valor3
    valor1 = valor2
    valor2 = valor3
print('FIM')