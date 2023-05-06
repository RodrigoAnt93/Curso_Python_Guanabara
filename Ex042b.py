m1 = float(input('Qual a primeira medida? '))
m2 = float(input('Qual a segunda medida? '))
m3 = float(input('Qual a terceira medida? '))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Essas medidas formam um TRIANGULO.')
    if m1 == m2 == m3:
        print('EQUIlÁTERO.')
    elif m1 != m2 != m3 != m1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES')
else:
    print('Essas medidas não formam um triângulo.')