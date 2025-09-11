class Cachorro:
    especie = 'Canis lupus familiaris'
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

c1 = Cachorro('Albert', 3)

print(c1.nome, c1.idade, c1.especie)

Cachorro.especie = 'Canis familiaris'

print(c1.especie)