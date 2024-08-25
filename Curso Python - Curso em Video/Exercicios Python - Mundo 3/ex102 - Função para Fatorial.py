def fatorial(n=1, show=True):
    """
     ==> Calcula o fatorial de um numero
     fatorial(n=1, show='sim')
    :param n: O numero a ser calculado
    :param show: Mostrar ou nao a conta  do fatorial
    :return: retorna o valor do fatorial do numero n
    feito por @Dan1el._dev :)
    """
    from time import sleep
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} ', end='')
            sleep(0.5)
            if c == 1:
                print(f'==> ', end='\n')
                sleep(0.5)
            else:
                print(f'x ', end='')
                sleep(0.5)
        f *= c
    return f'O fatorial de {n}! = {f}'


num = int(input('Digite um numero Para calcular o fatorial: '))
while True:
    ver = str(input('Deseja ver o calculo? S/N')).strip().upper()[0]
    if ver in 'SN':
        break
if ver == 'N':
    ver = False
elif ver == 'S':
    ver = True
print(fatorial(num, ver))
help(fatorial)
