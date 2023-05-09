print('==' * 20)
print('{: ^40}'.format(' 10 PRIMEIRAS P.A '))
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c, end='→ ')

print('ACABOU')