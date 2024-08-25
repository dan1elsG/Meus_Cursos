numero = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")),
          int(input("Digite mais um valor: ")), int(input("Digite o ultimo valor: ")))
print(f"O valores digitado foi {numero}")
if 3 in numero:
    print(f'O numero 3 apareceu na posicao {numero.index(3) + 1}')
else:
    print(f'O valor 3 nao apareceu em nenhuma posicao ')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
print('Os valores pares digitados foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(f'{n}', end=' ')
