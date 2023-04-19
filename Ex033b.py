p = int(input('Qual lucro do primeiro dia? '))
s = int(input('Qual o lucro do segundo dia: '))
t = int(input('Qual lucro do terceiro dia: '))
#verificando o valor menor
menor = p
if s<p and s<t:
    menor = s
if t<p and t<s:
    menor = t
print('O menor lucro foi R${}'.format(menor))
#verificando maior valor
maior = p
if s>p and s>t:
    maior = s
if t>p and t>s:
    maior = t
print('O maior lucro é R${}'.format(maior))