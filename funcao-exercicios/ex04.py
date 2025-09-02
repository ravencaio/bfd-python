def mensagem(nome : str = 'visitante') -> str:
    return f'Olá, {nome}!'

print(mensagem('Fred'))
print(mensagem())