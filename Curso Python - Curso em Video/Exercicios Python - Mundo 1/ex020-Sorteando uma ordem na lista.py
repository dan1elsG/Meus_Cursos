# importa a biblioteca randon.
import random

# Nome e Historia do programa.
print('\033[34m+', '-=' * 45, '+')
print('|\033[m{:^90}'.format('Sorteando uma Ordem na Lista'), "\033[34m |")
print('+', '-=' * 45, '+')
print('|   \033[mO professor de matemática, Sr. Silva, estava prestes a começar uma nova aula empolgante\033[34m  |')
print('|   \033[mAntes de iniciar, ele decidiu fazer algo divertido. Queria sortear a ordem de        \033[34m    |')
print('|   \033[mApresentacao dos trabalhos. Com um sorriso no rosto, ele percebeu que não sabia muito  \033[34m   |')
print('|   \033[mBem como digitar os nomes na sua nova lista eletrônica. Ajude o  Professor\033[34m               |')
print('|   \033[ma digitar os nomes dos alunos: \033[34m                                                          |')
print('+', '-=' * 45, '+')

# Usuario digita os nomes dos alunos.
aluno1 = str(input('\033[mNome do primeiro aluno: ')).title()
aluno2 = str(input('Nome do segundo aluno: ')).title()
aluno3 = str(input('Nome do terceiro aluno: ')).title()
aluno4 = str(input('Nome do quarto aluno: ')).title()
print('\033[34m+', '-=' * 45, '+')

# Lista e Imprime a Ordem aleatoria  de apresentacao dos trabalhos.
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('\033[m  A apresentacao dos trabalhos sera nessa ordem {}'.format(lista))
print('\033[34m+', '-=' * 45, '+')
