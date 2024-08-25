print('Gerador de PA')
print('-=' * 20)
primeiro_termo = int(input('Digite o primeiro termo: '))
while primeiro_termo >= 100:
    print('Numero muito grande  para calcular digite um numero menor que 100')
    primeiro_termo = int(input("digite o primeiro termo: "))
razao = int(input("Digite a razão:"))
while razao >= 100:
    print('Numeros muito grande para calcular digite um numero menor que 100.')
    razao = int(input("digite a razão: "))
termo = primeiro_termo
contador = 1
while contador <= 10:
    termo = termo + razao
    contador = contador + 1
    print("{} ->".format(termo), end='')
print("FIM")