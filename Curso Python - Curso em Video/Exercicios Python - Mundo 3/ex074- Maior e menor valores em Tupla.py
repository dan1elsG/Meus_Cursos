from random import randint

# Randomiza uma tupla
lista = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
# maior = menor = lista
# Mostra os Valores Sorteados
print('Os valores sorteados foram: ', end='')
for contador in lista:
    print(f'{contador}', end=" ")

# Verica qual numero e maior e menor
#    if maior < contador:
#       maior = contador
#    if menor > contador:
#       menor = contador

# Mostra o maior e menor valor
# print(f'\nO Maior numero sorteado foi: {maior}')
# print(f'O Menor numero sorteado foi: {menor}')
print(f'\nO Maior numero sorteado foi: {max(lista)}')
print(f'O Menor numero sorteado foi: {min(lista)}')
