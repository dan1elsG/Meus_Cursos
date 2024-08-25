def leiaDinheiro(msg):
    while True:
        dinheiro = str(input(msg)).replace(',', '.').strip()
        if dinheiro.replace('.', '').isnumeric():
            return float(dinheiro)
        else:
            print(f'\033[31mERROR! {dinheiro} NAO E VALOR MONETARIO VALIDO!\033[m')
