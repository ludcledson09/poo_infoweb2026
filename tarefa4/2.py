class contato:
    def __init__(self,id,nome,email,fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self,id):
        if id < 0: raise ValueError("Id deve se positivo")
    def set__nome(self,nome):
        self.__nome=nome
    def set__email(self,email):
        self.__email=email
    def set__fone(self,fone):
        self.__fone=fone
    def get_id(self):return self.__id
    def get_nome(self):return self.__nome
    def get_emai(self):return self.__email
    def get_fone(self):return self.__fone
    def __str__(self):
       return f"{self.__id}.{self.__nome}.{self.__email}.{self.__fone}"
    
class ContatoUI:
    contatos =[]
    @staticmethod
    def main():
        op = 0
        while op !=6:
            op = ContatoUI.menu()
            if op==1:ContatoUI.inserir()
            if op==2:ContatoUI.listar()
            if op==3:ContatoUI.atualizar()
            if op==4:ContatoUI.excluir()
            if op==5:ContatoUI.pesquisar()
    @staticmethod
    def menu():
        print("1-inseir 2-lista 3-atualizar 4- excluir 5-pesquiar 6- fim")
        return int(input("escolha um opção"))
    @classmethod
    def inserir(cls):
        id = int(input("informe o id do contato"))
        nome =input("informe o nome")
        email=input("informe o e-mail")
        fone =input("inseir o telefone")
        x=contato(id,nome,email,fone)
        cls.contato.append(x)
        print("contato inserido com sucesso")
    @classmethod
    def listar(cls):
        if len(cls.contatos) ==0:print("nemhum contato na agenda")
        else:
            for x in cls.contatos: print(x)
    @classmethod
    def atualizar(cls,id,nome,email,fone):
        o = int(input('você quer atualizar o que(1-id 2-nome 3-mail 4- telefone)'))
        while o != 6:
            if o==1:
             id=int(input('digite seu novo id'))
             x=contato(id,nome,email,fone)
             cls.contatos.append(x)
    @classmethod
    def atualizar(cls):
        ContatoUI.listar()
        id = int(input("informe o id do contato a ser alterado: "))
        x=ContatoUI.listar_id(id)
        if x != None:
            cls.contatos.remove(x)
            nome=input("informe o novo nome: ")
            email=input("informe o novo e-mail: ")
            fone=input("informe o novo telefone: ")
            x=contato(id,nome,email,fone)
    @classmethod
    def exluir(cls):
        id=(input("informe o id do contato a ser excluido: "))
        x=ContatoUI.listar_id(id)
        if x != None:
            cls.contatos.remove
    @classmethod
    def pesquisar(cls):
        iniciais = input("Informe as iniciais do contato: ")
        for x in cls.contatos:
            if x.get_nome().startswith(iniciais): print(x)



ContatoUI.main()