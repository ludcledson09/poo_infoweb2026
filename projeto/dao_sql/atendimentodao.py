from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliação(),obj.get_prescrição(), obj.get_id_horario()))

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM atendimento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Atendimento(id, datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario ) for (id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM atendimento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        rows = [row]
        obj = [Atendimento(id, datetime.strptime(data, "%d/%m/%Y %H:%M"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario ) for (id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario) in rows]
        #obj = Atendimento(*row) if row else None
        cls.fechar()
        return obj[0]

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE atendimento SET data=?, queixa_principal=?, historico_saude=?, avaliacao=? prescricao=?, id_horario=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_data().strftime("%d/%m/%Y %H:%M"), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliação(),obj.get_prescrição(), obj.get_id_horario(), obj.get_id() ))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM atendimento WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()