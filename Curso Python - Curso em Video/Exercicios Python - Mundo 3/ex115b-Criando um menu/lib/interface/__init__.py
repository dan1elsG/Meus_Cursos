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
    cabecalho('Menu Principal')
    for num, item in enumerate(lista):
        print(f'\033[32m{num+1} - \033[34m{item}\033[m')
    print(linha())
    return leiaint('\033[34mSUA OPCAO:\033[m')


def verificar_se_aquivo_txt_existe(txt):
    try:
        with open(f'{txt}', 'r') as file:
            file.read()
    except FileNotFoundError:
        with open(f'{txt}', 'w') as file:
            file.write('')
        return carregar(f'CRIANDO ARQUIVO {txt}',  f'\033[32mArquivo {txt} criado com sucesso!\033[m')


def ler_arquivo(txt):
    with open(f'{verificar_se_aquivo_txt_existe(txt)}', 'r') as file:
        linhas = file.readlines()
        for linhaw in linhas:
            nome, idade = linhaw.strip().split(',')
            print(f'{nome} tem \t{idade} anos')


def cadastrar_pessoa(txt):
    nome = str(input('Nome: ')).capitalize()
    idade = leiaint('Idade: ')
    with open(f'{verificar_se_aquivo_txt_existe(txt)}', 'w') as file:
        file.write(f'{nome}, {idade}')
        print('Pessoa cadastrada com sucesso!')
