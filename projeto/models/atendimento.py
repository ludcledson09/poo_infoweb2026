from datetime import datetime
class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliação, prescrição, id_horario):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliação(avaliação)
        self.set_prescrição(prescrição)
        self.set_id_horario(id_horario)

    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_data(self, data):
        if data < datetime.now(): raise ValueError("Data deve tá no futuro")
        self.__data = data
    def set_queixa_principal(self, queixa_principal):
        if queixa_principal == "": raise ValueError("Queixa deve ser informada")
        self.__queixa_principal = queixa_principal
    def set_historico_saude(self, historico_saude):
        if historico_saude == "": raise ValueError("Historico deve ser informado")
        self.__historico_saude = historico_saude
    def set_avaliação(self, avaliação):
        if avaliação =="" : raise ValueError("Avaliação deve ser informada")
        self.__avaliação = avaliação
    def set_prescrição(self, prescrição):
            if prescrição == "": raise ValueError("Prescrição deve ser informado")
            self.__nome = prescrição
    def set_id_horario(self, id_horario):
        if id_horario < 0: raise ValueError("O Id_horario deve ser positivo")
        self.__id_horario = id_horario

    def get_id(self) : return self.__id
    def get_data(self) : return self.__data
    def get_queixa_principal(self) : return self.__queixa_principal
    def get_historico_saude(self) : return self.__historico_saude
    def get_avaliação(self) : return self.__avaliação
    def get_prescrição(self) : return self.__prescrição
    def get_id_horario(self) : return self.__id_horario

    def to_json(self):
        dic = {"id":self.__id,"data":self.__data.strftime("%d/%m/%Y %H:%M"),\
        "queixa_principal":self.__queixa_principal,"historico_saude":self.__historico_saude,\
        "avaliação":self.__avaliação,"prescrição":self.__prescrição,\
        "id_horario":self.__id_horario}
        return dic
    @staticmethod
    def from_json(dic):
        return Atendimento(dic["id"], dic["data"], dic["queixa_principal"], dic["historico_saude"], dic["avaliação"], dic["prescrição"], dic["id_horario"])
    
                        