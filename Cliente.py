import jsons
import pymongo
from Regex import Regex

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dblanchonete"]
mycolCliente = mydb["cliente"]

class Cliente:


    def __init__(self, id, nome, telefone, cidade, estado, endereco, email, dt_nascimento):
        self.id =id
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco
        self.email = email
        self.dt_nascimento = dt_nascimento

    def inserir_cliente(cliente):
        result = mycolCliente.insert_one(jsons.dump(cliente))
        if result.inserted_id:
            print(f'\nO cadastro da cliente foi inserido com sucesso.')

    def preencher_cliente():
        a = True
        while (a):
            id = (input('\nInforme o ID: '))
            a = Regexa.valida_id(id)
        b = (input('\nInforme a nome: '))
        c = True
        while (c):
            tel = (input('\nInforme o Telefone: '))
            c = Regex.valida_tel(tel)
        d = (input('\nInforme a cidade: '))
        e = (input('\nInforme o estado: '))
        f = (input('\nInforme o endereço: '))
        g = (input('\nInforme o email: '))
        h = (input('\nInforme a data de nascimento: '))
        cliente = Cliente(id, b, tel, d, e, f, g, h)
        return cliente

    def atualizar_cliente(id_cliente, cliente):
        result = mycolCliente.update_one({'id': id_cliente}, {"$set": cliente.__dict__})
        if result.modified_count > 0:
            print(f'\nO cliente foi alterado com sucesso.')

    def excluir_cliente(id_cliente):
        mycolCliente.delete_one({"id": id_cliente})
        print("Cliente excluído com sucesso!")

    def cons_nome_cliente(nome_cliente):
        myquery = {"nome": {"$regex": nome_cliente}}
        mydoc = mycolCliente.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_cliente(id_cliente):
        myquery = {"id": id_cliente}
        mydoc = mycolCliente.find(myquery)
        for x in mydoc:
            print(x)

    def listar_cliente():
        mydoc = mycolCliente.find().sort("id", 1)
        for x in mydoc:
            print(x)