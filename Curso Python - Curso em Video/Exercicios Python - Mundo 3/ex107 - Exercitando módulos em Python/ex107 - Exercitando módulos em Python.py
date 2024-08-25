import moedas

p = int(input('Digite um valor: '))
print(f'O dobro do R${p} vale R${moedas.dobro_(p)}')
print(f'aumentando 10%, R${moedas.aumentar_(p)}')
print(f'A metade de R${p} vale R${moedas.metade_(p)}')
