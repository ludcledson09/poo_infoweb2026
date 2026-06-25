import json
from pathlib import Path

class Pais:
    def __init__(self,id,nome,sigla,grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla  ==  "": raise ValueError("Sigla deve ser informada")
        self.__sigla = sigla
    def set_grupo(self, grupo):
        if grupo == "": raise ValueError("Grupo deve ser informado")
        self.__grupo= grupo

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_sigla(self) : return self.__sigla
    def get_grupo(self) : return self.__grupo

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__sigla} - {self.__grupo}"
   
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "sigla":self.__sigla, "grupo":self.__grupo }
   
    @staticmethod
    def from_json(dic):
        return Pais(dic["id"], dic["nome"], dic["sigla"], dic["grupo"])
    

class Jogo:
    def __init__(self,id,id_pais1,id_pais2,gols1,gols2,fase,data_hora):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_id_pais1(self, id_pais1):
        if id_pais1 <0: raise ValueError("Id deve ser positivo")
        self.__id_pais1 = id_pais1
    def set_id_pais2(self, id_pais2):
        if id_pais2  <0: raise ValueError("Id deve ser positivo")
        self.__id_pais2 = id_pais2
    def set_gols1(self, gols1):
        if gols1 <0: raise ValueError("Gols deve ser positivo")
        self.__gols1= gols1
    def set_gols2(self, gols2):
        if gols2 <0: raise ValueError("Gols deve ser positivo")
        self.__gols2= gols2
    def set_fase(self, fase):
        if fase  ==  "": raise ValueError("Fase deve ser informada")
        self.__fase = fase
    def set_data_hora(self, data_hora):
        if data_hora == "": raise ValueError("Data e hora deve ser informada")
        self.__data_hora = data_hora

    def get_id(self) : return self.__id
    def get_id_pais1(self) : return self.__id_pais1
    def get_pais2(self) : return self.__id_pais2
    def get_gols1(self) : return self.__gols1
    def get_gols2(self) : return self.__gols2
    def get_fase(self) : return self.__fase
    def get_data_hora(self) : return self.__data_hora

    def __str__(self):
        return f"{self.__id} - {self.__id_pais1} - {self.__id_pais2} - {self.__gols1} - {self.__gols2} - {self.__fase} - {self.__data_hora}"
   
    def to_json(self):
        return { "id":self.__id, "id_pais1":self.__id_pais1, "pais2":self.__id_pais2, "gols1":self.__gols1, "gols2":self.__gols2,"fase":self.__fase,"data_hora":self.__data_hora  }
   
    @staticmethod
    def from_json(dic):
        return Jogo(dic["id"], dic["id_pais1"], dic["id_pais2"], dic["gols1"], dic["gols2"], dic["fase"], dic["data_hora"])
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        id_pais1 = input("Informe o pais: ")
        id_pais2 = input("Informe o pais: ")
        gols1 = input("Informe o numero de gols: ")
        gols2 = input("Informe o numero de gols: ")
        fase = input("Informe a fase: ")
        data_hora = input("Informe a data e a hora: ")
        x = Pais(id, id_pais1, id_pais2, gols1, gols2, fase, data_hora)
        cls.__objetos.append(x)
        PaisUI.salvar()

    @classmethod
    def listar(cls):                
        for x in cls.__objetos: print(x)
        
class PaisUI:
    __objetos = []
    __pais_json = Path(__file__).resolve().parent / "pais.json"
    @staticmethod
    def main():
        PaisUI.abrir()
        op = 0
        while op != 9:
            op = PaisUI.menu()
            if op == 1: PaisUI.inserir()
            if op == 2: PaisUI.listar()
            if op == 3: PaisUI.atualizar()
            if op == 4: PaisUI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def salvar(cls):    
        arquivo = open(cls.__pais_json, mode = "w")
        json.dump(cls.__objetos, arquivo, default = Pais.to_json, indent = 2)
        arquivo.close()

    @classmethod
    def abrir(cls):  
        try:  
            arquivo = open(cls.__pais_json, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__objetos = []
            for dic in list_dic:
                x = Pais.from_json(dic)
                cls.__objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        sigla = input("Informe a sigla: ")
        grupo = input("Informe o grupo: ")
        x = Pais(id, nome, sigla, grupo)
        cls.__objetos.append(x)
        PaisUI.salvar()

    @classmethod
    def listar(cls):                
        for x in cls.__objetos: print(x)

    @classmethod
    def atualizar(cls):
        for x in cls.__objetos: print(x)
        id = int(input("Informe o id do pais a ser atualizado: "))
        for x in cls.__objetos:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                sigla = input("Informe a nova sigla: ")
                grupo = input("Informe o novo grupo: ")
                x.set_nome(nome)
                x.set_email(sigla)
                x.set_fone(grupo)
                PaisUI.salvar()

    @classmethod
    def excluir(cls):
        for x in cls.__objetos: print(x)
        id = int(input("Informe o id do pais a ser excluído: "))
        for x in cls.__objetos:
            if x.get_id() == id:
                cls.__objetos.remove(x)
            PaisUI.salvar()

PaisUI.main()
