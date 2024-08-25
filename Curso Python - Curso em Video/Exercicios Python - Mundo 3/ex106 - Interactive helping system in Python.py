def escreva(txt):
    tam = len(txt)
    print('\033[42m-' * tam)
    print(txt)
    print('-' * tam, )
    print('\033[m')


def carregando():
    from time import sleep
    print('\033[47mCarregando', end='')
    c = 0
    while c <= 3:
        c += 1
        print('.', end='')
        sleep(0.5)
    print('\033[m')


def pyhelp(f):
    carregando()
    print('\033[43m')
    help(f)
    print('-'*40)


escreva('SYSTEMA HELP')
while True:
    f = str(input(f'\033[mDigite uma funcao ou biblioteca>> (FIM) PARA FINALIZAR'))
    if f.upper() == 'FIM':
        break
    pyhelp(f)
