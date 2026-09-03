import json
class Cliente:
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self):
         return {"id" : self.id, "nome" : self.nome}
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"],dic["nome"])

def salvar():
    a = Cliente (1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")
    c = Cliente.from_json({"id" : 3, "nome" : "Alan turing" })

    lista = [a, b, c]

    arquivo = open("clientes json", mode = "w")
    json.dump(lista, arquivo, default = Cliente.to_json)
    arquivo.close()


    print(a)
    print(b)
    print(a.__dict__)
    print(b.__dict__)
    print(vars(a))
    print(vars(b))
    print(a.to_json())
    print(b.to_json())

from models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        # gerar um novo id com o maior valor existente mais um
        id = 0
        if len(self.__objetos) > 0:
            for aux in self.__objetos:
                if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):                
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):  
        try:  
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):    
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()

class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"
    
    def to_json(self):
        return { "id":self.__id, "descricao":self.__descricao, "valor":self.__valor }
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])



