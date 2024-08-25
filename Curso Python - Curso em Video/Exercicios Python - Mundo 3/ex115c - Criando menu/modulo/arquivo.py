from .interface import *

txt = 'CADASTRO.txt'


def verificar_se_aquivo_txt_existe(nome):
    try:
        a = open(f'{nome}', 'r')
        a.close()
    except FileNotFoundError:
        with open(f'{nome}', 'w') as file:
            file.write('')
        return carregar(f'CRIANDO ARQUIVO {nome}', f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def ler_arquivo(nome):
    try:
        with open(f'{nome}', 'r') as file:
            linhas = file.readlines()
            for linhaw in linhas:
                n, i = linhaw.strip().split(',')
    except FileNotFoundError:
        verificar_se_aquivo_txt_existe(nome)
    except ValueError:
        print(f'TIVEMOS UM PROBEMA AO TENTAR LER O ARQUIVO {nome}')
    else:
        with open(f'{nome}', 'r') as file:
            linhas = file.readlines()
            for linhaw in linhas:
                n, i = linhaw.strip().split(',')
                print(f'{n:<20}\t{i:>12} anos')

def cadastrar_pessoa(nome):
    n = str(input('Nome: ')).capitalize()
    i = leiaint('Idade: ')
    try:
        with open(f'{nome}', 'a') as file:
            file.write(f'{n}, {i}\n')
            print(f'{n} foi cadastrada com sucesso!')
    except FileNotFoundError:
        verificar_se_aquivo_txt_existe(nome)
