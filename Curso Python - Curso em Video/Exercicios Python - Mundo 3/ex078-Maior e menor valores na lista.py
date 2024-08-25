valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {i}: ')))
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {max(valores)} e esta nas posicoes', end=' ')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}', end=" ")
print(f'\no menor valor digitado foi {min(valores)} e esta nas posicoes', end=' ')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}', end=" ")
