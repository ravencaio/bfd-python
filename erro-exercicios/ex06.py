class IdadeInvalidaError(Exception): ...

def cadastrar_idade(idade):
    print(idade)



idade = int(input('Digite a idade: '))

if idade < 0:
    raise IdadeInvalidaError('Idade menor que 0')
    