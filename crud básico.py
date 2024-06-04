import sqlite3

# Função para criar a tabela
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        idade INTEGER)''')
    conexao.commit()
    conexao.close()