from time import sleep  # importa a fucao sleep da biblioteca time

print('\033[34m>>===>-' * 13, '\n{:^80}'.format('Exercicio 037'), '\n', '>>===>-' * 13)  # firula para deixar o programa
# mais bonito
print('\033[36mPROCESSADO.....\033[31m\n', '>>===>❤' * 13)
sleep(2)  # Faz o programa "Dormir" por alguns segundos.
print('\033[m''''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais\033[31m\n''''', '>>===>❤' * 13)
# Enunciado da questao.
sleep(1)
print('\033[35m{:^80}'.format('COMPARANDO NUMEROS'), '\n', '>>===>❤' * 13)
numero = int(input('\033[mDigite o primerio numero:'))
numero1 = int(input('Digite o segundo numero:'))  # pedi pro usuario digitar dois numeros para comparalos.
print('\033[35m{}'.format('CALCULANDO A RESPOSTA'), '\n', '>>===>❤' * 13, '\033[m')
sleep(1)
if numero > numero1:
    print('O primeiro numero e maior')  # informa se o numero for maior que numero1
elif numero < numero1:
    print('O Segundo numero e maior')  # informa se o numero for menor que o numero1
else:
    print('Nao existe numero maior, pois os dois sao iguais.')  # informa se o numero eo numero1 sao iguais
