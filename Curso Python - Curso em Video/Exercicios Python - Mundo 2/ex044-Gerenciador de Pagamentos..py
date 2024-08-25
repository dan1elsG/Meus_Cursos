from time import sleep

# Nome da Loja
print('\033[34m-==-' * 20, '\n\033[31m{:^80}'.format('LOJAS PAGUE MENOS'), '\n\033[34m', '-==-' * 20)
sleep(2)

# Apresentacao da assistente virtual
print('\033[m\n Ola Sou a Layla, sua assistente virtual. Vou te auxiliar na sua compra!')
sleep(1)

# Pedi pro Usuario digitar o valor da compra e mostras as opcoes para seguir com o pagamento.
preco = float(input(' Qual o valor da sua Compra: R$'))
forma_pagamento = int(input('Qual a sua forma de pagamento:\n'
                            '[ 1 ] A vista dinheiro/cheque.\n'
                            '[ 2 ] A vista no cartao.\n'
                            '[ 3 ] Em ate 2x no cartao.\n'
                            '[ 4 ] 3x ou mais no cartao.\n'
                            'Qual Sua opcao:'))
sleep(1)

# verifica a opcao digitada pelo usuario e informa o valor a ser pago.
if forma_pagamento == 1:
    desconto = preco - (preco * 10 / 100)
    print('O valor da Compra e de {}R$, pagando avista ficara {}R$. aperte enter para finalizar!'.format(preco,
                                                                                                         desconto))
    input('')
elif forma_pagamento == 2:
    desconto = preco - (preco * 5 / 100)
    print('O Valor da Compra e de {:.2f}R$, Pagando avista no cartao ficara {:.2f}R$. Aperte enter para finalizar!'.
          format(preco, desconto))
    input('')
elif forma_pagamento == 3:
    parcela = preco / 2
    print('O valor da Compra e de {:.2f}R$, Parcelando no Cartao ficara 2x de {:.2f}R$. Aperte enter para finalizar!'.
          format(preco, parcela))
    input('')
elif forma_pagamento == 4:
    parcela = int(input('Deseja parcelar em quantas vezes?'))
    if parcela == 2:
        parcela = preco / 2
        print(
            'O valor da Compra e de {:.2f}R$, Parcelando no Cartao ficara 2x de {:.2f}R$. Aperte enter para finalizar!'.
            format(preco, parcela))
    else:
        juros = preco + (preco * 20 / 100)
        parcelado_cartao = juros / parcela
        print('O valor da Compra e de {:.2f}R$, Parcelando no Cartao em {}x ficara {:.2f}R$ com 20% de juros. '
              'Aperte enter para finalizar!'.format(preco, parcela, parcelado_cartao))
        input('')
print('Pague menos agradece sua compra. Muito Obrigado!')
