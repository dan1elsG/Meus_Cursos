print('-=' * 40, '\n{:^80}'.format('Radar Eletronico'), '\n', '-=' * 40)
km = int(input('qual a velocidade do seu carro: '))
# Verifica a Velocidade do carro e Impreme uma mensagem dizendo o valor da multa ou nao.
if km > 80:
    multa = (km - 80) * 7
    print('voce esta em {}km/h\nultrapassou o limite de 80km/h\nVoce recebera um multa no valor de {:.2f}R$.'.format(
        km, multa))
else:
    print('voce esta em {}km/h\nEsta velocidade permitida!'.format(km))
