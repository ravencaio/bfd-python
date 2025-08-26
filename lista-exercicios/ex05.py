lista_livros = ['Harry Potter', 'Fahrenheit 451', 'O Senhor dos Anéis']
if lista_livros.count('Silêncio dos inocentes') > 0:
    lista_livros.remove('Silêncio dos inocentes')
else:
    print('Livro não encontrado :(')