
valor = int(input('Quantos Reais deseja sacar: R$ '))
while valor > 5000:
    print('Error Caixa nao saca mais que 5000.')
    valor = int(input('digite novamente o valor: R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'{totalcedula} Cedula de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break