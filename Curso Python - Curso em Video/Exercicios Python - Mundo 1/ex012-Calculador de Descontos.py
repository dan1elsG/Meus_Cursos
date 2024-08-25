from time import sleep

print('\033[34m>-+>' * 16, '\n{:^60}'.format('CALCULADOR DE DESCONTOS'), '\n', '>-+>' * 16)
sleep(1)  # Faz o programa "Dormir" Por alguns segundo.
print('\033[32mPara calcular seu desconto Insira o nome do produtoe seu valor,\n logo em seguida voce tera sua'
      ' porcentagem de desconto.')   # explicacao de como o programa funciona.
print('\033[m>-<-' * 16)  # Firula pra deixar o programa mais intuitivo.
sleep(0.4)
produto = str(input('\033[mQual o nome do Produto que voce deseja comprar: ')).title().strip()  # pergunta e formata a
# resposta do usuario deixando o primeira letra maiuscula e remove os espacos indesejado.
sleep(0.25)
preco = float(input('qual o valor do produto que voce deseja comprar? '))  # pergunta o valor do produto e coloca
# na variavel preco
sleep(0.30)
desconto = preco - (preco * (5/100))  # Calcula o desconto que op usuario tera emcima do produto que deseja comprar.
print('Produto: {}\nValor {:0.2f}\nVoce Ganhou 5% de desconto entao o novo valor sera {:0.2f}'.format(produto, preco,
                                                                                            desconto))  # Imprime na
# tela Qual produto o usuario quer o valor do  mesmo e a procentagem de desconto.
