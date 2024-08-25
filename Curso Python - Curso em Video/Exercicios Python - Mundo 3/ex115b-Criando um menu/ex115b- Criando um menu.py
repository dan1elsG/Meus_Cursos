from lib.interface import *
from time import sleep


verificar_se_aquivo_txt_existe('Cadastro_pessoas.txt')
while True:
    res = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSOAS', 'SAIR DO PROGRAMA'])
    if res == 1:
        sleep(1)
        cabecalho('PESSOAS CADASTRADAS')
        ler_arquivo('Cadastro_pessoas.txt')
    elif res == 2:
        sleep(1)
        cabecalho('CADASTRAR PESSOAS')
        cadastrar_pessoa('Cadastro_pessoas.txt')
    elif res == 3:
        carregar('SAINDO DO PROGRAMA')
        break
    else:
        print('\033[31mERRO! DIGITE UMA OPCAO VALIDA!')

