total = valor = quanditade_acima_de_1000 = preco = barato = cont = 0
nome_produto_barato = nome = ' '
print('====Loja do produto=====')
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preco do produto: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < barato:
        barato = preco
        nome_produto_barato = nome
    if preco > 1000:
        quanditade_acima_de_1000 += 1
    continua = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while continua == 'SN':
        continua = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print(f'Total da compra: R${total}')
print(f'Foram {quanditade_acima_de_1000} Produtos acima de 1000 reais.')
print(f'O produto mais barato foi {nome_produto_barato} que custa R${barato:.2f}')
