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

# Função para adicionar um novo usuário na tabela
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()

# Função para listar todos os usuários
def listar_usuarios():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Função para atualizar os dados de um usuário
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?''', (nome, idade, id))
    conexao.commit()
    conexao.close()