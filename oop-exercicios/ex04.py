class Carro:
    def __init__(self, marca : str, modelo : str, ano : int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

c1 = Carro('Chevrolet', 'Onix', 2017)
c2 = Carro('Hyundai', 'Hilux', 2020)
c3 = Carro('Mercedes Benz', 'AMG', 2025)

print(f'{c1}\n{c2}\n{c3}')

print('#'*14)
c1.ano = 2013

print(f'{c1}\n{c2}\n{c3}')