from modules.create_db import create_db # função de criação do banco de dados
from modules.login import login # função de login
from modules.Cliente import Cliente # função de login
# import sqlite3 as sql

create_db() # cria banco de dados com o usuário e a senha do gerente

# menu
while True:
    print('''
-----MENU PRINCIPAL-----
1 - Realizar login
0 - sair
''')

    menu_principal = input('Digite uma opção: ')

    if menu_principal == '1':
        user = input('Digite seu nome de usuário: ').lower()
        password = input('Digite sua senha: ').lower()

        # armazena o retorno da função
        conexao = login(user, password)

        # verifica se conexão é verdadeira ou falsa
        if conexao:
            # menu de gestão de clientes
            while True:
                print('''
-----MENU GERÊNCIA-----
1 - Consultar clientes
2 - Cadastrar clientes
3 - Saque
4 - Transferêcnia
0 - Voltar
                ''')
                menu_gerencia = input('Digite uma opção: ')

                match menu_gerencia:
                    case '1':
                        consulta = Cliente.consulta()
                        #verifica se returna um valor false
                        if not consulta:
                            continue
                        else:
                            print('Consulta realizada com sucesso.')
                            continue
                    case '2':
                        print('Informe os dados do cliente')

                        try:
                            # pega os dados do cliente e cria o objeto Cliente
                            nome_cliente = input('Nome do cliente: ')
                            valor_cliente = float(input('Valor inicial: '))
                            
                        except ValueError:
                            print('Informe um valor válido. Utilize ponto para separar as casas decimais.')
                            continue
                        
                        else:
                            cliente = Cliente(nome_cliente, valor_cliente)

                            if not cliente:
                                continue
                            else:
                                cliente.cadastrar() # cadastrar cliente
                                continue
        
                    case '3':
                        print('Informe os dados para saque')
                        try:
                            nome_saque = input('Nome do cliente: ')
                            valor_saque = float(input('Digite o valor para o saque: '))
                        except ValueError:
                            print('Digite uma informação válida.')
                            continue
                        else:
                            Cliente.sacar(nome_saque, valor_saque)
                    case 4:
                        pass
                    case '0':
                        break
                    case _:
                        print('Digite uma opção válida.')
                        continue
        else:
            print('Falha na conexão, tente novamente.')
    elif menu_principal == '0':
        print('Encerrando o programa...')
        break
    else:
        print('digite uma opção válida')
        continue

    
