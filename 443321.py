Atualização do arquivo clientedao.py

from models.cliente import Cliente
from models.dao import DAO
import json

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__("clientes.json")

    def _abrir(self):  
        try:  
            arquivo = open(self._arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self._objetos.append(obj)
        except FileNotFoundError:
            pass

    def _salvar(self):    
        arquivo = open(self._arquivo, mode = "w")
        json.dump(self._objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
    @staticmethod
    def total_atendimentos():
         r = ProfissionalDAO().listar()
         r.sort(key = lambda obj : obj.get_nome().casefold())
         dic = {}
         for obj in r:
                dic[obj.get_id()] = 0
         horarios = HorarioDAO().listar()
         for h in horarios:
            if h.get_confirmado(): dic[h.get_id_profissional()] = dic[h.get_id_profissional()] + 1
         list_prof = []
           for key, value in dic.items():
                prof = {}
                prof["id"] = key
                prof["nome"] = Service.profissional_listar_id(key).get_nome()
                prof["qtd"] = value
                list_prof.append(prof)
            return list_prof