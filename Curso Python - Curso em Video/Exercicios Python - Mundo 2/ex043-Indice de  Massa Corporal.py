from time import sleep

# Sobre o programa
print('\033[34m-=' * 40, '\n{:^80}'.format('PROGRAMA QUERO SABER SE TOU GORDO'), '\n', '-=' * 40)
sleep(1)
print(' \033[mEsse programa foi criado para descobrir se voce esta acima do ceu peso ideal pois\n estamos enfrentando'
      'muitas mortes por obesidada morbida em nossa cidades.\n', '-=' * 40)
sleep(0.9)
print('''                       TABELA DO INDICE DE MASSA CORPORAL
 – IMC abaixo de 18,5: Abaixo do Peso

 – Entre 18,5 e 25: Peso Ideal

 – 25 até 30: Sobrepeso

 – 30 até 40: Obesidade

 – Acima de 40: Obesidade Mórbida\n''', '-=' * 40)

# Calcula o IMC
peso = float(input(' Digite seu peso em Kg:'))
altura = float(input(' Qual sua Altura em metros: '))
imc = peso / (altura ** 2)
sleep(1)
print(' Peso {:.2f}KG\n Altura {:.2f}M\n IMC {:.1f}\nCom estes Dados Voce esta '.format(peso, altura,
                                                                                        imc), end='')
# Verifica se o usuario esta acima ou abaixo do peso.
if imc < 18.5:
    print('Abaixo do peso, alimente-se melhor.')
elif 18.5 <= imc <= 25:
    print('Com Peso Ideal.')
elif 25 <= imc <= 30:
    print('Com Sobrepeso, Cuide-se mais')
elif 30 <= imc <= 40:
    print('Com Obesidade, procure um medico.')
elif imc > 40:
    print('Com Obesidade Morbida, procure um medico imediatemente.')
