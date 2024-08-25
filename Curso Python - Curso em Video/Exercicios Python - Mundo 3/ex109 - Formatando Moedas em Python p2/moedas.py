def dobro_(valor=0, formato=False, moeda='R$'):
    dobro = valor*2
    return dobro if formato is False else formatando(dobro)


def metade_(valor=0, formato=False, moeda='R$'):
    med = valor / 2
    return med if formato is False else formatando(med)


def aumentar_(valor=0, taxa=10, formato=False, moeda='R$'):
    aumento = valor + (valor * (taxa/100))
    return aumento if formato is False else formatando(aumento)


def diminuir_(valor=0, taxa=10, formato=False, moeda='R$'):
    diminuindo = valor - (valor * (taxa/100))
    if formato:
        return f'{moeda}{diminuindo:.2f}'.replace('.', ',')
    else:
        return diminuindo


def formatando(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
