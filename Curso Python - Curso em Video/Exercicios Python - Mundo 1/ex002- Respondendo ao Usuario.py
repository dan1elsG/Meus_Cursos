from time import sleep  # Codigo para importar a apenas a funcao sleep da biblioteca time.

print('\033[34m-=' * 50)  # imprime na tela 50 vezes -= na cor azul.
print('{:^100}'.format('Exercicio 002'))  # Codigo para Centralizar o nome exercicio 002.
print('-=' * 50)
input('\033[mAperte e tecla enter para continar...')  # Codigo para deixar que o usuario aperte enter para continuar.
print('\033[34m=' * 100)
print('\033[35m Faca um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.\033[m')  # Codigo
# para mostrar o enuciado do exercicio na cor roxa.
print('\033[34m-=' * 50)
sleep(1.2)  # Faz o programa "dormir" por alguns segundos.
print('\033[31mPROCESSANDO A RESPOSTA.....\033[m')  # Codigo para "Processar a resposta".
sleep(0.7)
nome = input('\033[37mDigite seu nome: ').title()  # Pedi para o usuario digitar o nome e automaticamente formata o nome
# deixando a primeira letra maiuscula.
sleep(0.5)
print('\033[1;36m\nSeja Bem-Vindo {} !'.format(nome))  # Mostra ao usuario uma mensagen de boas vindas.
