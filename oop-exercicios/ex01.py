class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

p1 = Pessoa('Caio', 19)
p2 = Pessoa('Fred', 36)

print(f'{p1}\n{p2}')