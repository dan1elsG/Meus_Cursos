def escreva(txt):
    tam = len(txt)
    print('~' * tam)
    print(txt)
    print('~' * tam)


while True:
    escreva(input('Digite um texto: '))
    while True:
        res = input('Deseja continuar? [S/N] ').strip().upper()
        if res in 'NS':
            break
        if res == 'N':
            break
