lista = ('lapis', 1.75, 'Caderno', 15.90, 'Estojo', 25, 'Canetas', 22.30, 'livros', 9.99, 'Mochila', 1.00)
print('-' * 40, '\n{:^40}'.format('Tabela de Precos'), '\n', '-' * 40)
contador = 0
while True:
    if contador == len(lista):
        break
    else:
        print(f'\n {lista[contador]:.<30}', f'R${lista[contador + 1]:.2f}')
        contador = contador + 2
print('-' * 40)
