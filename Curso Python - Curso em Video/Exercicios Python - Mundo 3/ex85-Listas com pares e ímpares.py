td_numeros = [[], []]
for n in range(0, 7):
    numero = int(input(f'digite o {n + 1}o numero: '))
    if numero % 2 == 0:
        td_numeros[0].append(numero)
    if numero % 2 == 1:
        td_numeros[1].append(numero)
print(f'Os valores pares digitados foram {sorted(td_numeros[0])}')
print(f'Os valores impares digitados foram {sorted(td_numeros[1])}')
