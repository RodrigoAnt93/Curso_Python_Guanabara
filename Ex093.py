jogador = {}
gol = []
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantos jogos o {jogador["nome"]} ele jogou? '))
for c in range(1, partidas +1):
    gol.append(int(input(f'   Quantos gols no {c}° jogo? ')))
jogador['gols'] = gol.copy()
jogador['total_gol'] = sum(gol)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'    => Na partida {c+1}, fez {v} gols')
print(f'Fez um total de {jogador["total_gol"]} gols')