from models.horario import Horario
import json

class HorarioDAO:
    def __init__(self):
        self.__arquivo = "horarios.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
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