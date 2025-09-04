num = input('Digite um número inteiro: ')

try:
    int(num)
except ValueError:
    print('Digite um número inteiro!!!!')
else:
    print('Número inteiro digitado')