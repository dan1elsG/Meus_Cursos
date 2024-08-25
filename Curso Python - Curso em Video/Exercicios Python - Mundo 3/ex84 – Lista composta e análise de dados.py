dados = list()
pesado = list()
leves = list()
resp = ''
cont = 0
while True:
    cont += 1
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if cont == 1:
        pesado.append(dados[:])
        leves.append(dados[:])
        dados.clear()
    else:
        for p in pesado:
            if p[1] < dados[-1]:
                pesado.clear()
                pesado.append(dados[:])
            elif p[1] == dados[1]:
                pesado.append(dados[:])
                break
        for p in leves:
            if p[1] > dados[-1]:
                leves.clear()
                leves.append(dados[:])
            elif p[1] == dados[1]:
                leves.append(dados[:])
                break
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    resp = ''
    dados.clear()
print(f'{cont} pessoas foram cadastradas')
print(f'O maior peso foi de {(pesado[0][1])}Kg.PESO DE ', end=" ")
for p in pesado:
    print(f'{p[0]}', end='')
print(f'\nO menor peso foi de {(leves[0][1])}Kg.PESO DE ', end=' ')
for p in leves:
    print(f'{p[0]}', end='')
