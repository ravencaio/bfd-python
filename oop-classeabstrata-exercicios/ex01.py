from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def falar(self):
        ...
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        print('Au au!')

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        print('Miau..')
    
c1 = Cachorro('Rex', 4)
g1 = Gato('Nuvem', 5)

c1.falar()
g1.falar()
