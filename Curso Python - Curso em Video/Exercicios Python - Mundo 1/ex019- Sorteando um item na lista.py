# importa a biblioteca randon.
import random
print('\033[34m+', '-=' * 45, '+')
print('|\033[m{:^90}'.format('Sorteando um Nome na Lista'), "\033[34m |")
print('+', '-=' * 45, '+')
print('|   \033[mO professor de matemática, Sr. Silva, estava prestes a começar uma nova aula empolgante\033[34m  |')
print('|   \033[mAntes de iniciar, ele decidiu fazer algo divertido. Queria sortear um dos seus quatro\033[34m    |')
print('|   \033[mAlunos para apagar o quadro. Com um sorriso no rosto, ele percebeu que não sabia muito\033[34m   |')
print('|   \033[mBem como digitar os nomes na sua nova lista eletrônica. Ajude o  Professor\033[34m               |')
print('|   \033[ma digitar os nomes dos alunos: \033[34m                                                          |')
print('+', '-=' * 45, '+')

# pedi para o usuario digitar os nomes dos alunos
nome1 = input(str('\033[mQual o nome do Primeiro aluno: ')).title()
nome2 = input(str('Qual o nome do Segundo aluno : ')).title()
nome3 = input(str('Qual o nome do Terceiro aluno:')).title()
nome4 = input(str('Qual o  nome do Quarto aluno : ')).title()
print('\033[34m+', '------' * 15, '+')

# Lista e Sorteia Qual aluno ira apagar o quadro.
alunos = [nome1, nome2, nome3, nome4]
sorteado = random.choice(alunos)
print('\033[m   Aluno sortedo: {}'.format(sorteado))
print('\033[34m+', '------' * 15, '+')
