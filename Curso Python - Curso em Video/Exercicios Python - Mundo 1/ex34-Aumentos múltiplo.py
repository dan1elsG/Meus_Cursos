from time import sleep
print('\033[1m-=' * 40, '\n{:^80}'.format('Aumentos Multiplos'), '\n', '-=' * 40)
sleep(1)
salario = float(input('Qual seu Salario: '))
sleep(1)
# Verifica o salario e aumenta caso o salario for R$1250 10% senao aumenta 15%.
if salario > 1250:
    aumento = salario + (salario * 10/100)
else:
    aumento = salario + (salario * 15/100)
print('seu  novo slario e R${:.2f}'.format(aumento))
