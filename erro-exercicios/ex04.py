try:
    arquivo = open('./dados.txt', 'r')
except FileNotFoundError:
    print('O arquivo não foi encontrado')
else:
    print('O arquivo foi encontrado')
finally:
    print('Encerrando programa')
