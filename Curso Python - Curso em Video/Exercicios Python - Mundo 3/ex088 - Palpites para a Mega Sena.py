from random import randint
from time import sleep
jogost = []
jogos = []
num = 0
print('-='*30)
print('{:^60}'.format('MEGA SENA'))
print('-='*30)
jogosq = int(input('Quantos jogos voce quer que eu serteie?'))
print('{:-^60}'.format(f' SORTEANDO {jogosq} JOGOS '))
for c in range(0, jogosq):
    while len(jogos) < 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
    jogost.append(jogos[:])
    jogos.clear()
for c in range(0, jogosq):
    print(f'JOGO {c+1}: {sorted(jogost[c])}')
    sleep(1)
print('{:-^60}'.format(f' < BOA SORTE! > '))

