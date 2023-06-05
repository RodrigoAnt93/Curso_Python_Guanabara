def dados(jog, g):
    if jog == '':
        jog = '<deconhecido>'
    if not g.isdigit():
        g = '0'
    print(f'  O jogador {jog} fez {g} gols no campeonato.')


jogador = str(input('Nome Jogador: ')).strip().title()
gols = str(input('Gols: '))
dados(jogador, gols)
