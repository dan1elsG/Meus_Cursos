from time import sleep   # importa a fucao sleep da biblioteca time

print('\033[34m>>===>-' * 12, '\n{:^71}'.format('Exercicio 037'), '\n', '>>===>-' * 12)  # firula para deixar o programa
# mais bonito
print('\033[36mPROCESSADO.....\033[31m\n',  '>>===>❤' * 12)
sleep(2)  # Faz o programa "Dormir" por alguns segundos.
print('\033[mEscreva um programa em Python que leia um número inteiro qualquer e peça para o usuário\nescolher '
      'qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.\033[31m\n', '>>===>❤' * 12)
# Enunciado da questao.
sleep(1)
numero = int(input('\033[mdigite um numero inteiro:'))  # Pedi ao usuario Digitar um numero para ser Covertido.
binario = bin(numero)[2:]  # Faz o calculo do  numero digitado para binario e fatia o resultado.
octal = oct(numero)[2:]   # Faz o calculo do  numero digitado para octal e fatia o resultado.
hexadecimal = hex(numero)[2:]   # Faz o calculo do  numero digitado para hexadecimal e fatia o resultado.
print('-=' * 45, '''\033[36m
[ 1 ] para numero Binario
[ 2 ] para numero Octal
[ 3 ] para numero Hexadecimal\033[m\n''', '-=' * 45)
opcao = int(input('Sua Opcao:'))   # Cria uma lista com opcoes para o usuario escolher.
if opcao == 1:
    print('\033[32m{} Convertido para binario e igual a {} '.format(numero, binario))
elif opcao == 2:
    print('{} Convertido para Octal e igual a {} '.format(numero, octal))
elif opcao == 3:
    print('{} Convertido para Hexadecimal e igual a {} '.format(numero, hexadecimal))
else:
    print('\033[31mOpcao invalida. Tente Novamente!')  # Informa ao usuario de acordo com a opcao escolhida imprime
    # o resultado na tela.
