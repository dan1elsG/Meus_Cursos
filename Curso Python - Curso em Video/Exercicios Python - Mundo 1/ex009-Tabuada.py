from time import sleep

print('\033[34m-=' * 40, '\n{:^80}'.format('Exercicio 009'), '\n', '-=' * 40)  # firula pra deixar o programa bonito.
sleep(0.6)  # Faz o programa "dormir" alguns segundos.
print('\033[35m faca um programa que leia um numero\n e qualquer e mostre sua tabuada.\n\033[m', '-=' * 40)
#  linha acima mostra o enunciado do exercicio.
sleep(0.9)
print('\033[32m Abrindo sua tabuada...\n\033[34m', '-=' * 40, '\n{:^80}'.format('TABUADA MULTIPLICACA'), '\n', '-=' *
      40)
sleep(0.10)
n = int(input('\033[mDigite um numero: '))  # Pedi pro usuario digitar um numero para fazer sua multiplicacao.
print('-=' * 40, '\n{:^80}'.format('MULTIPLICANDO'))
r1 = n * 2  # Faz a multiplicacao do numero digitado pelo usuario
r2 = n * 3
r3 = n * 4
r4 = n * 5
r5 = n * 6
r6 = n * 7
r7 = n * 8
r8 = n * 9
r9 = n * 10
print('{} X 2 = {}\n{} X 3 = {}\n{} X 4 = {}\n{} X '
      '5 = {}\n{} X 6 = {}\n{} X 7 = {}\n{} X 8 = {}\n{} X 9 = {}\n{} X 10 = {}'.format(n, r1, n, r2, n,
                                                                                        r3, n, r4, n, r5, n, r6,
                                                                                        n, r7, n, r8, n, r9))
# linha acima exibe a multiplicacao do numero digitado  pelo usuario.
print('-=' * 40)  # fim do programa
