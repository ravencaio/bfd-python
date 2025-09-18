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

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, nivel_acesso):
        super().__init__(nome, email, cargo)
        self.nivel_acesso = nivel_acesso

c1 = Gerente('Caio', 'ravencaiobr@gmail.com', 'Gerente', 'Alto')

print(c1.nivel_acesso)
