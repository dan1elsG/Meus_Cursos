print('\033[1m-=' * 40, '\n{:^80}'.format('Maior e Menor Valores'), '\n', '-=' * 40)
# Pedi ao Usuario para  Digitar 3 numeros
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

# Verifica Numero Maior
numeromaior = numero1
if numero2 >= numero3 and numero2 >= numero1:
    numeromaior = numero2
elif numero3 >= numero2 and numero3 >= numero1:
    numeromaior = numero3
print('numero Maior: {}'.format(numeromaior))

# Verifica Numero Menor
numeromenor = numero1
if numero2 <= numero3 and numero2 <= numero1:
    numeromenor = numero2
elif numero3 <= numero2 and numero3 <= numero1:
    numeromenor = numero3
print('numero Menor: {}'.format(numeromenor))
