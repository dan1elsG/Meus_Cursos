print('Gerador de PA')
print('-=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
contador = 1
termo = p
contador1 = 1
total = 1
contador2 = 0
contador3 = 0
while contador <= 10:
        termo = termo + r
        contador = contador + 1
        print('{} -> '.format(termo), end='')
        if contador >= 10 + 1:
            print('PAUSA')
            p = termo
contador -= 1
while not total == 0:
    contador1 = 1
    contador3 += contador2
    total = int(input("Quanto numero mais vc deseja digitar:"))
    for c in range(1, total):
        contador2 = c + 1
    while contador1 <= total:
        termo = termo + r
        contador1 += 1
        if total > 0:
            print('{} -> '.format(termo), end='')
    print('Progrecao finalizada com {} termos mostrados'.format( contador + contador3) if total == 0 else 'PAUSA')



