from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area():
        ...
    @abstractmethod
    def perimetro():
        ...

class Retangulo(FormaGeometrica):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimetro(self):
        return self.x * 2 + self.y * 2

r1 = Retangulo(int(input('Digite a largura do retângulo: ')), int(input('Digite a altura do retângulo: ')))

print(f'Área: {r1.area()}m²; Perímetro: {r1.perimetro()}')