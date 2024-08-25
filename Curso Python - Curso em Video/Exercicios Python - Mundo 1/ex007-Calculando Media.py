from time import sleep  # importa a funcao sleep da biblioteca ou modulo time.

print('\033[34m-=' * 40)
print('{:^80}'.format('Exercicio 007'))
print('-=' * 40)  # Firula para  deixar o programa mais bonito
sleep(0.6)  # Faz o programa "DORMIR" por alguns segundos.
print('\033[35mDesenvolva um programa que leia duas notas \nde um aluno e calcule e mostre a sua media.\033[m')
# Codigo acima mostra o enuciado do exercicio 7.
print('\033[37m-#-' * 27)
sleep(0.8)
print('\033[33mPROCESSANDO A RESPOSTA....')  # Programa esta "Processando a Resposta".
sleep(3)
print('\033[33mGERANDO CALCULADORA DE MEDIA...')
print('\033[37m-#-' * 27)
sleep(0.3)
print('{:^80}\n{}'.format('\033[34mCAlCULADOR DE MEDIA DE ALUNOS', '--' * 40))
nota1 = float(input('\033[mDigite a primeira nota: '))  # Pedi pro usuario digitar a nota do aluno.
print('\033[32mSALVANDO A  PRIMEIRA NOTA...\033[m')  # Exibe a mensagem Salvando nota.
sleep(0.5)
nota2 = float(input('Digite a segunda nota: '))  # Pedi para o usuario digitar as notas dos alunos.
print('\033[32mSALVANDO A  SEGUNDA NOTA...\033[m')  # Exibe a mensagem Salvando nota.
sleep(0.5)
input('NOTAS SALVAS COM SUCESSO CLIQUE ENTER PARA CONTINUAR....')  # Pedi ao usuario para mostrar a media da nota.
sleep(1)
media = (nota1 + nota2) / 2  # Calcula a media das notas digitadas.
print('\033[34m-=' * 40)
print('\033[m A MEDIA DESSE ALUNO E {:.1f}'.format(media))  # Mostra o resultado das medias do aluno
print('\033[34m-=' * 40)  # Fim do programa.
