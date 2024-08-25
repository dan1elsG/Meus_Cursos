frase = str(input('Digite uma frase: ')).upper().strip()
letra = ''
for letra in range(len(frase)-1, -1, -1):
    print(frase[letra], end='')


if frase[letra] == frase[letra - 1]:
    print('\né um palidromo.')
else:
    print('\nnão é um palidromo.')
