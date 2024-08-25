

def verificar_dados(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} tem {gols} gols.')


nome_jogador = str(input('Nome do Jogador: '))
gols_jogador = str(input(f'Gols no campeonato: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador.strip() == '':
    verificar_dados(gols=gols_jogador)
else:
    verificar_dados(nome_jogador, gols_jogador)
