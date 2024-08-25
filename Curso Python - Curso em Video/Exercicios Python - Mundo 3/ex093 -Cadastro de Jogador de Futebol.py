from time import sleep
partidas = []
aproveitamento = dict()
aproveitamento['jogador'] = str(input('Nome do Jogador: '))
aproveitamento['partidas'] = int(input(f'Quantas partidas {aproveitamento['jogador']} jogou?'))
soma = 0
for i in range(0, aproveitamento['partidas']):
    partida = int(input(f'Quantos gols {aproveitamento['jogador']} marcou  na partida {i+1}?'))
    soma += partida
    partidas.append(partida)
aproveitamento['gols'] = partidas.copy()
aproveitamento['total'] = soma
print('-=' * 30)
sleep(1)
print(f'O jogador {aproveitamento['jogador']} jogou {aproveitamento["partidas"]} jogos.')
for i, v in enumerate(aproveitamento['gols']):
    print(f'          => Na partida {i + 1}, fez {v} gols.')
    sleep(1)
print(f'Foi um total de {aproveitamento["total"]} gols.')

















