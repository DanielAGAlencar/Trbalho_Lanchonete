import jsons
import pymongo
from Regex import Regex


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dblanchonete"]
mycolFornecedor = mydb["fornecedor"]

class Fornecedor:
    def __init__(self, id, nome, telefone, nome_produto_venda, segmento_produto, gasto_mensal):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.nome_produto_venda =nome_produto_venda
        self.segmento_produto = segmento_produto
        self.gasto_mensal = gasto_mensal

    def inserir_fornecedor(fornecedor):
        result = mycolFornecedor.insert_one(jsons.dump(fornecedor))
        if result.inserted_id:
            print(f'\nO cadastro da fornecedor foi inserido com sucesso.')

    def preencher_fornecedor():
        a = True
        while (a):
            id = (input('\nInforme o ID: '))
            a = Regex.valida_id(id)
        nome = (input('\nInforme a nome: '))
        c = True
        while (c):
            tel = (input('\nInforme o Telefone: '))
            c = Regex.valida_tel(tel)
        nome_prod = (input('\nInforme nome do produto: '))
        seg_prod = (input('\nInforme o segmento do produto: '))
        d = True
        while (d):
            gasto_mensal = (input('\nInforme o gasto mensal: '))
            d = Regex.valida_valores(gasto_mensal)
        fornecedor = Fornecedor(id, nome, tel, nome_prod, seg_prod, "R$ " + gasto_mensal)
        return fornecedor

    def atualizar_fornecedor(id_fornecedor, fornecedor):
        result = mycolFornecedor.update_one({'id': id_fornecedor}, {"$set": fornecedor.__dict__})
        if result.modified_count > 0:
            print(f'\nO fornecedor foi alterado com sucesso.')

    def excluir_fornecedor(id_fornecedor):
        mycolFornecedor.delete_one({"id": id_fornecedor})
        print("Fornecedor excluído com sucesso!")

    def cons_nome_fornecedor(nome_fornecedor):
        myquery = {"nome": {"$regex": nome_fornecedor}}
        mydoc = mycolFornecedor.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_fornecedor(id_fornecedor):
        myquery = {"id": id_fornecedor}
        mydoc = mycolFornecedor.find(myquery)
        for x in mydoc:
            print(x)

    def listar_fornecedor():
        mydoc = mycolFornecedor.find().sort("id", 1)
        for x in mydoc:
            print(x)