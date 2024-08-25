from random import randint
from time import sleep
jogador = cpu = " "
jogador_campeao = 0
print('-=' * 40)
print('{:^80}'.format('IMPAR OU PAR'))
print('-=' * 40)
print('ABRINDO.....')
sleep(1)
while True:
    cpu_num = randint(0, 10)
    jogador_num = int(input('Digite um numero entre 0 e 10: '))
    sleep(1)
    while jogador_num not in range(0, 11):
        jogador_num = int(input('Dgite um numero entre 0 e 10: '))
        sleep(1)
    while jogador not in 'PI':
        jogador = str(input('Voce quer impar ou par: [I para impar/P para par]')).upper().strip()
        sleep(1)
        if jogador == 'I':
            cpu = "P"
        elif jogador == 'P':
            cpu = "I"
        print('-=' * 40)
    soma = cpu_num + jogador_num
    if soma % 2 == 0:
        if jogador == "P":
            print(f'O COMPUTADOR ESCOLHEU {cpu} E O JOGADOR ESCOLHOU {jogador}')
            print(f'O COMPUTADOR JOGOU {cpu_num} E O JOGADOR {jogador_num}  RESULTADO {soma} DEU PAR!')
            print("O JOGADOR VENCEU!")
            print('-=' * 40)
            jogador_campeao += 1
            jogador = cpu = " "

        elif cpu == "P":
            print(f'O COMPUTADOR ESCOLHEU {cpu} E O JOGADOR ESCOLHOU {jogador}')
            print(f'O COMPUTADOR JOGOU {cpu_num} E O JOGADOR {jogador_num}  RESULTADO {soma} DEU PAR!')
            print("O COMPUTADOR VENCEU!")
            print('-=' * 40)
            break
    else:
        if jogador == "I":
            print(f'O COMPUTADOR ESCOLHEU {cpu} E O JOGADOR ESCOLHOU {jogador}')
            print(f'O COMPUTADOR JOGOU {cpu_num} E O JOGADOR {jogador_num}  RESULTADO {soma} DEU IMPAR!')
            print("O JOGADOR VENCEU!")
            print('-=' * 40)
            jogador_campeao += 1
            jogador = cpu = " "
        elif cpu == "I":
            print(f'O COMPUTADOR ESCOLHEU {cpu} E O JOGADOR ESCOLHOU {jogador}')
            print(f'O COMPUTADOR JOGOU {cpu_num} E O JOGADOR {jogador_num}  RESULTADO {soma} DEU IMPAR!')
            print("O COMPUTADOR VENCEU!")
            print('-=' * 40)
            break

print(f'Jogador Ganhou {jogador_campeao} vezes seguidadas')
