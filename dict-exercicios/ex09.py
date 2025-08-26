a = {'manga' : 10, 'maçã' : 9, 'abacaxi' : 7, 'melancia' : 8}
b = {'mangaba' : 6, 'laranja' : 8, 'guaraná' : 10, 'maçã' : 10}
for n, v in b.items():
    a[n] = v
print(a)