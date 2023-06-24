print('-=' * 20)
print('{: ^40}'.format(' SISTÉMA URNA ELETRÔNICA '))
print('-=' * 20)
eleitor = int(input('Numero de eleitores votantes na urna: '))
print('''Opções de candidato:
Lula - [13]
Ciro - [12] 
Tablet - [45]
Branco/Nulo - [00]''')
lula = ciro = tablet = bn = 0
print('')
for c in range(1, eleitor + 1, 1):
    voto = int(input(f'Voto do {c}° eleitor: '))
    if voto == 13:
        lula += 1
    elif voto == 12:
        ciro += 1
    elif voto == 45:
        tablet += 1
    else:
        bn += 1
print('~~' * 30)
print(f'Lula recebeu {lula} votos')
print(f'Ciro recebeu {ciro} votos')
print(f'Tablet recebeu {tablet} votos')
print(f'Brancos e Nulos somaram {bn} votos')
