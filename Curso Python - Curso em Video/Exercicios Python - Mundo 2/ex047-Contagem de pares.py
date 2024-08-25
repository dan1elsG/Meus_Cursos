print('\033[1;36m-=' * 40, '\n{:^80}'.format('CONTAGEM DE NUMEROS PARES'), '\n', '-=' * 40)
numero = int(input('digite um numeros: '))
for conte in range(0, numero+1):
    if conte % 2 == 0:
        print('{: }'.format(conte), end='')
print(', Acabou...')
