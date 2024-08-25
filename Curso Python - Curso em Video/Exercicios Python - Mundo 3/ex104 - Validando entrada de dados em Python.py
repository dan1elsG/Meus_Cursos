def leiaInt(num):
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            return int(numero)
        else:
            print('\033[31mERROR! digite um numero inteiro valido.\033[m')


n = leiaInt('DIGITE UM NUMERO INTEIRO: ')
print(f'\033[32mO valor digitado foi {n}\033[m')
