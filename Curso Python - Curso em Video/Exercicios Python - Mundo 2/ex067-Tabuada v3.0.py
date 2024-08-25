from time import sleep
print('Abrindo Tabuada v3.0')
sleep(3)
while True:
    n = int(input('Digite um numero: -1 para finalizar'))
    if n < 0:
        break
    print('Calculando...')
    sleep(3)
    print('Tabuada do numero {}\n'.format(n), '-=' * 40)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-=' * 40)
print('FIM DO PROGRAMA')