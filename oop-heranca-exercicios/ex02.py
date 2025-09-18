class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def exibir_informações(self):
        print(f'{self.nome} === {self.email}')


class Cliente(Usuario):
    def __str__(self):
        return f'NOME: {self.nome} | EMAIL: {self.email}'
    
c1 = Cliente('Caio', 'ravencaiobr@gmail.com')
c1.exibir_informações()
