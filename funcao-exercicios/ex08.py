def soma(x : int, y : int) -> int:
    return x + y
def subtração(x : int, y : int) -> int:
    return x - y
def multiplicação(x : int, y : int) -> int:
    return x * y
def divisão(x : int, y : int) -> int:
    return x / y

def calcular(x : int, y : int, func) -> int:
    return func(x, y)

print(calcular(12, 32, soma))
