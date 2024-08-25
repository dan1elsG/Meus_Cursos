from time import sleep

print('\033[34m-=' * 40, '\n{:^80}'.format('Exercicio 010'), '\n', '-=' * 40)  # firula pra deixar o programa bonito.
sleep(0.6)  # Faz o programa "dormir" alguns segundos.
print('\033[35m Crie um programa que leia quanto dinheiro uma pessoa\ntem na carteira e mostre quantos Dolares ela'
      ' pode comprar.\nConsidere: US$1.00 = 4.87\n\033[m', '-=' * 40)
#  linha acima mostra o enunciado do exercicio.
sleep(0.9)
print('{:^80}'.format('\033[34mCONVERSOR DE MOEDAS\033[m'), '\n', '-=' * 40)
sleep(0.10)
reais = float(input('\033[32mQuantos reais voce tem na carteira?\033[m  '))  # Pedi ao usuario para digitar um numero.
sleep(0.9)
dolar = reais / 4.87  # Converte  o valor para dolar
print('-=' * 40, '\n\033[35mCONVERTENDO...\033[m')
sleep(0.6)
print('-=' * 40, '\n\033[34mVOCE PODE COMPRAR {:.2f} DOLARES.'.format(dolar))  # Exibe o valor digitado convertido.
