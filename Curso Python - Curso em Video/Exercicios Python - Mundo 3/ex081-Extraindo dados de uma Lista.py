lista = []
c = 0
res = ' '
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res in 'N':
        break
    else:
        res = ' '
print(f'Valores em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('O Numero 5 nao esta na lista')
else:
    print('O Numero 5 esta na lista')
print(f'foi digitados {c} valores')
