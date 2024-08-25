from time import sleep


def contador(i, f, p):
    if p < 0:
        m = p * -1
        print(f'Contagem de {i} ate {f} de {m} em {m}')
    else:
        print(f'Contagem de {i} ate {f} de {p} em {p}')
    if f < 0:
        maior = i
        passo = p
        s = 0
        print(f'{i} ', end='')
        while True:
            s = maior - passo
            if f >= s:
                print('FIM !')
                break
            s = maior - passo
            print(f'{s} ', end='')
            maior = s
            sleep(0.3)
    elif i < 0:
        maior = i
        passo = p
        s = 0
        print(f'{i} ', end='')
        while True:
            s = maior + passo
            if s >= f:
                print('FIM !')
                break
            s = maior + passo
            print(f'{s} ', end='')
            maior = s
            sleep(0.3)
    else:
        for c in range(i, f, p):
            print(f'{c} ', end='')
            sleep(0.3)
        print('FIM !')


contador(1, 10, 1)
contador(10, 0, -2)
print('Contagem Personalizada!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
