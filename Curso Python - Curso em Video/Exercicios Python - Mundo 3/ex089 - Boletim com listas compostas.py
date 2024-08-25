from time import sleep
boletin = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista = [nome, nota1, nota2, media]
    boletin.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        print('-=' * 40)
        break
print(f'{"ID":<7}{"NOME":<10}{"MEDIA":<11}')
print('-=' * 17)
for i, n in enumerate(boletin):
    print(f'{i:<7}{n[0]:<10}{n[3]:<11.1f}')
print('-=' * 17)
while True:
    resps = int(input('Deseja Ver as notas de qual aluno? (999 interrompe): '))
    print('-=' * 17)
    sleep(1)
    for i, v in enumerate(boletin):
        if i == resps:
            print(f'Notas de {v[0]} foram {v[1]} e {v[2]}')
    if resps == 999:
        break
print('FINALIZANDO....')
sleep(1)
print()
print('< VOLTE SEMPRE! >')
sleep(1)
