def leiaInt(num):
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


def leiaFloat(num):
    while True:
        try:
            numero = float(input(num))
            return numero
        except (ValueError, TypeError):
            print('\033[31mERROR! digite um numero Real valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nUsuario preferiu nao digitar esse numero.\033[m')
            numero = 0.0
            return numero


n = leiaInt('DIGITE UM NUMERO INTEIRO: ')
n1 = leiaFloat('DIGITE UM NUMERO REAL: ')
print(f'\033[32mO valor inteiro foi {n}, e o real  foi {n1}\033[m')
