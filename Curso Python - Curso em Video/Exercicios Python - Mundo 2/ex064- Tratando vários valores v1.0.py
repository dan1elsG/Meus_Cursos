numero = int(input('Digite um numero [999 para parar]: '))
soma = numero
cont = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    soma += numero
    cont += 1
    if numero == 999:
        soma -= 999
print('Voce digitou {} ea soma dos numeros inteiros e {}'.format(cont, soma))

