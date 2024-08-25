from time import sleep
print('Abrindo Tabuada v2.0')
sleep(3)
n = int(input('Digite um numero: '))
print('Calculando...')
sleep(3)
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
