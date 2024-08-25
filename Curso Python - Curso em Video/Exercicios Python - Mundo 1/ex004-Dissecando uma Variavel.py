from time import sleep  # importa a funcao sleep da biblioteca time.

print('\033[34m-=' * 40)
print('{:^80}'.format('Exercicio 004'))
print('-=' * 40)
sleep(1)  # Faz o programa "Dormir" por alguns segundos.
print('\033[35mFaca um programa que leia algo pelo teclado e mostre na tela\nseu tipo primitivo e todas as informacoes '
      'possiveis  sobre ele.\033[34m')  # Mostra o enunciado na tela na cor roxa.
print('-=' * 40)
sleep(0.6)
print('\033[31mPROCESSANDO A RESPOSTA....\033[m')  # O programa  ira "Processar a resposta".
print('-=' * 40)
sleep(3)
n = input('digite algo: ')  # Pedi ao Usuario para digitar algo.
print('\033[36mAlfabetico?\033[m', n.isalpha())  # Mostra se o que o usuario digitou e alfabetico.
print('\033[35mAlfanumerico?\033[m', n.isalnum())  # Mostra  se o que foi digitado e alfanumerico.
print('\033[34mNumerico?\033[m', n.isnumeric())  # Mostra se oque foi digitado e numerico.
print('\033[33mClasse?\033[m', type(n))  # Mostra a classe do que foi digitado pelo usuario.
print('\033[37mMinusculo?\033[m', n.islower())  # Mostra se o que foi digitado esta maiusculo.
print('\033[36mMaiusculo?\033[m', n.isupper())  # mostra se o que foi digitado esta minusculo.
print('\033[32mApenas espacos?\033[m', n.isspace())  # Mostra se  foi digitados apenas espacos pelo usuario.
print('\033[31mEsta capitalizado?\033[m', n.istitle())  # Mostra se o que o usuario digitou esta capitalizado.
print('-=' * 40)
