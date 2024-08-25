lista = []
c = 0
valor = int(input('Quantos Valores deseja digitar na sua lista: '))
while True:
    if valor > 10:
        print('Valido apenas 10 numeros por vez.')
        valor = int(input('Quantos Valores deseja digitar na sua lista: '))
    else:
        break
while True:
    n = int(input('Digite um valor:'))
    c += 1
    if c == 1:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        if n not in lista:
            if n > lista[-1]:
                tamanho = len(lista)
                lista.insert(tamanho + 1, n)
                print('Valor adicionado com sucesso...Ao final da lista')
            elif n < lista[0]:
                lista.insert(0, n)
                print('Valor adicionado com sucesso...Ao inicio da lista')
            else:
                for i in range(0, len(lista)):
                    if n > lista[i]:
                        if n < lista[i + 1]:
                            lista.insert(i + 1, n)
                            print(f'Valor adicionado com sucesso...Na posicao {i + 1} da lista ')
        elif n in lista:
            print('Valor Duplicado....Nao irei adicionar')
            c -= 1
    if c == valor:
        break
print(f'Voce digitou os valores {lista}')
