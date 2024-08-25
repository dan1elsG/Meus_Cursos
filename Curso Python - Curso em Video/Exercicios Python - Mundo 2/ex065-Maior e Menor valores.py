numeros = int(input('Digite um numero: '))
continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
cont = 1
soma = numeros
menor = numeros
maior = numeros
while continuar == "S":
    if numeros > maior:
        maior = numeros
    numeros = int(input('Digite um numero: '))
    cont += 1
    soma += numeros
    if numeros > maior:
        maior = numeros
    if numeros <= menor:
        menor = numeros
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Voce digitou {} numeros, o maior valor foi {} eo menor {}'.format(cont, maior, menor))
print('A media entre os valores digitados foi {:0.2f}'.format(media))
