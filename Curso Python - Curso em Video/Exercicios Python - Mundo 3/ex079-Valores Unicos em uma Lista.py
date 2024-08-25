
valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
    if c == 'N':
        break
    for pos in range(0, len(valor) - 1):
        while valor[pos] == valor[-1]:
            print('Valor duplicado! Nao sera adicionado a lista!')
            valor.pop(-1)
            valor.append(int(input('Digite um valor: ')))

print(list(sorted(valor)))
