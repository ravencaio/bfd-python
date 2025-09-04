num1 = input('Digite um número inteiro: ')
try:
    num1 = int(num1)
except:
    print('Algo deu errado')
else:
    print('Conversão bem sucedida')