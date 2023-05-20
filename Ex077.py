nomes = ('Santa Cruz', 'Futebol', 'Boston Celtics', 'Basquete', 'Pokemon', 'Charizard', 'Gengar', 'Pizza')
for p in nomes:
    print(f'\nA palavra {p.upper()} tem as vogáis: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra.lower()}', end=' ')