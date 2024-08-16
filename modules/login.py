import sqlite3 as sql

def login_user(user):
    try:
        # conectando no banco de dados
        banco = sql.connect('banco.db')
        cursor = banco.cursor() # cursor para executar comandos SQL
        #seleciona o usuário com base no parâmetro fornecido
        cursor.execute("""
        SELECT user FROM gerente
            WHERE user = '{}'
            """.format(user))
        
        # retorna none se não tiver nenhum valor correpondente
        resultado = cursor.fetchone()

        # verifica se o resultado não é nulo
        # retorna o primeiro resultado correspondente
        if resultado != None:
            print('Usuário verificado com sucesso.')
            return True
        else:
            print('Usuário não existe.')
            return False

    except sql.Error as erro:
        print(f'Ocorreu um erro no nome de usuário: {erro}.')
        return False

    finally:
        cursor.close() # fecha o cursor
        banco.close() # fecha a conexão com o banco de dados
    
def login_password(password):
    try:
        # conectando no banco de dados
        banco = sql.connect('banco.db')
        cursor = banco.cursor() # cursor para executar comandos SQL
        #seleciona o usuário com base no parâmetro fornecido
        cursor.execute("""
        SELECT password FROM gerente
            WHERE password = '{}'
            """.format(password))
        
        # retorna none se não tiver nenhum valor correpondente
        resultado = cursor.fetchone()

        # verifica se o resultado não é nulo
        # retorna o primeiro resultado correspondente
        if resultado != None:
            print('Senha verificada com sucesso.')
            return True
        else:
            print('Senha incorreta.')
            return False

    # uma exceção em caso de erro
    except sql.Error as erro:
        print(f'Ocorreu um erro na senha: {erro}.')
        return False

    finally:
        cursor.close() # fecha o cursor
        banco.close() # fecha a conexão com o banco de dados

# função de login
def login(user, password):
    try:
        # executa as funções e guarda o retorno
        usuario = login_user(user)
        senha = login_password(password)

        # verifica se usuário e senha são verdadeiros
        if usuario and senha:
            print('Usuário logado com sucesso')
            return True
        else:
            return False
    
    # uma exceção caso aconteção algum erro
    except sql.Error as erro:
        print(f'Um erro inesperado aconteceu: {erro}.')
        return False