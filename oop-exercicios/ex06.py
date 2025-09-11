class ContaBancaria:
    def __init__(self, titular : str = '', saldo : float = 0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor : float) -> bool:
        self.saldo += valor
        return True

    def sacar(self, valor : float) -> bool:
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

p1 = ContaBancaria('Eduardo Mendes')
if p1.sacar(1200):
    print('A sua conta tem pelo menos 1200 reais')
else:
    print('A sua conta não tem saldo suficiente')