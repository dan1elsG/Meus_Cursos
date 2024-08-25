def dobro_(valor=0):
    dobro = valor*2
    return dobro


def metade_(valor=0):
    med = valor / 2
    return med


def aumentar_(valor=0, taxa=10):
    aumento = valor + (valor * (taxa/100))
    return aumento


def diminuir(valor=0, taxa=10):
    diminuindo = valor - (valor * (taxa/100))
    return diminuindo


def formatando(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
