from time import sleep

print('\033[34m>===>' * 15, '\n{:^80}'.format('Exercicio 011'), '\n', '>===>' * 15)  # firula pra deixar o programa bonito.
sleep(0.6)  # Faz o programa "dormir" alguns segundos.
print('\033[35m Faca um programa que leia a largura ea altura de uma parede em metros,'
      '\ncalcule a sua area ea quantidade  de tinta necessaria para pinta-la,'
      '\nsabendo que cada litro de tinta pinta uma area de 2 metros quadrados.\n\033[m', '-=' * 40)
#  linha acima mostra o enunciado do exercicio.
sleep(0.9)
print('{:^80}'.format('\033[34mPINTANDO PAREDE\033[m'), '\n',  '-=' * 40)
largura = float(input('Qual a largura da parede que voce deseja pintar? '))  # Pedi pra digitar a largura.
print('-=' * 40)
sleep(0.7)
altura = float(input('qual a altura da parede? '))  # Pedi pra digitar a altura.
print('-=' * 40)
sleep(0.7)
area = largura * altura  # Calcula a area.
tinta = area / 2  # Faz calculo pra saber quantos litros de tinta vai ser usado pra pintar a parede.
print('Sua parede tem {} de altura e {} de largura e gastara {} litros de tinta'.format(altura, largura, tinta))
print('-=' * 40)  # Fim do programa.
