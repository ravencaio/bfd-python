from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover():
        ...
    @abstractmethod
    def parar():
        ...

'''
class Carro(Transporte):
    def mover():
        print('Vruuuuum')

c1 = Carro()    Da erro, pois é necessário implementar todos os métodos abstratos pra criar uma classe que herda uma classe abstrata
'''
class Carro(Transporte):
    def mover():
        print('Vruuuuum')
    def parar():
        print('Freiando...')

c1 = Carro()
