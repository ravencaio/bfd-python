from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        ...

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f'Processando R${valor} no crédito')

class Boleto(Pagamento):
    def processar(self, valor):
        print(f'Processando R${valor} no boleto')


c1 = CartaoCredito()
b1 = Boleto()

c1.processar(12)
b1.processar(235.4)