jogador = {}
time = []
gol = []
while True:
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantos jogos o {jogador["nome"]} jogou? '))
    for c in range(1, partidas +1):
        gol.append(int(input(f'   Quantos gols no {c}° jogo? ')))
    jogador['gols'] = gol.copy()
    jogador['total_gol'] = sum(gol)
    time.append(jogador.copy())
    opc = str(input('Deseja continuar: S/N ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('ERRO! Deseja continuar: S/N ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for c in jogador.keys():
    print(f'{c:<20}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-=' * 30)
while True:
    perg = int(input(f'Mostrar dados de qual jogador? [999 para parar] '))
    if perg == 999:
        break
    elif perg > len(time):
        print('Não existe jogador com o código 8')
    else:
        print(f'{"  --Levantamento do jogador ":>8}{time[perg]["nome"]}:')
        for c, g in enumerate(time[perg]["gols"]):
            print(f'    No jogo {c+1} ele fez {g} gols')
    print('--' * 40)

print('--- FIM ---')
