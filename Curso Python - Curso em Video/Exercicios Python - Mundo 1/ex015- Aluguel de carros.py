from time import sleep

# exebi nome do exercicio.
print('\033[34m-o--o-' * 13, '\n{:^78}'.format('Aluguel De Carros'), '\n', '-o--o-' * 13)

# Historia do exercicio.
print('\033[mEm uma cidade tranquila chamada "Viva Rodas", onde as estradas eram ladeadas\npor campos verdejantes, algo'
      'empolgante estava prestes a acontecer.\nUma nova loja de aluguel de carros, chamada "Caminho Fácil",'
      ' abriu suas portas,\ntrazendo consigo a promessa de uma experiência de aluguel revolucionária.\033[34m\n',
      '-O--O-' * 13)
sleep(1)

# Usuario tem que digitar quantos dias pretende fica com os carros.
print('\033[mPara iniciarmos, por favor, informe quantos dias você pretende ficar com o\nnosso carro na '
      'Caminho Fácil - Aluguel de Carros', end='')
dias_alugado = int(input(': \033[34m'))
print('-o--o-' * 13)
sleep(1)

# Usuario tera que digitar quantos  km vai percorrer com o carro.
print('\033[mPara darmos continuidade, gentileza informar quantos quilômetros você pretende\npercorrer com o nosso'
      'carro na Caminho Fácil - Aluguel de Carros', end='')
km_rodados = float(input(': \033[34m'))
print('-o--o-' * 13)
sleep(1)

# Calcula e Imprimi o valor a ser pago pelo usuario.
valor_a_pagar = (dias_alugado * 60) + (km_rodados * 0.15)
print('''\033[mÓtimo! Com base nas informações fornecidas, o custo total do seu aluguel com a 
Caminho Fácil - Aluguel de Carros' será de R${}. Aproveite a sua viagem em\nViva Rodas!\033[34m'''.format(valor_a_pagar)
      )
print('-o--o-' * 13)
