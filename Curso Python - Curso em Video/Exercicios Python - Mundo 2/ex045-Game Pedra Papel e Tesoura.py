from random import choice
from time import sleep

print('\033[1;36m-=' * 40, '\n{:^80}'.format('PEDRA PAPEL TESOURA'), '\n', '-=' * 40)
computador = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = choice(computador)
print('\033[1m[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA\n'
      'CASO O JOGADOR DIGITE UM NUMERO DIFERENTE DAS OPCOES SUA JOGADA SERA ALEATORIA.\n', '-=' * 40)
jogador = int(input('\033[1mQUAL SUA JOGADA: '))
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
elif jogador == 3:
    jogador = 'TESOURA'
else:
    jogador = choice(computador)
print('\033[1;36m-=' * 40)
print('\033[1;34mJO')
sleep(1)
print('\033[1;34mKEN')
sleep(1)
print('\033[1;34mPOO!!!')

# Verifica se o CPU ganhou!
if (cpu == 'PEDRA' and jogador == 'TESOURA' or cpu == 'PAPEL' and jogador == 'PEDRA' or cpu == 'TESOURA'
        and jogador == 'PAPEL'):

    print('\033[1;34m-=' * 40)
    print('Jogador: {}\nCPU: {}'.format(jogador, cpu))
    print('\033[1;34m-=' * 40)
    print('\033[1;31mCPU GANHOU!')

# Verifica se o JOGADOR ganhou!
elif (jogador == 'PEDRA' and cpu == 'TESOURA' or jogador == 'PAPEL' and cpu == 'PEDRA' or jogador == 'TESOURA'
      and cpu == 'PAPEL'):

    print('\033[1;34m-=' * 40)
    print('Jogador: {}\nCPU: {}'.format(jogador, cpu))
    print('\033[1;34m-=' * 40)
    print('\033[1;32mJOGADOR GANHOU!!')

# Verifica se a partida deu empate!
elif (jogador == 'PEDRA' and cpu == 'PEDRA' or jogador == 'PAPEL' and cpu == 'PAPEL' or jogador == 'TESOURA'
      and cpu == 'TESOURA'):

    print('\033[1;34m-=' * 40)
    print('Jogador: {}\nCPU: {}'.format(jogador, cpu))
    print('\033[1;34m-=' * 40)
    print('\033[1;35mEMPATE!!')
