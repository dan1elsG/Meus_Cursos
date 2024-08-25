num = int(input('Digite um numero Para calcular o fatorial: '))
while num >= 25:
    print('O programa nao suporta {} vezes!\nTente novamente.'.format(num), end=' ')
    num = int(input('Digite um numero Para calcular o fatorial: '))
c = num + 1
f = 1
print('O fatorial de {} é {}! ='.format(num, num), end=' ')
while c > 1:
    c = c - 1
    f *= c
    if c == 1:
        print(' {}'.format(c), end='')
    else:
        print(' {} x'.format(c), end='')
print(' ➡ {}'.format(f))
