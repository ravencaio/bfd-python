from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        ...

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        ...

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print('Ligando computador...')
    def desligar(self):
        print('Desligando computador...')

c1 = Computador()
c1.ligar()
c1.desligar()