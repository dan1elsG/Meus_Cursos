from time import sleep


def descobri_o_maior(valor):
    print('analisando os valores passados...')
    sleep(1)
    for v in valor:
        print(v, end=' ')
        sleep(0.5)
    print(f'O maior valor digitado foi {max(valor)}')


valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
descobri_o_maior(valores)
