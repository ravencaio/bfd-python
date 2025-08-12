num1 = int(input('Dirigite o primeiro número: '))
num2 = int(input('Dirigite o segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 == num2:
    print(f'{num1} = {num2}')
else:
    print(f'{num2} é maior que {num1}')