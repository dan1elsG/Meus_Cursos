matriz = [[], [], []]
c = 0
while True:
    for c1 in range(0, 3):
        num = int(input(f'Digite um valor para {[c, c1]}:'))
        matriz[c].append(num)
    c += 1
    if c == 3:
        break
print('', matriz[0], '\n', matriz[1], '\n', matriz[2], '\n', end='')
