from time import sleep
print('\033[1;36m-=' * 40, '\n{:^80}'.format('CONTAGEM REGRESSIVA'), '\n', '-=' * 40)
for conte in range(10, -1, -1):
    print(conte)
    sleep(1)
print('BUM! BUM! POOW!')