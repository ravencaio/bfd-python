class Pessoa:
    def __init__(self, __cpf, __rg, data_nasc, nome):
        self.__cpf = __cpf
        self.__rg = __rg
        self.data_nasc = data_nasc
        self.nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf
    
    def set_rg(self, rg):
        self.__rg = rg

    def get_rg(self):
        return self.__rg
    
p1 = Pessoa('755.323.653-23', '12.324.544', '12/07/1996', 'Ary Mendonça')

print(p1.get_cpf())
p1.set_cpf('233.683.215-35')
print(p1.get_cpf())

print(p1.get_rg())
p1.set_rg('65.431.655')
print(p1.get_rg())
