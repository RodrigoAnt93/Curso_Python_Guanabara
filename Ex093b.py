jogador = {}
gol = []
totgol = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantos jogos o {jogador["nome"]} ele jogou? '))
for c in range(1, partidas +1):
    g = (int(input(f'   Quantos gols no {c}° jogo? ')))
    totgol += g
    gol.append(g)
jogador['gols'] = gol.copy()
jogador['total_gol'] = totgol
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
