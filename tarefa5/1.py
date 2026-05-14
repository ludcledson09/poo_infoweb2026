class Times:
 def _init_(self,id,nome,estado_fed):
    self.set_id(id)
    self.set_nome(nome)
    self.set_estado_fed(estado_fed)

 def set_id(self,id):
    if id <0 or isinstance(id,int): raise ValueError('não pode ser str')
    else:self._id=id
 def set_nome(self,nome):
    if nome =="": raise ValueError('não pode ser vazio')
    else:self._nome=nome  
 def set_estado_fed(self,estado_fed):
    if estado_fed =="": raise ValueError('não pode ser vazio')
    else:self._estado_fed=estado_fed 
 def get_id(self): return self._id
 def get_nome(self): return self._nome
 def get_estado_fed(self): return self._estado_fed
class ContatoUI:
    time = []   # atributo de classe - é uma lista de contatos
    @staticmethod
    def main():
        op = 0
        while op != 6:
         op = ContatoUI.menu()
         if op == 1: ContatoUI.inserirtime()   # C reate
         if op == 2: ContatoUI.listartime()    # R ead
         if op == 3: ContatoUI.atualizartime() # U pdate
         if op == 4: ContatoUI.excluirtime()   # D elete
         if op == 5: ContatoUI.pesquisar()