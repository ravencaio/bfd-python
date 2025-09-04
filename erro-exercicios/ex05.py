def divisão(a : int, b : int) -> int:
    return a / b

num1 = float(input('Digite o numerador: '))
num2 = float(input('Digite o denominador: '))

if num2 == 0:
    raise ZeroDivisionError('Denominador não pode ser igual a 0')

print(divisão(num1, num2))