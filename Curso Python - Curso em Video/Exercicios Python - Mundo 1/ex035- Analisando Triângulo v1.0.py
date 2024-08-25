
# Nome Do exercicio.
print(' \033[1;34m{:=^40}\n'.format(''), '{:^40}\n'.format(' Analisando Triângulo v1.0'), '{:-^40}'.format(''))

# pedi ao usuario para digitar um  numero.
a = int(input('digite o primeiro numero: '))
b = int(input('digite o seundo numero: '))
c = int(input('digite o terceiro numero: '))

# Verifica se os numeros digitados formam um triangulo.
if a + b > c and b + c > a and c + a > b:
    print('esse numeros formam um triaangulo')
else:
    print('esses numeros nao forman um triangulo')
