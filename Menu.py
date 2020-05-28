from Lanchonete import Lanchonete
from Cliente import Cliente
from Fornecedor import Fornecedor


def lanchonete():
    def lanchonete_opcao():
        print('=================================')
        print("--> 1 - Voltar ao Menu Principal")
        print("--> 2 - Voltar ao Menu de  Lanchonete")
        print("--> 3 - Encerrar Programa")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            menu()
        if opcao == 2:
            lanchonete()
        if opcao == 3:
            exit()
        if opcao != 1 and opcao != 2:
            print("=====Digite uma opção valida=====")
            lanchonete_opcao()

    def consulta_lanchonete():
        print('=================================')
        print("--> 1 - Consulta por Nome")
        print("--> 2 - Consulta por ID")
        print("--> 3 - Listar Todas os Lanchonetes")
        opcao = int(input("Digite a opção desejada: "))
        print('=================================')
        if opcao == 1:
            nome_lanchonete = str(input("\nInforme o Nome da Lanchonete: "))
            Lanchonete.cons_nome_lanchonete(nome_lanchonete)
            print('=================================')
            lanchonete_opcao()
        if opcao == 2:
            id_lanchonete = str(input("\nInforme o ID da Lanchonete: "))
            Lanchonete.cons_id_lanchonete(id_lanchonete)
            print('=================================')
            lanchonete_opcao()
        if opcao == 3:
            Lanchonete.listar_lanchonete()
            print('=================================')
            lanchonete_opcao()
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("=====Digite uma opção valida=====")
            consulta_lanchonete()

    print('=================================')
    print("--> 1 - Para Cadastrar Lanchonete")
    print("--> 2 - Para Alterar  Lanchonete")
    print("--> 3 - Para Excluir Lanchonete")
    print("--> 4 - Para Consultar Lanchonetes")
    print("--> 5 - Para Voltar ao Menu Anterior")
    print("--> 6 - Encerrar o Programa")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Lanchonete.inserir_lanchonete(Lanchonete.preencher_lanchonete())
        print('=================================')
        lanchonete_opcao()
    if opcao == 2:
        id_lanchonente = str(input("\nInforme o id da Lanchonente: "))
        Lanchonete.atualizar_lanchonete(id_lanchonente, Lanchonete.preencher_lanchonete())
        print('=================================')
        lanchonete_opcao()
    if opcao == 3:
        id_lanchonente = str(input("\nInforme o id da Lanchonente: "))
        Lanchonete.excluir_lanchonete(id_lanchonente)
        print('=================================')
        lanchonete_opcao()
    if opcao == 4:
        consulta_lanchonete()
        print('=================================')
    if opcao == 5:
        menu()
        print('=================================')
    if opcao == 6:
        exit()
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao !=6:
        print("=====Digite uma opção valida=====")
        lanchonete()
        print('=================================')

def cliente():
    def cliente_opcao():
        print('=================================')
        print("--> 1 - Voltar ao Menu Principal")
        print("--> 2 - Voltar ao Menu de  Cliente")
        print("--> 3 - Encerrar Programa")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            menu()
        if opcao == 2:
            cliente()
        if opcao == 3:
            exit()
        if opcao != 1 and opcao != 2:
            print("=====Digite uma opção valida=====")
            cliente_opcao()

    def consulta_cliente():
        print('=================================')
        print("--> 1 - Consulta por Nome")
        print("--> 2 - Consulta por ID")
        print("--> 3 - Listar Todos os Clientes")
        opcao = int(input("Digite a opção desejada: "))
        print('=================================')
        if opcao == 1:
            nome_cliente = str(input("\nInforme o Nome do Cliente: "))
            Cliente.cons_nome_cliente(nome_cliente)
            print('=================================')
            cliente_opcao()
        if opcao == 2:
            id_cliente = str(input("\nInforme o ID do Cliente: "))
            Cliente.cons_id_cliente(id_cliente)
            print('=================================')
            cliente_opcao()
        if opcao == 3:
            Cliente.listar_cliente()
            print('================================')
            cliente_opcao()
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("=====Digite uma opção valida=====")
            consulta_cliente()

    print('=================================')
    print("--> 1 - Para Cadastrar Cliente")
    print("--> 2 - Para Alterar  Cliente")
    print("--> 3 - Para Excluir Cliente")
    print("--> 4 - Para Consultar Cliente")
    print("--> 5 - Para Voltar ao Menu Anterior")
    print("--> 6 - Encerrar o Programa")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Cliente.inserir_cliente(Cliente.preencher_cliente())
        print('=================================')
        cliente_opcao()
    if opcao == 2:
        id_cliente = str(input("\nInforme o id do Cliente: "))
        Cliente.atualizar_cliente(id_cliente, Cliente.preencher_cliente())
        print('=================================')
        cliente_opcao()
    if opcao == 3:
        id_cliente = str(input("\nInforme o id do Cliente: "))
        Cliente.excluir_cliente(id_cliente)
        print('=================================')
        cliente_opcao()
    if opcao == 4:
        consulta_cliente()
    if opcao == 5:
        menu()
        print('=================================')
    if opcao == 6:
        exit()
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
        print("=====Digite uma opção valida=====")
        cliente()
        print('=================================')

def fornecedor():
    def fornecedor_opcao():
        print('=================================')
        print("--> 1 - Voltar ao Menu Principal")
        print("--> 2 - Voltar ao Menu de  Fornecedor")
        print("--> 3 - Encerrar Programa")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            menu()
        if opcao == 2:
            fornecedor()
        if opcao == 3:
            exit()
        if opcao != 1 and opcao != 2:
            print("=====Digite uma opção valida=====")
            fornecedor_opcao()

    def consulta_fornecedor():
        print('=================================')
        print("--> 1 - Consulta por Nome")
        print("--> 2 - Consulta por ID")
        print("--> 3 - Listar Todos os Fornecedores")
        opcao = int(input("Digite a opção desejada: "))
        print('=================================')
        if opcao == 1:
            nome_fornecedor = str(input("\nInforme o Nome do Fornecedor: "))
            Fornecedor.cons_nome_fornecedor(nome_fornecedor)
            print('=================================')
            fornecedor_opcao()
        if opcao == 2:
            id_fornecedor = str(input("\nInforme o ID do Fornecedor: "))
            Fornecedor.cons_id_fornecedor(id_fornecedor)
            print('=================================')
            fornecedor_opcao()
        if opcao == 3:
            Fornecedor.listar_fornecedor()
            print('=================================')
            fornecedor_opcao()
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("=====Digite uma opção valida=====")
            consulta_fornecedor()

    print('=================================')
    print("--> 1 - Para Cadastrar Fornecedor")
    print("--> 2 - Para Alterar  Fornecedor")
    print("--> 3 - Para Excluir Fornecedor")
    print("--> 4 - Para Consultar Fornecedor")
    print("--> 5 - Para Voltar ao Menu Anterior")
    print("--> 6 - Encerrar o Programa")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Fornecedor.inserir_fornecedor(Fornecedor.preencher_fornecedor())
        print('=================================')
        fornecedor_opcao()
    if opcao == 2:
        id_fornecedor = str(input("\nInforme o id do Cliente: "))
        Fornecedor.atualizar_fornecedor(id_fornecedor, Fornecedor.preencher_fornecedor())
        print('=================================')
        fornecedor_opcao()
    if opcao == 3:
        id_fornecedor = str(input("\nInforme o id do Cliente: "))
        Fornecedor.excluir_fornecedor(id_fornecedor)
        print('=================================')
        fornecedor_opcao()
    if opcao == 4:
        consulta_fornecedor()
        print('=================================')
    if opcao == 5:
        menu()
        print('=================================')
    if opcao == 6:
        exit()
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
        print("=====Digite uma opção valida=====")
        fornecedor()
        print('=================================')

def menu():
    print('=================================')
    print("--> 1 - Para Lanchonete")
    print("--> 2 - Para Cliente")
    print("--> 3 - Para Fornecedor")
    print("--> 4 - Encerrar o Programa")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        lanchonete()
    if opcao == 2:
        cliente()
    if opcao == 3:
        fornecedor()
    if opcao == 4:
        exit()
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print("=====Digite uma opção valida=====")
        menu()

menu()






