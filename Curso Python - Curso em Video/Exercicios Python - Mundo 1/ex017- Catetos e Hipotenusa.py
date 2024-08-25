from time import sleep

# Nome do exercicio.
print('\033[34m=====>' * 13, '\n{:^78}'.format('Cateto e hipotenusa'), '\n', '=====>' * 13)
sleep(1)  # Faz o programar esperar alguns segundos.

# usuario digita o valor dos catetos.
cateto_oposto = float(input('\033[mcomprimento do cateto oposto: '))
print('\033[34m=====>' * 13)
cateto_adjacente = float(input('\033[mcumprimento do cateto adjacente: '))
print('\033[34m=====>' * 13)
sleep(2)

# Faz os Calculos do catetos digitado.
hipotenusa = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
total = hipotenusa ** (1/2)

# Imprimi o valor da hipotenusa.
print('\033[mA hipotenusa vai medir {:.2f}'.format(total))
print('\033[34m=====>' * 13)
