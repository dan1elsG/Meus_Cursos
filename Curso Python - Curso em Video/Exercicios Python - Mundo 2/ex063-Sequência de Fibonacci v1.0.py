numero = int(input('Digite um numero: '))
termo = 0
termo1 = 1
print('{} -> {}'.format(termo, termo1), end='')
cont = 3
while cont <= numero:
    termo3 = termo + termo1
    termo = termo1
    termo1 = termo3
    print(' -> {}'.format(termo3), end='')
    cont = cont + 1
print(' -> FIM')
