
aproveitamento = dict()
soma = 0
partidas = []
time = []
while True:
    aproveitamento['jogador'] = str(input('Nome do Jogador: '))
    aproveitamento['partidas'] = int(input(f'Quantas partidas {aproveitamento['jogador']} jogou?'))
    if aproveitamento['partidas'] == 0:
        partida = 0
        partidas.append(partida)
    for i in range(0, aproveitamento['partidas']):
        partida = int(input(f'Quantos gols {aproveitamento['jogador']} marcou  na partida {i + 1}?'))
        soma += partida
        partidas.append(partida)
    aproveitamento['gols'] = partidas.copy()
    aproveitamento['total'] = soma
    time.append(aproveitamento.copy())
    aproveitamento.clear()
    partidas.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S/N.')
    if resp in 'N':
        break
print(f'{"COD":<4}{"NOME":<4}{'':<11}{"GOLS"}{'':>11}{"TOTAL":<4}')
print('-' * 30)
for i, v in enumerate(time):
    print(f'{i:<4}{v['jogador']:>4}{'':>7}{v['gols']}{'':>11}{v['total']:<4}')
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {dados}')
    for k, n in enumerate(time):
        if k == dados:
            for i, v in enumerate(time[k]["gols"]):
                print(f'LEVANTAMENTO DO JOGADOR {time[k]["jogador"].upper()}')
                if time[k]["partidas"] == 0:
                    print(f'          =>  {time[k]["jogador"]} nao  jogou nenhuma partida.')
                else:
                    print(f'          => Na partida {i + 1}, {time[k]["jogador"]} fez {v} gols.')

print('<<< VOLTE SEMPRE >>>')
