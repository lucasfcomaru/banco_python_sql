import sqlite3 as sql

def create_db():
    # criando o banco de dados
    banco = sql.connect('banco.db')
    cursor = banco.cursor() # cursor para executar comandos SQL
    
    # cria uam tabela se ela não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gerente (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    );
    ''')
    banco.commit() # confirma as alterações

    # insere o usuário gerente 
    cursor.execute('''
    -- se a linha já existir ele ignora o insert
    INSERT OR IGNORE INTO gerente (id, user, password)
        VALUES (1, 'admin', 'admin123');
    ''')
    banco.commit() # confirma as alterações

    # cria a tabela de clientes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        valor REAL NOT NULL,
        cadastro INTEGER NOT NULL
    );
    ''')
    banco.commit() # confirma as alterações

    cursor.close() # fecha o cursor
    banco.close() # fecha a conexão com o banco de dados