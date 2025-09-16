class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Funcionario(Pessoa):
    def __init__(self, nome, idade, sexo, emprego, senioridade):
        super().__init__(self, nome, idade, sexo)
        self.emprego = emprego
        self.senioridade = senioridade


func1 = Funcionario('Luiz', 27, 'M', 'Gestor de Projetos', 'Senior')
pes1 = Pessoa('Caio', 19, 'M')


