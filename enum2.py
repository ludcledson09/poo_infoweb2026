from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO= 1
    PAGO_PARCIAL = 2
    Pago = 3

class boleto:
    def __init__(self, cod, emissao,venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO
    def set_cod_barras(self,cod):
        if len(cod) != 10: raise ValueError("código deve ter 10 digitos")
        self.__cod_barras = cod
    def set_data_emissao(self,emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode ser no futuro")
        self.__data_emissao = emissao
    def set_data_vencimento(self,vencimento):
        if vencimento < datetime.now(): raise ValueError("Data não pode ser no passado")
        self.__data_vencimento = vencimento
    def set_valor_boleto(self,valor):
        if valor < 0: raise ValueError("Boleto não pode ter valor negativo")
        self.__valor_boleto = valor
    def set_pagar(self,valor_pago):
        if valor_pago < 0: raise ValueError("Valor não pode ter valor negativo")
        if self.__situaçao_pagamento != Pagamento.EM_ABERTO: raise ValueError("Boleto já foi pago")
        self.__valor_pago = valor_pago
        self._data_pagamento = datetime.now()
        if self.__valor_boleto == self.__valor_pago:self.__situacao_pagamento = Pagamento.PAGO_TOTAL
        else: self.__situaçao_pagamento =Pagamento.PAGO_PARCIAL
    def get__cod_barras(self):return self.__cod_barras
    def get__data_emissao(self):return self.__data_emissao
    def get__data_vencimento(self):return self.__data_vencimento
    def get__valor_boleto(self):return self.__valor_boleto
    def get__valor_pagamento(self):return self.__valor_pagamento
    def get__situacao_pagamento(self):return self.__data_pagamento
    def __str__(self):
        s = f"Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Valor: R$ {self.__valor_boleto:.2f} - Valor Pago: R$ {self.__valor_pago:.2f}"
        s += f"Vencimento: {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Data de Pagamento: {self.__data_pagamento}"
        s += f"Situação: {self.__situacao_pagamento}"
        return s
           
    



    
    