class Autenticacao:
    def login(self):
        return 'Login feito'
    def status(self):
        return 'Status Autenticação'

class Permissao:
    def verificar_permissao(self):
        return 'Permissão verificada'
    def status(self):
        return 'Status Permissão'
class Administrador(Autenticacao, Permissao):
    ...

a1 = Administrador()
print(a1.login())
print(a1.status())
print(Administrador.__mro__)