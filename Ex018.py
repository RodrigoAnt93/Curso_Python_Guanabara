from math import radians, sin, cos, tan
an = int(input('Digite o ângulo: '))
ra = radians(an)
s = sin(ra)
c = cos(ra)
t = tan(ra)

print('O seno é:{:.2f}\nO cosseno é:{:.2f}\nA tangente é:{:.2f}'.format(s, c, t))
