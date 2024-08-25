from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format('Primeiro e último nome de uma pessoa'), '\n', '-=' * 40)
sleep(1)

# Pedi para o usuario digitar seu nome completo.
Nome = str(input('digite seu nome completo: ')).title().strip()
sleep(1)
print('-=' * 40)

# Quebra em cada espaco e separa o ultimo eo primeiro.
nome = Nome.split()
print('Prazer em te conhecer {} !'.format(Nome))
sleep(1)
print('-=' * 40)
print('seu primeiro nome e {}'.format(nome[0]))
sleep(1)
print('-=' * 40)
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))
