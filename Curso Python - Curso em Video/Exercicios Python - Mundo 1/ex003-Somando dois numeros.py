from time import sleep  # filtro para importar apenas a funcao sleep da biblioteca time.

print('\033[34m-=' * 40)  # infeite do programa.
print('{:^80}'.format('Exercicio 003'))
print('-=' * 40)
input('\033[mAperte enter para continuar....')  # comando pedi para apertar qual quer tecla ou enter,Para continuar.
sleep(1)  # Funcao faz o programa "dormir" por alguns segundos.
print('\033[34m-=' * 40)
print('\033[32mCrie um programa que lei dois numeros e mostre a soma entre eles.\033[m')  # Perguta do exercicio
print('\033[34m-=' * 40)
print('\033[31mPROCESSANDO A RESPOSTA....3')
sleep(1)
print('2')
sleep(1)
print('1')
print('-=' * 40)
sleep(1)
numerox = (int(input('\033[32mdigite um numero: ')))  # Pedi ao usuario para digitar dois numeros.
numeroy = (int(input('digite um outro numero: ')))
soma = numerox + numeroy  # Realiza a soma entre os numeros que o usuario digitou.
print('\033[mA soma entre {} e {} vale {}'.format(numerox, numeroy, soma))  # imprime na tela  a soma entre os
# numeros digitados pelo usuario.
