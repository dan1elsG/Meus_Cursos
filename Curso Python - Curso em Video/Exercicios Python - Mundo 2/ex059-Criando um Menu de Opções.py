
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] Somar Valores.'
          '\n[2] Multiplicar Valores.'
          '\n[3] Maior Valor.'
          '\n[4] Novos Valores.'
          '\n[5] Sair do Programa.')
    opcao = int(input('>>>>>>> Qual Sua opcao:'))
    if opcao == 1:
        print('A soma de {} e {} vale {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicacao {} X {} vale {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior numero e: {}'.format(num1))
        else:
            print('O maior numero e: {}'.format(num2))
    elif opcao == 4:
        print("digite os numeros novamente")
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
print('Fim do Programa!')
