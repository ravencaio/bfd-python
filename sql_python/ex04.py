import sqlite3

conn = sqlite3.connect('escola_v2.db')

cursor = sqlite3.Cursor(conn)
cursor.execute('SELECT * FROM Aluno LEFT JOIN Turma')
print(cursor.fetchall())