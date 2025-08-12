idad = int(input('Digite a idade da pessoa: '))

if idad <= 12:
    print('Criança')
elif 12 < idad <= 17:
    print('Adolescente')
elif 17 < idad <= 64:
    print('Adulto')
else:
    print('Idoso')