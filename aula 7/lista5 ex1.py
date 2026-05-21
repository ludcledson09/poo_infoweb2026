from datetime import datetime
class Paciente:
    def __init__(self,id,n,c,t,nasc):
      self.set_id(id)
      self.set_nome(n)
      self.set_cpf(c)
      self.set_telefone(t)
      self.set_nascimento(nasc)
    def set_id(self,id):
      if id<0: raise ValueError("Id não pode ser negativo")
      self.__id = id
    def set_nome(self,n):
      if n =="": raise ValueError("Nome não pode ser vazio")
      self.__nome = n
    def set_cpf(self,c): 
      if c == "": raise ValueError("CPF não pode ser vazio")
      self.__cpf=c
    def set_telefone(self,t):
      if t =="": raise ValueError("Telefone não pode ser vazio")
      self.__telefone = t
    def set_nascimento(self,nasc):
      if nasc >datetime.now(): raise ValueError("Data não pode ester no futuro")
      self.__nascimento = nasc 
    def get_id(self):  return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return  self.__cpf
    def get_telefone(self): return self.__telefone 
    def get_nascimento(self): return self.__nascimento
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - \
{self._nascimento.strftime("%d/%m%Y")}"
    def idade(self):
       tempo = datetime.now() - self._nascimento #timedelta é contado em dias
       anos = tempo.days // 365
       meses = tempo.days %365 // 0
       return f"Idade: {anos} anos(s) e {meses} mes(es)"
    
x = Paciente(1,"Eduardo","001.002.003-45","84-90009", datetime(2010,1,25))
print(x)
print(x.idade())

class PacienteUI:
   __pacientes = []
   @staticmethod
   def main():
      op = 0
      while op != 9:
           op = PacienteUI()
           if op==1:PacienteUI.inserir()
           if op==2:PacienteUI.instalar()
      
   @staticmethod
   def menu():
      print("1-inserir,2-listar,3-atualizar,4-excluir,5-pesquisar,6-aniversariante,9-fim")
      return int(input("informe uma opção: "))
   
   @staticmethod
   def inserir(cls):
       id =int(input("informe o id: "))
       nome =(input("informe o nome: "))
       cpf =int(input("informe o CPF: "))
       fone =(input("informe o telefone: "))
       nasc = datetime.strptime(input("Informe a data de nascimento"),"%d/%m/%Y")
       x =Paciente(id,nome,cpf,fone,nasc)
       cls.__pacientes.append(x)
    
   @classmethod
   def list(cls):
      for x in cls.__pacientes:print(x, x.idade())

PacienteUI.main()
