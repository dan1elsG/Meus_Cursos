lista = []
cont1 = 0
cont2 = 0
n = str(input('Digite uma expressao numerica: '))
for c in n:
    if c == '(':
        lista.append(c)
        cont2 += 1
for c in n:
    if c == ')':
        lista.append(c)
        cont1 += 1
if cont1 == cont2:
    print('Expressao numerica valida')
elif cont1 != cont2:
    print('Expressao invalida')
