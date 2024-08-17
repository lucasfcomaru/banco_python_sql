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
                print(f'Nome: {cliente[0]} \nSaldo: R${cliente[1]:.2f} \nCliente desde: {cliente[2]}')
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

    def sacar(nome_cliente, valor_saque):
        try:
            # conectando no banco de dados
            banco = sql.connect('banco.db')
            cursor = banco.cursor() # cursor para executar comandos SQL
            # pega o valor do saldo atual
            cursor.execute("""
                SELECT valor FROM clientes
                    WHERE nome = '{}';
            """.format(nome_cliente))
            banco.commit() # confirma as alterações
            saldo = cursor.fetchone() # retorna o valor do saldo atual em tupla
            saldo_atual = saldo[0] # acessa o índice da tupla
            saldo_atual -= valor_saque

            # Verifica se tem saldo suficiente
            saque = False
            if saldo_atual > 0:
                saque = True
                # atualiza o saldo do cliente
                cursor.execute("""
                    UPDATE clientes
                    SET valor = {}
                    WHERE nome = '{}';
                    """.format(saldo_atual, nome_cliente))
                banco.commit() # confirma as alterações
            else:
                print(f'Você não possui saldo suficiente. \nSaldo atual: R${saldo[0]:.2f}.')

        # exceções em caso de erro
        except sql.Error as erro:
            print(f'Ocorreu um erro ao realizar o saque do cliente {nome_cliente}: {erro}.')
            return False
        
        except:
            print('Informe os campos corretamente')
            return False

        else:
            # verifica se o saque foi feito
            if saque:
                print(f'Saque realizado com sucesso. \nSaldo atual: R${saldo_atual:.2f}')                

        finally:
            cursor.close() # fecha o cursor
            banco.close() # fecha a conexão com o banco de dados

    def depositar(nome_cliente, valor_deposito):
        try:
            # conectando no banco de dados
            banco = sql.connect('banco.db')
            cursor = banco.cursor() # cursor para executar comandos SQL
            deposito = False # servepara fazer a verificação e exibir menssagem correta

            if valor_deposito > 0: # verifica se cliente não digitou um valor negativo ou zero
                deposito = True

                # pega o valor do saldo atual
                cursor.execute("""
                    SELECT valor FROM clientes
                        WHERE nome = '{}';
                """.format(nome_cliente))
                banco.commit() # confirma as alterações
                saldo = cursor.fetchone() # retorna o valor do saldo atual em tupla
                saldo_atual = saldo[0] # acessa o índice da tupla
                saldo_atual += valor_deposito # incrementa o valor do depósito

                # atualiza o saldo do cliente
                cursor.execute("""
                    UPDATE clientes
                    SET valor = {}
                    WHERE nome = '{}';
                    """.format(saldo_atual, nome_cliente))
                banco.commit() # confirma as alterações
            else:
                print(f'R${valor_deposito} Não é um valor válido para depósito. Tente novamente.')

        # exceções em caso de erro
        except sql.Error as erro:
            print(f'Ocorreu um erro ao realizar o saque do cliente {nome_cliente}: {erro}.')

        except:
            print('Informe os campos corretamente')

        else:
            # verifica se o saque foi feito
            if deposito:
                print(f'Depósito realizado com sucesso. \nSaldo atual: R${saldo_atual:.2f}')                
        finally:
            cursor.close() # fecha o cursor
            banco.close() # fecha a conexão com o banco de dados

    def excluir(nome_cliente):
        try:
            # conectando no banco de dados
            banco = sql.connect('banco.db')
            cursor = banco.cursor() # cursor para executar comandos SQL
            exclusao = False
            # verifica se o cliente existe
            cursor.execute("""
                SELECT nome FROM clientes
                    WHERE nome = '{}'
            """.format(nome_cliente))
            banco.commit()
            cliente = cursor.fetchone() # retorna uma tupla

            if cliente[0] == nome_cliente:
                exclusao = True # usado pra fazer a verificação
                # exclui o cliente
                cursor.execute("""
                    DELETE FROM clientes
                        WHERE nome = '{}';
                """.format(nome_cliente))
                banco.commit() # confirma as alterações

        # exceções em caso de erro
        except sql.Error as erro:
            print(f'Ocorreu um erro ao realizar a exclusão do cliente {nome_cliente}: {erro}.')
        except:
            print(f'Ocorreu um erro ao realizar a exclusão do cliente {nome_cliente}.')
        else:
            # verifica se exclusão foi feita
            if exclusao:
                print(f'O cliente {nome_cliente} foi excluído com sucesso.')
        finally:
            cursor.close() # fecha o cursor
            banco.close() # fecha a conexão com o banco de dados

    def transferencia():
        pass