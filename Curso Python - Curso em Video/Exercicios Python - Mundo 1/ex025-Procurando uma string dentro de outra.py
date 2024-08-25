from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format(' Procurando uma string dentro de outra'), '\n', '-=' * 40)
sleep(1)

# pedi para o usuario digitar seunome completo.
nome = str(input('digite seu nome completo: ')).title().strip()
print('-=' * 40)
sleep(1)

# Verifica  se o nome tem silva e imprimne na tela verdadeiro ou falso.
print('Seu Nome tem Silva? {}'.format('Silva' in nome))
