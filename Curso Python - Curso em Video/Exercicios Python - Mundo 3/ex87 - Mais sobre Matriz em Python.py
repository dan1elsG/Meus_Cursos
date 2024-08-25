matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma1 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            if l == 0 and c == 0:
                soma += matriz[l][c]
        if l == 0 and c == 2:
            soma1 = matriz[l][c]
        elif l == 1 and c == 2:
            soma1 += matriz[l][c]
        elif l == 2 and c == 2:
            soma1 += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if l == 1:
            for c in range(0, 3):
                if matriz[c] == 0:
                    maior = matriz[l][c]
                if matriz[l][c] >= maior:
                    maior = matriz[l][c]
    print()
print(f'A soma dos valores pares e {soma}')
print(f'A soma dos valores da terceira coluna e {soma1}')
print(f'O maior valor da segunda linha e {maior}')
