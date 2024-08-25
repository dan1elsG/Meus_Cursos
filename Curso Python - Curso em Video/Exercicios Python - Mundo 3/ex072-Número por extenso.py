
lista_de_numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
                    'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um  numero entre 0  e 20: '))
    if 0 < numero > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'O numero digitado foi {lista_de_numeros[numero]}')
        continua = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        while continua not in 'SN':
            continua = str(input('Deseja continuar [S/N]: ')).strip().upper()
        if continua == 'N':
            break
print("Obrigado por usar o programa! Volte sempre!")
