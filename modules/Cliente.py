import sqlite3 as sql

class Cliente:
    def __init__(self, nome, valor_inicial):
        self.nome = nome
        self.valor_inicial = valor_inicial
    
    # método para cadastrar um cliente
    def cadastrar(self):
        try:
            # conectando no banco de dados
            banco = sql.connect('banco.db')
            cursor = banco.cursor() # cursor para executar comandos SQL
            # Insere um cliente novo com a data de cadastro do dia atual
            cursor.execute("""
            INSERT INTO clientes (nome, valor, cadastro)
                VALUES ('{}', '{}', date())""".format(self.nome, self.valor_inicial))
            banco.commit() # confirma as alterações

        # uma exceção em caso de erro
        except sql.Error as erro:
            print(f'Ocorreu um erro ao cadastrar o cliente {self.nome}: {erro}.')
            return False

        else:
            print(f'O cliente {self.nome} foi cadastrado com sucesso.')

        finally:
            cursor.close() # fecha o cursor
            banco.close() # fecha a conexão com o banco de dados
    
    def consulta():
        try:
            # conectando no banco de dados
            banco = sql.connect('banco.db')
            cursor = banco.cursor() # cursor para executar comandos SQL
            # Retorna nome, saldo e data de cadastro dos clientes
            cursor.execute("""
            SELECT nome, valor, cadastro
                FROM clientes;
            """)
            banco.commit() # confirma as alterações

            # cria uma lista com os resultados
            resultado = cursor.fetchall()
            
            # itera sobre o resultado
            for cliente in resultado:
                print(f'Nome: {cliente[0]} \nSaldo: {cliente[1]} \nCliente desde: {cliente[2]}')
                print('-' * 10)

        # uma exceção em caso de erro
        except sql.Error as erro:
            print(f'Ocorreu um erro ao consultar os clientes: {erro}.')
            return False

        else:
            print('Consulta realizada com sucesso.')

        finally:
            cursor.close() # fecha o cursor
            banco.close() # fecha a conexão com o banco de dados

    def saque():
        pass

    def transferencia():
        pass