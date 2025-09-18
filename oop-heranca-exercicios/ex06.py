class Autenticacao:
    def login(self):
        return 'Login feito'
    
class Permissao:
    def verificar_permissao(self):
        return 'Permissão verificada'
    
class Administrador(Autenticacao, Permissao):
    ...

a1 = Administrador()
print(a1.login())
print(a1.verificar_permissao())