num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    res = num1 * num2
except:
    print('Algo deu errado')
else:
    print(res)