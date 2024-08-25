from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format(' Primeira e última ocorrência de uma string'), '\n', '-=' * 40)
sleep(1)

# Pedi ao usuario para digitar uma frase.
frase = str(input('Digite Uma Frase:')).upper().strip()
print('-=' * 40)
sleep(1)

# Verifica aonde uma certa string esta.
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
sleep(1)
print('A  primeira letra A aparece na pisicao {}'.format(frase.find('A')+1))
sleep(1)
print('a ultima letra a apareceu na posicao {}'.format(frase.rfind('A')+1))
