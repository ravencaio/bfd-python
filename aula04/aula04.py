fibonacci = [0,1]
quant = int(input('Quantos digitos de fibonacci você quer ver: '))
match quant:
    case 0:
        exit
    case 1:
        print(0)
    case _:
        for c in range(quant-2):
            novo = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(novo)
        for num in fibonacci:
            if num == fibonacci[-1]:
                print(num)
                break
            print(f'{num}, ', end='')