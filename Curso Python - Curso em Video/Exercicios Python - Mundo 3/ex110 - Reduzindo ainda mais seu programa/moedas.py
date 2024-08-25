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
    return diminuindo if formato is False else formatando(diminuindo)


def formatando(valor=0, moeda='R$'):
    return f'{moeda}{valor:8.2f}'.replace('.', ',')


def resumo(valor=0, taxa=10, taxa1=10):
    print('', '-=' * 25, f'\n{"RESUMO DO VALOR":^50}\n', '-=' * 25)
    print(f"PRECO ANALISADO: \t{formatando(valor):>33}\n"
          f"DOBRO DO PRECO: \t{dobro_(valor, formato=True):>33}\n"
          f"METADE DO PRECO: \t{metade_(valor, formato=True):>33}\n"
          f"{taxa}% DE AUMENTO: \t{aumentar_(valor, taxa, formato=True):>33}\n"
          f"{taxa1}% DE REDUCAO: \t\t{diminuir_(valor, taxa1, formato=True):>33}")
    print('-=' * 25)

