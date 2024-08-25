
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area do terreno {largura}x{comprimento} e de {area}')


print('Controle de terrenos')
print('-=' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
