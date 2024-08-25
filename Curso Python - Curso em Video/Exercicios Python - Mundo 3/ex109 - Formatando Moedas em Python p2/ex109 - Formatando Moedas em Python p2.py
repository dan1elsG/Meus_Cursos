import moedas


p = float(input('Digite um valor: '))
print(f'A metade de {moedas.formatando(p,)} vale {moedas.metade_(p, True)}')
print(f'O dobro de {moedas.formatando(p)} vale {moedas.dobro_(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar_(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir_(p, 13, True)}')
