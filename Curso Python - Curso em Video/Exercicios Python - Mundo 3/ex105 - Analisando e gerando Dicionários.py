def notas(*n, sit=False):
    """
    --> Funcao para analizar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando a situacao do aluno.
    :return: retorna um dicionario com as notas sobre a situacao do aluno.
    feito por @dan1el._dev
    """
    situacao = ''
    notas_alunos = n
    total = len(notas_alunos)
    maior = max(notas_alunos)
    menor = min(notas_alunos)
    media = sum(notas_alunos)/len(notas_alunos)
    if media > 8:
        situacao = 'MUITO BOA'
    elif 7 <= media <= 8:
        situacao = 'BOA'
    elif 5 <= media < 7:
        situacao = 'RAZOAVEL'
    elif media < 5:
        situacao = 'RUIM'
    if sit:
        notas_alunos = {'TOTAL': total, 'MAIOR': maior, 'MENOR': menor, 'MEDIA': media, 'SITUACAO': situacao}
        return print(notas_alunos)
    else:
        notas_alunos = {'TOTAL': total, 'MAIOR': maior, 'MENOR': menor, 'MEDIA': media}
        return print(notas_alunos)
notas(10, 10, 10, 8, 7)
