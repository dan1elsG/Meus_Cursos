from math import trunc

print('=++=-' * 12, '\n{:^60}'.format('QUEBRANDO NUMERO'), '\n', '-=++=' * 12)

# pedi pro usuario escolher 2 opcoes.
usuario = int(input('Para ver Minha Resposta digite [ 1 ]\n'
                    'Para ver a Resposta do Curso em Video digite [ 2 ]\n'
                    'Sua opcao: '))

if usuario == 1:  # Caso digite 1 usuario vera minha resposta.
    print('''numero = float(input('Digite um numero real: '))
print('O numero digitado e {} e sua porcao inteira e {:.0f}'.format(numero, numero))\n''', '-=' * 40)
    numero = float(input('Digite um numero real: '))
    print('O numero digitado e {} e sua porcao inteira e {:.0f}!'.format(numero, numero))
elif usuario == 2:  # Caso digite 2 usuario vera a resposta do Curso em Video.
    print('''from math import trunc # filtra da biblioteca math a fucao trunc

numero = float(input('Digite um numero real: ')) # pedi pro usuario digitar um numero

print('O numero digitado e {} e sua porcao inteira e {}'.format(numero, trunc(numero)))
# Imprimi o resultado pro usuario.\n''', '-=' * 40)
    numero = float(input('Digite um numero real: '))
    print('O numero digitado e {} e sua porcao inteira e {}'.format(numero, trunc(numero)))
else:  # Se o Usuario digitar outra coisa o programa ira manda tentar novamente
    print('Tente Novamente')
