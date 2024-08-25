from time import sleep  # importa a fucao sleep da biblioteca time

print('\033[34m>>===>-' * 13, '\n{:^80}'.format('Exercicio 037'), '\n', '>>===>-' * 13)  # firula para deixar o programa
# mais bonito
print('\033[36mPROCESSADO.....\033[31m\n', '>>===>❤' * 13)
sleep(1)  # Faz o programa "Dormir" por alguns segundos.
print('''\033[mCrie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma 
mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO''''\033[31m\n', '>>===>❤' * 13)
# Enunciado da questao.
sleep(2)
print('{:^80}'.format('Calculador de Media V1'))
print('\033[31m>>===>❤' * 13)
nota1 = float(input('\033[mQual a primeira nota:'))  # Pedi pro usuario digitar as notas.
nota2 = float(input('Qual a segunda nota: '))
media = (nota1 + nota2) / 2  # Calcula as notas que o usuario digitou.
sleep(2)
if media < 5.0:  # Se media for menor ou 5.0 aluno reprovado.
    print('A media deste aluno foi {} pts com essa nota ele esta reprovado'.format(media))
elif 5.0 <= media <= 6.9:  # Se media estiver entre 5.0 ate 6.9 aluno esta de recuperacao.
    print('A media deste aluno foi {} pts com esta  nota ele esta de Recuperacao'.format(media))
elif media >= 7.0:  # Se media for maior que 7.0 aluno aprovado.
    print('A media deste aluno foi {} pts com esta nota ele esta aprovado'.format(media))  # Com base na media o
    # programa exibi na tela a mesagem falando se o usuario foi aprovado ou reprovado.
