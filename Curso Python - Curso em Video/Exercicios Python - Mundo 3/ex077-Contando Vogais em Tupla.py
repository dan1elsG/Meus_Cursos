
lista = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Facimp')
contador = 0
while True:
    print(f'\nNa palavra {(lista[contador])} temos', end=' ')
    separador = list(lista[contador])
    for contarvogais in separador:
        if contarvogais in 'aeiou''AEIOU':
            print(contarvogais, end=' ')
    contador += 1
    if contador == len(lista):
        break
