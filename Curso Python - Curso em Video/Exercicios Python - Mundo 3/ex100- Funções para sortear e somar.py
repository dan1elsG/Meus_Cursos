from time import sleep
from random import randint


def carregando():
    print('processando', end='')
    c = 0
    while c <= 3:
        c += 1
        print('.', end='')
        sleep(0.5)
    print()


def sortei(valores):
    for c in range(0, 6):
        valores.append(randint(1, 10))


def soma_valores(valores):
    c = 0
    par = []
    for valor in valores:
        if valor % 2 == 0:
            par.append(valor)
    for i in par:
        print(f'{i}', end=' ')
        while True:
            c += 1
            if c == len(par):
                break
            print('+', end=' ')
            sleep(0.5)
            break
        sleep(0.5)
    print(f'= {sum(par)}')


lista = list()
sortei(lista)
print(f'Os valores sorteados foram', end='')
for i in lista:
    print(f' => {i}', end='')
    sleep(0.5)
print('.')
carregando()
soma_valores(lista)
