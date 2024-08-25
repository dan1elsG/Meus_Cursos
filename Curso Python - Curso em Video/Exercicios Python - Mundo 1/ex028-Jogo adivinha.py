import random
from time import sleep

print('\033[1m', '-=' * 40, '\n{:^80}'.format('Jogo da Adivinhacao V1'), '\n', '-=' * 40)
sleep(1)
print('CPU : "Ola vamos fazer uma Brincadeira de adivinha? tem 4 niveis de adivinha e Voce so tem 1 chance:"\n'
      '[ 1 ] Facil\n'
      '[ 2 ] Medio\n'
      '[ 3 ] dificil\n'
      '[ 4 ] Nem Tente')
nivel = int(input('Sua opcao:'))
# Verifica o numero digitado e imprime os niveis escolhidos.
if nivel == 1:
    computador = random.randint(1, 3)
    print('{:=^80}'.format('Nivel FACIL'))
    print('CPU: "Pensei em um numero Tente adivinha-lo!"')
    jogador = int(input('Digite um numero de 1 a 3:'))
# Verifica se o jogador ganhou ou perdeu.
    if computador == jogador or computador != jogador:
        print('formando pc...')

        print('Jogador: {}\nCPU: {}\n'
              '"Parabens!Voce Acertou o numero que eu pensei."'.format(jogador, computador))
    else:
        print('Jogador: {}\nCPU: {}\n '
              '"Nao Acertou HAHA!"'.format(jogador, computador))
elif nivel == 2:
    computador = random.randint(1, 5)
    print('{:=^80}'.format('Nivel MEDIO'))
    print('CPU: "Pensei em um numero Tente adivinha-lo!"')
    jogador = int(input('Digite um numero de 1 a 5:'))
    if computador == jogador:
        print('Jogador: {}\nCPU: {}\n'
              '"Parabens!Voce Acertou o numero que eu pensei."'.format(jogador, computador))
    else:
        print('Jogador: {}\nCPU: {}\n '
              '"Nao Acertou HAHA!"'.format(jogador, computador))
elif nivel == 3:
    computador = random.randint(1, 8)
    print('{:=^80}'.format('Nivel DIFICIL'))
    print('CPU: "Pensei em um numero Tente adivinha-lo!"')
    jogador = int(input('Digite um numero de 1 a 8:'))
    if computador == jogador:
        print('Jogador: {}\nCPU: {}\n'
              '"Parabens!Voce Acertou o numero que eu pensei."'.format(jogador, computador))
    else:
        print('Jogador: {}\nCPU: {}\n '
              '"Nao Acertou HAHA!"'.format(jogador, computador))
elif nivel == 4:
    computador = random.randint(1, 20)
    print('{:=^80}'.format('NEM TENTE'))
    print('CPU: "Pensei em um numero Tente adivinha-lo!"')
    jogador = int(input('Digite um numero de 1 a 20:'))
    if computador == jogador:
        print('Jogador: {}\nCPU: {}\n'
              '"Parabens!Voce Acertou o numero que eu pensei."'.format(jogador, computador))
    else:
        print('Jogador: {}\nCPU: {}\n '
              '"e pra apanhar e ficar calado!"'.format(jogador, computador))
else:
    print('Escolha uma numero valido!')
