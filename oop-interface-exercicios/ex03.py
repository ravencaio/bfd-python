from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        ...

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        ...

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print('Imprimindo relatório')
        return None
    
    def exportar(self):
        print('Exportando relatório')
        return None
    
r1 = Relatorio()

r1.imprimir()
r1.exportar()