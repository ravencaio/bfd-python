num1 = input('Digite o numerador: ')
num2 = input('Digite o denominador: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    num1 / num2
except ValueError:
    print('Digite valores válidos')
except ZeroDivisionError:
    print('Não se pode dividir por 0')
else:
    print(num1 / num2)