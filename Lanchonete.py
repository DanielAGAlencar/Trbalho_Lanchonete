import jsons
import pymongo
from Regex import Regex


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dblanchonete"]
mycolLanchonete = mydb["lanchonete"]

class Lanchonete:

    def __init__(self, id, descricao, qtd_clienets, num_empregados, total_receita, total_despesas):
        self.id = id
        self.descricao = descricao
        self.qtd_clientes = qtd_clienets
        self.num_empregados = num_empregados
        self.total_receita =total_receita
        self.total_despesas = total_despesas

    def inserir_lanchonete(lanchonete):
        result = mycolLanchonete.insert_one(jsons.dump(lanchonete))
        if result.inserted_id:
            print(f'\nO cadastro da lanchonete foi inserido com sucesso.')

    def preencher_lanchonete():

        a = True
        while (a):
            id = (input('\nInforme o ID: '))
            a = Regex.valida_id(id)
        b = (input('\nInforme a descrição: '))
        c = (input('\nInforme a quantidade de clientes: '))
        d = (input('\nInforme o numero de empregados: '))
        e = True
        while (e):
            receita = (input('\nInforme o total de receita: '))
            e = Regex.valida_valores(receita)
        f = True
        while (f):
            despesa = (input('\nInforme o total de despesa: '))
            f = Regex.valida_valores(despesa)
        lanchonete = Lanchonete(id, b, c, d, receita, despesa)
        return lanchonete

    def atualizar_lanchonete(id_lanchonete, lanchonete):
        result = mycolLanchonete.update_one({'id': id_lanchonete}, {"$set": lanchonete.__dict__})
        if result.modified_count > 0:
            print(f'\nA lanchonete foi alterado com sucesso.')

    def excluir_lanchonete(id_lanchonete):
        mycolLanchonete.delete_one({"id": id_lanchonete})
        print("Lanchonente excluído com sucesso!")

    def cons_nome_lanchonete(nome_lanchonete):
        myquery = {"descricao": {"$regex": nome_lanchonete}}
        mydoc = mycolLanchonete.find(myquery)
        for x in mydoc:
            print(x)

    def cons_id_lanchonete(id_lanchonete):
        myquery = {"id": id_lanchonete}
        mydoc = mycolLanchonete.find(myquery)
        for x in mydoc:
            print(x)

    def listar_lanchonete():
        mydoc = mycolLanchonete.find().sort("id", 1)
        for x in mydoc:
            print(x)


