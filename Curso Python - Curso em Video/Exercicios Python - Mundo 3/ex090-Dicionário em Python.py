from time import sleep
situacao = ''
aluno = {}
nome = str(input('Nome: '))
media = float(input(f'Qual a media de {nome}:'))
if media >= 7:
    situacao = 'Aprovado'
elif 5 <= media < 7:
    situacao = 'Recuperacao'
elif media < 5:
    situacao = 'Reprovado'
aluno = {'Nome': nome, 'Media': media, 'situacao': situacao}
print('-=' * 40)
sleep(1)
print(f'- nome e igual a {nome}')
sleep(1)
print(f'- media e igual a {media}')
sleep(1)
print(f'- situacao e igual a {situacao}')
sleep(1)
print('-=' * 10, '< FIM DO PROGRAMA >', '-=' * 10)
