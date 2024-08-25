

def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(num):
    while True:
        try:
            numero = int(input(num))
            return numero
        except (TypeError, ValueError):
            print('\033[31mERROR! digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nUsuario preferiu nao digitar esse numero.\033[m')
            return


def carregar(txt, txt1=''):
    from time import sleep
    print(f'\033[31m{txt}', end='')
    c = 0
    while c <= 3:
        c += 1
        print('.', end='')
        sleep(0.5)
    print(f'\n{txt1}')


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for num, item in enumerate(lista):
        print(f'\033[32m{num+1} - \033[34m{item}\033[m')
    print(linha())
    return leiaint('\033[34mSUA OPCAO:\033[m')



