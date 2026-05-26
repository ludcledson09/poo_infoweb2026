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
{self.__nascimento.strftime("%d/%m/%Y")}"
    def idade(self):
       tempo = datetime.now() - self.__nascimento #timedelta é contado em dias
       anos = tempo.days // 365
       meses = tempo.days % 365 // 30
       return f"Idade: {anos} anos(s) e {meses} mes(es)"
class PacienteUI:
   __pacientes = []
   @staticmethod
   def main():
      op = 0
      while op != 9:
           op = PacienteUI.menu()
           if op==1:PacienteUI.inserir()
           if op==2:PacienteUI.listar()
           if op==3:PacienteUI.atualizar()
           if op==4:PacienteUI.excluir()
           if op==5:PacienteUI.pesquisar()
           if op==6:PacienteUI.aniversariantes()
      
   @staticmethod
   def menu():
      print("1-inserir,2-listar,3-atualizar,4-excluir,5-pesquisar,6-aniversariante,9-fim")
      return int(input("informe uma opção: "))
   
   @classmethod
   def inserir(cls):
       id =int(input("informe o id: "))
       nome =(input("informe o nome: "))
       cpf =int(input("informe o CPF: "))
       fone =(input("informe o telefone: "))
       nasc = datetime.strptime(input("Informe a data de nascimento: "),"%d/%m/%Y")
       x =Paciente(id,nome,cpf,fone,nasc)
       cls.__pacientes.append(x)
    
   @classmethod
   def listar(cls):
      for x in cls.__pacientes:print(x, x.idade())

   @classmethod
   def atualizar(cls):
       for x in cls.__pacientes: print(x)
       id =int(input("informe o id do paciente a ser atualizado: "))
       for x in cls.__pacientes:
         if x.get_id() ==id:
          nome =(input("informe o novo nome: "))
          cpf =int(input("informe o novo CPF: "))
          fone =(input("informe o novo telefone: "))
          nasc = datetime.strptime(input("Informe a nova data de nascimento: "),"%d/%m/%Y")
          x.set_nome(nome)
          x.set_cpf(cpf)
          x.set_telefone(fone)
          x.set_nascimento(nasc)
   @classmethod
   def excluir(cls):
      for x in cls.__pacientes: print(x)
      id =int(input("informe o id do paciente a ser atualizado: "))
      for x in cls.__pacientes:
        if x.get_id() ==id:
          cls.__pacientes.remove(x)
    
   @classmethod
   def pesquisar(cls):
     s=input("informe as iniciais do nome: ")
     for x in cls.__pacientes:
        if x.get_nome().startswit(s):print(x)

   @classmethod
   def aniversariantes(cls):
      m = int(input("input o mês para a listar de aniversaiantes (1-12): "))
      for x in cls.__pacientes:
          if x.get_nascimento().month == m: print(x)
     
PacienteUI.main()
