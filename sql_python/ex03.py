import sqlite3

conn = sqlite3.connect('escola_v2.db')

cursor = sqlite3.Cursor(conn)
notas = cursor.execute('SELECT nota1, nota2, nome FROM Aluno')
notas_lista = [((notas[1] + notas[0])/2, notas[2]) for notas in notas]
print(sorted(notas_lista, reverse=True)[:10])
cursor.close()
