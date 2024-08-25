from datetime import date
from time import sleep

print('-=' * 40, '\n{:^80}'.format('CLASSIFICANDO ATLETAS'), '\n', '-=' * 40)  # imprimi o nome da atividade.
print(''' CLASSIFICACOES:
– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER\n''', '-=' * 40)
sleep(3)  # Faz o programar "Dormir" por alguns segundos.
nascimento = int(input('Digite o ano do nascimento: '))  # pedi ao usuario o ano do nascimento.
ano = date.today().year  # mostra o ano atual que estamos.
idade = ano - nascimento  # Calcula a idade do usuario.
print('O atleta tem {} anos.'.format(idade))
sleep(1)
print('Classificacao: ', end='')  # imprime a classificacao do atleta.

if idade <= 9:
    print('Mirin')
elif 10 <= idade <= 14:
    print('Infantil')
elif 15 <= idade <= 19:
    print('Junior')
elif 20 <= idade <= 25:
    print('Senior')
else:
    print('Master')  # fim do programa.
