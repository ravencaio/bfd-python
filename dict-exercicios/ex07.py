d = {"a": 1, "b": 2, "c": 3}
e = {}
for k, v in d.items():
    e[v] = k
print(e)