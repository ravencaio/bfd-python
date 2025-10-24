import sqlite3

db = 'escola_v2.db'

def conectar_db(db):
    conn = sqlite3.connect(db)
    return conn
def listar_tabelas(conn):
    cur = sqlite3.Cursor(conn)
    tabela_cru = cur.execute('SELECT name FROM sqlite_master WHERE type="table";')
    tabelas = [tabela[0] for tabela in tabela_cru]
    return tabelas
sql = conectar_db(db)
print(listar_tabelas(sql))