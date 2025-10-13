from abc import ABC, abstractmethod
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        ...
    @abstractmethod
    def buscar(self, id):
        return str()
    
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f'Salvando objeto : {objeto}')
    #Caso eu não implementasse o método "buscar", a classe não poderia ser instanceada
    def  buscar(self, id):
        return f'Objeto com id: {id}'
    

rm = RepositorioMemoria()

rm.salvar('Água')
print(rm.buscar(12))