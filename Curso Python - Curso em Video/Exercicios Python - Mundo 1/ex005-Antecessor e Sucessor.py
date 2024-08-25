from time import sleep   # importa a funcao sleep da biblioteca ou modulo time.

print('\033[34m-=' * 40)
print('{:^80}'.format('Exercicio 005'))
print('-=' * 40)  # firula para  deixar o programa mais bonito
sleep(0.6)  # Faz o programa "DORMIR" por alguns segundos.
print('\033[35mFaca um programa que leia um nimero inteiro\ne mostre na tela  o seu sucessor e seu antecesor.\033[m')
# Codigo acima mostra o enuciado do exercicio 5.
print('\033[37m-#-' * 27)
sleep(0.8)
print('\033[33mPROCESSANDO A RESPOSTA....')  # Programa esta "Processando a Resposta".
sleep(3)
print('\033[37m-#-' * 27)
sleep(0.3)
numero = int(input('\033[36mDigite um numero para mostrar seu sucessor e seu antecessor: \033[m'))  # Pedi ao usuario -
# para digitar um  numero.
sleep(1)
print('Numero digitado: {}'.format(numero))
sleep(0.9)
print('\033[32msucessor\033[m: {}'.format(numero + 1))  # Calcula e imprime o numero sucessor do digitado pelo usuario.
sleep(0.9)
print('\033[31mantecessor\033[m: {}'.format(numero - 1))  # Calcula e imprime o numero sucessor do digitado pelo usuario
sleep(2)

