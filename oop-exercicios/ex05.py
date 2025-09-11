class ContaBancaria:
    def __init__(self, titular : str = '', saldo : float = 0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor : float):
        self.saldo += valor

    def sacar(self, valor : float):
        if self.saldo < valor:
            return 'Saldo Insuficiente.'
        else:
            self.saldo -= valor

p1 = ContaBancaria('Claudio Braga')

p1.depositar(120)
print(p1.saldo)
print('#' * 20)
p1.sacar(14)
print(p1.saldo) 
print(p1.sacar(1233))

