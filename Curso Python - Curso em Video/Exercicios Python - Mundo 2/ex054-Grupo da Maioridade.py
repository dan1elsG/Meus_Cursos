from datetime import date
ano_atual = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    ano = int(input('Digite o ano que a {} pessoa nasceu:'.format(c)))
    idade = ano_atual - ano
    if idade >= 18:
        cont += 1
    else:
        cont1 += 1
print('{} pessoas maiores de 18 anos e {} pessoas menores de 18 anos'.format(cont, cont1))
