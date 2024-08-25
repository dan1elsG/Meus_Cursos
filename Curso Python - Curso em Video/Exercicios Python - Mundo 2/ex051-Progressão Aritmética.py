n = int(input('primeiro termo: '))
r = int(input('razao: '))
a = n + (11 - 1)*r
for c in range(n, a, r):
    print('{} ➡'.format(c), end='')

print('Acabou')





