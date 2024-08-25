from time import sleep  # importa a funcao sleep da biblioteca ou modulo time.

print('\033[34m-=' * 40)
print('{:^80}'.format('Exercicio 006'))
print('-=' * 40)  # firula para  deixar o programa mais bonito
sleep(0.6)  # Faz o programa "DORMIR" por alguns segundos.
print('\033[35mCrie um algoritimo que leia um numero e mostre o\nseu dobro triplo e raiz quadrada\033[m')
# Codigo acima mostra o enuciado do exercicio 6.
print('\033[37m-#-' * 27)
sleep(0.8)
print('\033[33mPROCESSANDO A RESPOSTA....')  # Programa esta "Processando a Resposta".
sleep(3)
print('\033[37m-#-' * 27)
sleep(0.3)
numero = int(input('\33[mDigite um numero para calcular seu dobro, triplo e raiz quadrada: '))  # Pedi ao usuario para
# digitar um numero.
print('-=' * 40)
sleep(1)
dobro = numero * 2  # Calcula o Dobro do numero digitado pelo usuario.
print('\033[33mCALCULANDO O DOBRO...')
sleep(0.2)
print('\033[37m-=' * 40)
triplo = numero * 3  # Calcula o Triplo do numero digitado pelo usuario.
print('\033[33mCALCULANDO O TRIPLO...')
sleep(0.4)
print('\033[37m-=' * 40)
raiz = numero ** (1 / 2)  # Calcula a raiz quadrada do numero digitado pelo usuario.
print('\033[33mCALCULANDO A RAIZ QUADRADA...')
sleep(0.6)
print('\033[37m-=' * 40)
print('\033[33mIMPRIMINDO A RESPOSTA...')
sleep(1)
print('\033[37m-=' * 40)
print('\033[mNumero digitado: {}\nDobro: {}\nTriplo: {}\nraiz quadrada: {:.2f}'.format(numero, dobro, triplo, raiz)
      )  # Codigo imprime o dobro, triplo e raiz quadrada do numero digitado pelo usuario.
print('\033[37m-=' * 40)  # Fim do Programa.
