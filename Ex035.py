print('-=-' * 20)
print('Vamos analisar se da para fazer um triangulo?')
print('-=-' * 20)

m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite segunda medida: '))
m3 = float(input('Digite terceira medida: '))
# Se uma medida for igual ou maior que a soma das outras, não se faz um triangulo
if m1 >= (m2 + m3) or m2 >= (m1 + m3) or m3 >= (m1 + m2):
    print('Essas medidas NÃO fazem um triangulo!')
else:
    print('Essas medidas FAZEM um triangulo!')
