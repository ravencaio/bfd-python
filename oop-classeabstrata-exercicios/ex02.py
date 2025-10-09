from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def falar(self):
        ...

a1 = Animal('Oblorg', 12)

# O erro é dado pois não se pode criar classes abstratas diretamente.