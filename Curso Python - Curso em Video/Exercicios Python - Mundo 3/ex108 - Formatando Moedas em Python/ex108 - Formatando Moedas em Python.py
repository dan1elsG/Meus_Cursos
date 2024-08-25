import moedas


p = float(input('Digite um valor: '))
print(f'A metade de {moedas.formatando(p)} vale {moedas.formatando(moedas.metade_(p))}')
print(f'O dobro de {moedas.formatando(p)} vale {moedas.formatando(moedas.dobro_(p))}')
print(f'Aumentando 10%, temos {moedas.formatando(moedas.aumentar_(p))}')
