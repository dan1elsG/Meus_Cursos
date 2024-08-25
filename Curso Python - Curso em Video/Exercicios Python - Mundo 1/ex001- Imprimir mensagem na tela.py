from time import sleep  # importa a funcao sleep da biblioteca time.

print('\033[34m-=' * 40)  # firula para deixar o programa mais bonito.
print('{:^80}'.format('Exercicio 001'))  # Centraliza o nome exercicio 001.
print('-=' * 40)
input('\033[mAperte a tecla enter para continuar.....')  # Deixa o usuario digitar apertar enter para cotinuar.
print('\033[34m-=' * 40)
sleep(2)  # faz o programa "dormi" por alguns segundos.
print('\033[35mCrie um programa que escreva "Ola,Mundo!" na tela.\033[m')  # Mostra o enuciado na cor roxa.
print('\033[34m-=\033[m' * 40)
print('\033[31mPROCESSANDO A RESPOSTA AGUARDE.....\033[m')  # programa esta, "Processando a resposta".
sleep(2)
print('\033[32mOla,Mundo!\033[32m')  # imprime uma mensagem na tela.
