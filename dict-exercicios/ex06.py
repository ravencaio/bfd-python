palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contador(palavras):
    novo_dict = {}
    for item in palavras:
        novo_dict[f'{item}'] = palavras.count(item)
    return novo_dict

print(contador(palavras))

