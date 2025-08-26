dict_alunos = {'Claudio' : [10, 7, 6.5], 'João' : [6, 7.8, 9], 'Vicente' : [10, 7.3, 8.7]}
for a, n in dict_alunos.items():
    som = 0
    for c in n:
        som += c
    print(f'A média do aluno {a} foi igual à {som/3:.2f}')

