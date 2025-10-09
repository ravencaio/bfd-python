from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar():
        ...

class Desligavel(ABC):
    @abstractmethod
    def desligar():
        ...

class Computador(Ligavel, Desligavel):
    def ligar():
        print('Ligando computador...')
    def desligar():
        print('Desligando computador...')

c1 = Computador
c1.ligar()
c1.desligar()