from time import sleep

print("Validacao de  sexo\n ABRINDO PROGRAMA...")
sleep(3)
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
print('Verificando sexo...')
sleep(0.5)
while sexo not in "MF":
    if sexo not in "MF":
        sexo = str(input('Sexo invalido. Digite novamente:')).strip().upper()
    print('Verificando Sexo.....')
    sleep(0.5)
if sexo in "MF":
    if sexo == 'F':
        print('Sexo feminino.')
    if sexo == 'M':
        print('Sexo masculino.')
print("Fim do programa")
