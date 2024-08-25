from datetime import date

print('-=' * 40, '\n{:^80}'.format('Verifica  ano bissexto'), '\n', '-=' * 40)
ano = int(input('Digite um ano: '))
# Verifica se o Ano e bissexto.
if ano == 0:
    ano = date.today().year
    print('ano atual e {}'.format(ano))
elif ano % 100 == 0 and ano % 400 == 0 or ano % 4 == 0 or ano % 400 == 0:
    print('Ano bissexto')
elif ano % 4 != 0 or ano % 400 != 0 and ano % 100 == 0:
    print('esse ano nao e bissexto')
