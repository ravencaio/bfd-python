def dados_pessoais(**kwargs):
    for c in kwargs.values():
        print(c)

dados_pessoais(nome="Ana", idade=25, cidade="Recife", profissão='Encanadora', aspiração='Programação')