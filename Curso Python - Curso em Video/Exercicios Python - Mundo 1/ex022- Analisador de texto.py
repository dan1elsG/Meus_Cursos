from time import sleep

print('\033[1m-=' * 40, '\n{:^80}'.format('Analisador de texto'), '\n', '-=' * 40)

sleep(1)  # Faz o Programa "Dormir" por alguns segundos.

nome = str(input('Digite Seu Nome Completo: '))   # Pedi para o Usuario digitar seu Nome completo.

print('-=' * 40)

# Formata o nome digitado
maiusculo = nome.upper()
minusculo = nome.lower()
formatado = nome.title()
nome_sem_espacos = len(nome.replace(" ", ""))
primeiro_nome = nome.split()
letras = len(primeiro_nome[0])

# Analisar o nome digitado.
print('Seu  Nome Conforme Voce Digitou: {}\n'.format(nome), '-=' * 40)
sleep(1)
print('Nome Maiusculo: {}\n'.format(maiusculo), '-=' * 40)
sleep(1)
print('Nome Minusculo: {}\n'.format(minusculo), '-=' * 40)
sleep(1)
print('Seu Primeiro Nome: {} \n'.format(primeiro_nome[0]), '-=' * 40)
sleep(1)
print('Quantidade de Letra que do seu Nome: {}\n'.format(nome_sem_espacos), '-=' * 40)
sleep(1)
print('Seu Primeiro Nome tem {} letras.\n'.format(letras), '-=' * 40)
sleep(1)
print('Seu Nome: {} :)\n'.format(formatado), '-=' * 40)
sleep(1)
print('Nome Analisado com Sucesso.........')
