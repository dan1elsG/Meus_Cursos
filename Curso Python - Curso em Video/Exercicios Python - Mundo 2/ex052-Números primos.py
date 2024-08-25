
n = int(input('Digite um Numero:'))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', c, end=' ')
        cont += 1
    else:
        print('\033[31m', c, end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, cont))
if cont == 2:
    print('e por isso ele e numero primo')
else:
    print('e por isso ele nao e numero primo')
