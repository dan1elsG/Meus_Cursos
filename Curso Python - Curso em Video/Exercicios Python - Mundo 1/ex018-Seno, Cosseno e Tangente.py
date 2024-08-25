# importa a biblioteca math
import math

# Nome Do exercicio.
print(' \033[34m{:=^40}\n'.format(''), '{:^40}\n'.format('Seno, Cosseno e Tangente'), '{:-^40}'.format(''))

# Pedi ao usuario para digitar um angulo.
angulo = float(input('\033[mdigite um angulo qualquer : '))
print('\033[34m-=' * 20)

# Calcula o seno cosseno e tangente do angulo digitado.
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Imprime o valor calculado do seno, cosseno e tangente.
print('\033[mAngulo digitado: {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f} '.format(angulo, seno,
                                                                                               cosseno, tangente))
print('\033[34m-=' * 20)
