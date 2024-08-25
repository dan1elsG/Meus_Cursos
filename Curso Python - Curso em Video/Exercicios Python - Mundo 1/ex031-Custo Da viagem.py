print('-=' * 40, '\n{:^80}'.format('Custo da viagem'), '\n', '-=' * 40)

viagem = int(input('digite  distacia da cidade aonde voce vai: '))
# Verifica se a viagem passa ou nao dos 200km
if viagem <= 200:
    preco = viagem * 0.50
    print('o valor da passagem e de {} reais'.format(preco))
else:
    preco = viagem * 0.45
    print('o valor da passagem e de {} reais'.format(preco))
