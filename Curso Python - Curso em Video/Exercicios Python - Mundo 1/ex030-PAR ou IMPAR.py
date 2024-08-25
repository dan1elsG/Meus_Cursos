print('-=' * 40, '\n{:^80}'.format('IMPAR ou PAR'), '\n', '-=' * 40)
numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print('Numero {} e par'.format(numero))
else:
    print('Numero {} e impar'.format(numero))
