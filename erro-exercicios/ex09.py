class SaldoInsuficienteError(Exception): ...

def sacar(saldo : int, valor : int):
    if saldo < saque:
        raise SaldoInsuficienteError
    return saldo - valor
saldo = input('Digite o saldo da conta: ')

saque = input(f'Digite o valor do saque(valor na conta = {saldo}): ')

try:
    saldo = float(saldo)
    saque = float(saque)
    sacar(saldo, saque)
except SaldoInsuficienteError:
    print('Saldo insuficiente')
except TypeError:
    print('Digite valores válidos')
else:
    print(f'Novo valor na conta: {sacar(saldo, saque)}')
finally:
    print('Encerrando programa')
