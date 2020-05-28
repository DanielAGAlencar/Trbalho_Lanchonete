import  re
import jsons
import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dblanchonete"]
mycolFornecedor = mydb["fornecedor"]
'''
def valida_id(email):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        print("email")
        return True
    else:
        return False
c = True
while (c):
    id = (str(input("digite o id: ")))
    c = valida_id(id)
print(id)'''
'''
def valida_id(id):
    if not re.fullmatch(r"\d{0,9}", id):
        print("Id Invalido")
        return True
    else:
        return False
c = True
while (c):
    id = (str(input("digite o id: ")))
    c = valida_id(id)
print(id)'''

'''def dig():
    tel = (input("digite o telefone: "))
    d = valida_telefone(tel)
    if d == tel:
        return d'''
'''
def valida_telefone():
    tel = (str(input("digite o telefone: ")))
    if not re.fullmatch("(\(?\d{2}\)?\s?\-?\s?)?(\d{4,5}\-?\d{4})", tel):
        print("Telfeone invalido!")
        print(str(tel))
        tel = valida_telefone()
        return tel
    else:
        return tel
c = valida_telefone()
print(str(c))'''
def valida_id(x):
    for y in mycolFornecedor.find({},{ "_id": 0, "name": 0, "telefone": 0, "nome_produto_venda": 0, "segmento_produto": 0, "gasto_mensal": 0 }):

