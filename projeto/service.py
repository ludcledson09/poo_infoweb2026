from models.cliente import Cliente #entidade
from models.clientedao import ClienteDAO #persistencia
from models.servico import Servico
from models.servicodao import ServicoDAO

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, nascimento):
        obj = Cliente(id, nome, email, fone, nascimento)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, nascimento):
        obj = Cliente(id, nome, email, fone, nascimento)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_aniversariantes(id):
        return ServicoDAO().listar_aniversariantes(id)
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)