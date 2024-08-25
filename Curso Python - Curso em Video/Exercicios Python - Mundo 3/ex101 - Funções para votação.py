def voto(ano):
    from datetime import date
    anovoto = date.today().year - ano
    if ano > date.today().year:
        return 'Esse ano ainda nao chegou!'
    else:
        if 0 < anovoto <= 14:
            return f'com {anovoto} anos: NAO VOTA'
        elif 15 < anovoto <= 17 or anovoto > 65:
            return f'com {anovoto} anos: VOTO OPCIONAL'
        elif 18 < anovoto <= 65:
            return f'com {anovoto} anos: VOTO OBRIGATORIO'


idade = int(input('digite a data de nascimento: '))
print(voto(idade))
