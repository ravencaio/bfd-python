from functools import reduce
lista = [2, 3, 4, 5]
print(reduce(lambda x, y: x * y, lista))
