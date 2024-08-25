from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format('Separando Digitos de um Numero'), '\n', '-=' * 40)
sleep(1)

# pedi pro usuario digitar 4 numeros.
numero = int(input('Digite um Numero com ate 4 Digitos: '))
print('-=' * 40)
sleep(1)

# Calculo para separar os numeros.
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Imprime as unidades dezenas centenas e milhar do  numero digitado.
print(' Numero Digitado: {}\n'
      ' {} unidade.\n '
      '{} dezenas.\n '
      '{} centenas.\n '
      '{} milhar.'.format(numero, unidade, dezena, centena, milhar))
