n = s = 0
while True:
    n = int(input('Digite um numero: (999 para parar): '))
    if n == 999:
        break
    s = s + n
print(f"A soma vale {s}.")
