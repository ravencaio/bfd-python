def media(*args) -> int:
    return sum(args) / len(args)

print(media(4,12,6))
print(media(32,43,23,12,34))
print(media(23,15,86,45,23,12,65,32))

#prova de que ta funcionando:
print('#'*20)
print(media(4,4,4,4,4,4,4))