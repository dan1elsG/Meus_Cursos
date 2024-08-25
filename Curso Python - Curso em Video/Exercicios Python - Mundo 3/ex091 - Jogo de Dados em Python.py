from random import randint
from time import sleep
jogadores = {"JOGADOR 1": randint(1, 6), "JOGADOR 2": randint(1, 6), "JOGADOR 3": randint(1, 6),
             "JOGADOR 4": randint(1, 6)}
print('-=' * 10, 'Jogo de dados em Python', '-=' * 10)
print('VALORES SORTEADOS:')
for k, v in jogadores.items():
    print(f"{k} tirou {v}.")
    sleep(1)
print('==', 'RANKING DOS JOGADORES', '==')
c = 0
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    c += 1
    print(f"  {c} LUGAR: {i}: {jogadores[i]}.")
    sleep(1)
