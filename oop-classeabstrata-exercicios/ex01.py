from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def falar(self):
        return f'Olá, sou {self.nome}'
    
    @abstractmethod
    def andar(self, metros:int):
        return f'{self.nome} andou {metros}M'
    
    @abstractmethod
    def comer(self, comida:str):
        return f'{self.nome} comeu {comida}'

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    
    def falar(self):
        return f'Olá, sou {self.nome}, e meu cargo é {self.cargo}'
    
    def andar(self, metros):
        return super().andar(metros)

    def comer(self, comida):
        return super().comer(comida)

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso:str):
        super().__init__(nome, idade)
        self.curso = curso
    def falar(self):
        return f'Olá, sou {self.nome}, e estou cursando {self.curso}'
    
    def andar(self, metros):
        return super().andar(metros)
    
    def comer(self, comida):
        return super().comer(comida)

f1 = Funcionario('Fred', 36, 'Professor')
a1 = Aluno('Caio', 19, 'Eng. Computação')