from time import sleep  # importa a fucao sleep da biblioteca time

print('\033[34m>>===>-' * 12, '\n{:^71}'.format('Exercicio 036'), '\n', '>>===>-' * 12)  # firula para deixar o programa
# mais bonito
print('\033[36mPROCESSADO.....\033[31m\n',  '>>===>❤' * 12)
sleep(2)  # Faz o programa "Dormir" por alguns segundos.
print('\033[mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\nPergunte o valor da '
      'casa,o salário do comprador e em quantos anos ele vai pagar.\nA prestação mensal não pode exceder 30% do '
      'salário ou então o empréstimo será negado.\033[31m\n', '>>===>❤' * 12)  # Enunciado da questao.
sleep(1)
valor_casa = float(input('\033[mQual o valor da Casa:'))  # Pedi para usuario digitar o valor da casa.
salario = float(input('Qual seu Salario: '))  # pedi para o usuario digitar o seu salario.
anos_pagamento = int(input('Quantos deseja realizar o pagamento: '))  # Pedi pro usuario digitar em quantos anos
# deseja pagar.
prestacao = valor_casa / (anos_pagamento * 12)  # Faz o calculo das prestacoes da casa.
minimo_pagar = salario * (30/100)  # Calcula o valor minimo que o usuario podera pagar.
print('\033[mpara pagar uma casa RS{:.2f} em {} anos a prestacao sera de RS{:.2f}'.format(valor_casa,
                                                                                          anos_pagamento, prestacao))
# Imprimi na tela os Valores digitado pelo usuario.
if prestacao <= minimo_pagar:
    print('\033[32mEmprestimo Aprovado.')
elif prestacao > minimo_pagar:
    print('\033[31mEmprestimo Negado.')   # Informa o Usuario se O imprestimo sera aprovado ou negado.
