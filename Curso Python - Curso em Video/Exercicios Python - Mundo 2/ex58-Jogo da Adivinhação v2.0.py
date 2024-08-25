import random
from time import sleep

print('\033[1m', '-=' * 40, '\n{:^80}'.format('Jogo da Adivinhacao V2'), '\n', '-=' * 40)
print('ABRINDO...')
sleep(1)
print('-=' * 40)
computador = random.randrange(0, 10)
print('Ola Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10.\nTente adivinhar...')
sleep(0.6)
jogador = int(input('Qual seu palpite:'))
palpite = 0
while jogador > 10:
    print("numero invalido... Tente novamente com um numero entre 0 e 10.")
    jogador = int(input('Qual seu palpite:'))
while jogador != computador:
    palpite += 1
    if jogador <= computador:
        print('Mais... Tente mais uma vez...')
    else:
        print('Menos... Tente mais uma vez...')
    jogador = int(input('Qual seu palpite:'))
if palpite == 0:
    print('Você Acertou.')
else:
    print('Voce acertou. Mais precisou de  {} tentativas.'.format(palpite))
