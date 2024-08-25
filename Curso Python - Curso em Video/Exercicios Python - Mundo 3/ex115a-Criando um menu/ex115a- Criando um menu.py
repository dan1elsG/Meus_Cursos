from lib.interface import *
from time import sleep

while True:
    res = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR PESSOAS', 'SAIR DO PROGRAMA'])
    if res == 1:
        sleep(1)
        cabecalho('VER PESSOAS CADASTRADAS')
    elif res == 2:
        sleep(1)
        cabecalho('CADASTRAR PESSOAS')
    elif res == 3:
        sair('SAINDO DO PROGRAMA')
        break
    else:
        print('\033[31mERRO! DIGITE UMA OPCAO VALIDA!')

