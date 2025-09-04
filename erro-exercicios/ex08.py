num1 = input('Digite seu número: ')
try:
    num1 = int(num1)
except:
    print('Digite um número válido')
else:
    if num1 % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
finally:
    print('Encerrando programa')