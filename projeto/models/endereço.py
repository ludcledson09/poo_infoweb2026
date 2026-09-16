class Endereço:
    def __init__(self, id, nome, endereço, id_cliente):
        self.set_id(id)
        self.set_nome(nome)
        self.set_endereço(endereço)
        self.set_id_cliente(id_cliente)
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_endereço(self, endereço):
        if endereço == "": raise ValueError("Endereço deve ser informado")
        self.__endereço = endereço
    def set_id_cliente(self, id_cliente):
        if id_cliente < 0 : raise ValueError("Id_cliente deve ser positivo")
        self.__id_cliente = id_cliente

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_endereço(self) : return self.__endereço
    def get_id_cliente(self) : return self.__id_cliente

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__endereço} - {self.__id_cliente}"
    
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "endereço":self.__endereço, "id_cliente":self.__id_cliente }
    
    @staticmethod
    def from_json(dic):
        return Endereço(dic["id"], dic["nome"], dic["endereço"], dic["id_cliente"])