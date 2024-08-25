mulher = homem = pessoas = 0
print('=====Cadastro de pessoas======')
while True:
    idade = int(input('Informe sua idade: '))
    if idade > 18:
        pessoas += 1
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    print('-=' * 40)
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    contiuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    print('-=' * 40)
    while contiuar not in 'SN':
        contiuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        print('-=' * 40)
    if contiuar == 'N':
        break
print(f'Total de pessoas com mais de 18 cadastradas: {pessoas}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {mulher}')
