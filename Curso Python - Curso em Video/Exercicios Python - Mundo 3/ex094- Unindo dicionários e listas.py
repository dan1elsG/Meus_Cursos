
pessoas = []
soma = 0
while True:
    cadastro = {'nome': str(input('Nome: ')), 'idade': int(input('Idade: ')),
                'sexo': str(input('Sexo [M/F]: ')).strip().upper()[0]}
    while cadastro['sexo'] not in 'MF':
        print('ERRO! Digite apenas M ou F')
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('ERRO! Digite apenas S ou N')
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    pessoas.append(cadastro.copy())
    cadastro.clear()
    if res == 'N':
        break
if len(pessoas) == 1:
    print(f'A) Somente uma pessoa cadastrada')
else:
    print(f'A) foram cadastradas {len(pessoas)} pessoas')
for i, v in enumerate(pessoas):
    if i == 0:
        soma = v["idade"]
    else:
        soma += v["idade"]
media = soma / len(pessoas)
print(f'B) A media de Idade e {media:.2f} anos.')
print(f'C) As   Mulheres cadastradas foram:')
for i, v in enumerate(pessoas):
    if v['sexo'] == 'F':
        print(f'    =>     A {v["nome"]}')
print('D) lista de pessoas acima da media:')
for i, v in enumerate(pessoas):
    if v['idade'] >= media:
        if v['sexo'] == 'F':
            print(f'    =>     A {v["nome"]} com {v["idade"]} anos.')
        if v['sexo'] == 'M':
            print(f'    =>     O {v["nome"]} com {v["idade"]} anos.')
print('<< VOLTE SEMPRE >>')
