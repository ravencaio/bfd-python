class Aluno:
    def __init__(self, nome : str, nota : float):
        self.nome = nome
        self.nota = nota
        

class Turma:
    def __init__(self, lista_alunos : list = []):
        self.lista_alunos = lista_alunos

    def adicionar_aluno(self, aluno : Aluno):
        self.lista_alunos.append([aluno.nome, aluno.nota])

a1 = Aluno('Caio', 8.3)
t1 = Turma()

t1.adicionar_aluno(a1)
print(t1.lista_alunos)
        