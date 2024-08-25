lista = []
impares = []
pares = []
c = 0
res = ' '
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 or n % 2 == 1:
        lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    c += 1
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res in 'N':
        break
    else:
        res = ' '
print(f'A lista de numeros digitados e {lista}')
print(f'A lista de numeros pares digitados e {pares}')
print(f'A lista de numeros impares digitados e {impares}')
