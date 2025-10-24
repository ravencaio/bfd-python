class Livro():
    def __init__(self, nome : str) -> None:
        self.nome = nome

class Aluno():
    def __init__(self, nome : str, idade : int) -> None:
        self.nome = nome
        self.idade = idade

    def pegar_livro(self, livro : Livro) -> None:
        print(f'O aluno {self.nome} pegou o livro {livro.nome}')


al = Aluno('Caio', 19)
l1 = Livro('Fahrenheit 451') 

al.pegar_livro(l1)