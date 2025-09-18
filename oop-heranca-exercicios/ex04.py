class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def exibir_informações(self):
        print(f'{self.nome} === {self.email}')
    def saudacao(self):
        print(f'Olá, usuário {self.nome}!')


class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

c1 = Cliente('Caio', 'ravencaiobr@gmail.com', 0)
print(c1.saldo)
