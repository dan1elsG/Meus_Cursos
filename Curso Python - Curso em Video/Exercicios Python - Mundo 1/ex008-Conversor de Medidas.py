from time import sleep  # importa a funcao sleep da biblioteca ou modulo time.

print('\033[34m-=' * 40)
print('{:^80}'.format('Exercicio 008'))
print('-=' * 40)  # Firula para  deixar o programa mais bonito
sleep(0.6)  # Faz o programa "DORMIR" por alguns segundos.
print('\033[35mEscreva um programa que leia  um valor em metros\nea exiba convertido em centimetros e milimetros\033[m')
# Codigo acima mostra o enuciado do exercicio 8.
print('\033[37m-#-' * 27)
sleep(0.8)
print('\033[33mPROCESSANDO A RESPOSTA....')  # Programa esta "Processando a Resposta".
sleep(3)
print('\033[34m==' * 40)
print('{:^80}'.format('CONVERSOR DE MEDIDAS.'))
print('{:^80}'.format('Converte de Metros Para Centimetros e Milimetros.'))
print('\033[34m==' * 40)  # Linha 13,14,15 e 16 Imprime na tela um painel com o nome conversor de medidas
metros = float(input('\033[36mDigite um Valor em Metros:\033[m '))  # Pedi ao usuario para digitar um numero em metros.
sleep(1)
centimetros = metros * 100  # Faz o calculo de metros para centimetros.
milimetro = centimetros * 100  # Faz o calculo de centimetos para milimetros.
print('\033[34m==' * 40)
print('Valor Digitado: {}m\nCentimetros: {}cm\nMilimetros: {}mm'.format(metros, centimetros, milimetro))
# Imprime na tela os valores que o usuario digitou em cm e mm.
print('\033[34m==' * 40)
