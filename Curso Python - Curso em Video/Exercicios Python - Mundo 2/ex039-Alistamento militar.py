import datetime
from time import sleep  # importa a fucao sleep da biblioteca time

print('\033[34m>>===>-' * 13, '\n{:^80}'.format('Exercicio 039'), '\n', '>>===>-' * 13)  # firula para deixar o programa
# mais bonito
print('\033[36mPROCESSADO.....\033[31m\n', '>>===>❤' * 13)
sleep(2)  # Faz o programa "Dormir" por alguns segundos.
print('\033[mFaça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,\nse ele'
      ' ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou\ndo tempo do'
      ' alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do\n'
      'prazo.\033[31m\n', '>>===>❤' * 13)
# Enunciado da questao.
sleep(1)

nome = input('\033[mQual seu Nome: ').title().strip()  # Pedi pro usuario digitar um nome e automaticamente formata o nome.
ano = int(input('Em que ano voce nasceu: '))  # Pedi pro usuario digitar o ano de nascimento
ano_atual = datetime.datetime.now().year  # Puxa o ano atual da maquina.
idade = ano_atual - ano  # calcula a idade do usuario
alistamento = idade - 18

tempo_alistamento = ano_atual - alistamento
alistado = input('Voce ja fez seu alistamento: S para sim e N para nao').upper().strip()

if idade > 18 and alistado in 'S SIM':
    print('Gostei de saber {} fez seu alistamento, voce dever ter se alistado em {}'.format(nome, tempo_alistamento))
elif idade > 18 and alistado in 'NAO N':
    print('{} deveria ter se alistado ha {} anos.'.format(nome, alistamento))
elif idade == 18 and alistado in 'S SIM':
    print('Parabens {} Fez seu alistamento no tempo Certo!'.format(nome))
elif idade == 18 and alistado in 'N NAO':
    print('{} ja esta na hora de fazer seu alistamento!'.format(nome))
elif idade < 18 and alistado in 'S SIM':
    print('{} esta mentindo, so podera ser alistar em {}!'.format(nome, tempo_alistamento))
elif idade < 18 and alistado in 'N NAO':
    print('Ola {}!, Podera se alistar em {}!'.format(nome, tempo_alistamento))
