pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

for k, v in sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True):
    print(f'{k} ficou com a pontuação {v}')