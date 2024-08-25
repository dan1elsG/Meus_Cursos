from time import sleep


print('\033[32m-R$-' * 28, '\n{:^96}'.format('REAJUSTE SALARIAL.'), '\n',  '-R$-' * 28)
sleep(1)
print('''\033[mNuma reviravolta surpreendente, o governo anunciou um aumento salarial, trazendo alívio instantâneo 
aos trabalhadores. As ruas ganharam vida com sorrisos, e as famílias começaram a vislumbrar um futuro mais 
próspero.Para facilitar a compreensão do impacto, o governo lançou um programa  que permitia aos trabalhadores 
calcular rapidamente o quanto o salário deles aumentou, proporcionando transparência e celebrando essa conquista 
significativa.Com a implementação do programa, os trabalhadores puderam calcular instantaneamente o impacto
do aumento salarial de 15%. Uma mensagem apareceu nos resultados, informando com entusiasmo:\033[32m''')
print('-R$-' * 28)
sleep(3)
salario = float(input('\033[mDigite o valor do seu salario: R$ '))
novosalario = salario + (salario * (15/100))
sleep(0.3333)
print('-=' * 56, '\n\033[32mParabéns! Seu salário aumentou para R$\033[m {:.2f}\033[32m! Aproveite os benefícios desse'
                 ' progresso e continue construindo\n um futuro próspero!'.format(novosalario))
