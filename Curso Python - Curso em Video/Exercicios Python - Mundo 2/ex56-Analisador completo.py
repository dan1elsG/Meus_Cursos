
nome_masc = ""
idademaior= 0
contmuie = 0
somaidade  = 0

for c in range(1, 5):
    print("{:-^40}".format('Dados da {} pessoa'.format(c)))
    nome = str(input('Digite o nome da {} pessoa: '.format(c))).capitalize()
    idade = int(input('Digite a idade da {} pessoa: '.format(c)))
    sexo = str(input('Digite o sexo [M/F] da {} pessoa: '.format(c))).upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        contmuie += 1
    if sexo == 'M':
        if idade >= idademaior:
            idademaior = idade
            nome_masc = nome
        sexo_masc = sexo
print('Mulheres com menos de 20 anos: {}'.format(contmuie))
print('O homem mais velho se chama {} e sua e idade e {} '.format(nome_masc, idademaior))
print('a media de idades do grupo: {}'.format(somaidade/4))
