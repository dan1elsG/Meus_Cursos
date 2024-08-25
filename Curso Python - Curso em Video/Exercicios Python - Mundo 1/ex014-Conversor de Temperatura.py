from time import sleep

print('-**-' * 25, '\n{:^100}'.format('CONVERSOR DE TEMPERATURAS'), '\n', '-**-' * 25)
print('''Em uma cidade onde as temperaturas eram sempre medidas em graus Fahrenheit,
turistas estrangeiros se viam perdidos diante do clima local. Um morador engenhoso 
criou um aplicativo simples, o "Conversor de Temperaturas Mágico", que rapidamente
se tornou uma solução prática. Agora, com apenas alguns Cliques, todos podiam entender 
e apreciar melhor o clima peculiar da cidade.''', '\n', '-**-' * 25)
sleep(2)
f = float(input('Bem-vindo à nossa cidade! Digite a temperatura graus Fahrenheit: '))  # Pedi pro usuario digitar a
# temperatura em graus Fahrenheit.
print('-**-' * 25, '\nCONVERTENDO...\n', '-**-' * 25)
c = ((f - 32) * 5) / 9  # Faz a conversao de graus para celsius.
sleep(2)
print('A temperatura atual é {:.0f}°C, aproveite o clima!'.format(c))  # exibe a temperatura.
