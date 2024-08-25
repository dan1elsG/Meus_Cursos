n1 = int(input('Quantos numero deseja somar: '))
soma = 0
for c in range(1, n1 + 1):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
print('{: }'.format(soma), end='')


