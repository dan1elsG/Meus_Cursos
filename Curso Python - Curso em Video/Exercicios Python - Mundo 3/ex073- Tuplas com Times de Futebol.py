times = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'Sao paulo', 'Cruzeiro', 'Atletico-MG', 'Bragantino',
         'Palmeiras', 'Internacional', 'Fortaleza', 'Gremio', 'Vasco da Gama', 'Criciuma', 'Juventude', 'Corinthians',
         'Fluminense', 'EC  Vitoria', 'Atletico-GO', 'Cuiaba')
print('-=' * 20)
cont = 0
for posicao in times:
    cont += 1
    print(f'{cont} - {posicao}')
print('-=' * 20)
print('Os Cinco primeiros colocados da tabela S)ão: {}'.format(times[:5]))
print('-=' * 20)
print('Os 4 Ultimos Colocados São: {}'.format(times[-4:]))
print('-=' * 20)
print('O Corinthians esta nak colocação: {}'.format(times.index('Corinthians') + 1))
print('-=' * 20)
print(f'times em ordem alfabetica {sorted(times)}')
