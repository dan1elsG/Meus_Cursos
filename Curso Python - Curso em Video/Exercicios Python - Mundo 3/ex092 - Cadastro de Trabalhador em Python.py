from datetime import date
from time import sleep
nome = str(input('Digite seu nome: ')).capitalize()
ano = int(input('Digite ano de nasciomento (YYYY): '))
idade = date.today().year - ano
carteira = int(input('Digite o numero da sua carteira: (0 Nao tem)'))
if carteira == 0:
    carteira = '0, USUARIO NAO POSUI CARTEIRA DE TRABALHO'
    cadastro = {'Nome': nome, 'idade': idade, 'carteira': carteira}
    for k, v in cadastro.items():
        print(f'- {k} tem o valor {v}')
        sleep(1)
else:
    cadastro = {'Nome': nome, 'idade': idade}
    ano_contrato = int(input('Digite o ano do contrato: '))
    salario = str(input('Digite seu salario: R$ '))
    aposentadoria = (ano_contrato + 35) - ano
    cadastro['salario'] = salario
    cadastro['aposentadoria'] = aposentadoria
    for k, v in cadastro.items():
        print(f'- {k} tem o valor {v}')




