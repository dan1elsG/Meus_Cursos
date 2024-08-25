from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format(' Verificando as primeiras letras de um texto'), '\n', '-=' * 40)
sleep(1)

# pedi pro usuario dogotar o nome du uma cidade.
Cidade = str(input('Digite o nome da sua Cidade: ')).title().split()
print('-=' * 40)
sleep(1)

# Verifica se o nome comeca com santo e imprime na tela se e verdadeiro ou falso.
print('Essa cidade comeca com Santo? {}'.format(Cidade[0] in 'Santo'))
