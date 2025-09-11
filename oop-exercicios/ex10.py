class ContaBancaria:
    def __init__(self, titular : str = '', __saldo : float = 0):
        self.titular = titular
        self.__saldo = __saldo
    def depositar(self, valor : float) -> bool:
        self.__saldo += valor
        return True

    def sacar(self, valor : float) -> bool:
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def set_saldo(self, valor):
        if valor < 0:
            print('Saldo não pode ser negativo')
        else:
            self.__saldo = valor
    
    def get_saldo(self):
        return self.__saldo
    
p1 = ContaBancaria('Arnaldo Souza', 344.12)
print(p1.get_saldo())
p1.set_saldo(12.76)
print(p1.get_saldo())
p1.set_saldo(-23.5)