alunosGeral = [[],[]]
for c in range(6):
    if c < 3:
        x = float(input(f'Digite a {c+1}ª nota do aluno 1: '))
        alunosGeral[0].append(x)
    else:
        x = float(input(f'Digite a {c-2}ª nota do aluno 2: '))
        alunosGeral[1].append(x)

print(alunosGeral)
