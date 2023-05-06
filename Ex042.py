m1 = float(input('Qual a primeira medida? '))
m2 = float(input('Qual a segunda medida? '))
m3 = float(input('Qual a terceira medida? '))

if m1 >= (m2+m3) or m2 >= (m1 + m3) or m3 >= (m1 + m2):
    print('\033[1:31mEssas medidas não formam um TRIANGULO.')
elif m1 == m2 and m1 == m3:
    print('Essas medidas fazem um TRIÂNGULO EQUILÁTERO.')
elif m1 == m2 or m2 == m3 or m3 == m1:
    print('Essas medidas fazem um TRIÂNGULO ISÓSCELAS.')
else:
    print('Essas medidas fazem um TRIANGULO ESCALENO.')