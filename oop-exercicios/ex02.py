class Pessoa:
    def __init__(self, nome : str, idade : int):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return f'Olá meu nome é {self.nome} e tenho {self.idade} anos'

p1 = Pessoa('João', 25)

print(p1.apresentar())