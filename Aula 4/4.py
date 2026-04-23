class contabancaria:
    def __init__(self):
        self.__t = 0
        self.__n = 0
        self.__s = 0
    def set_titular(self,v):
        if v!="": self.__n=v
    def set_numero(self,v):
        if v>0: self.__n =v
        else: raise ValueError()
    def set_saldo(self,v):
      if v>0: self.__s =v
      else: raise ValueError()
    def get_titular(self):
        return self.__t
    def get_numero(self):
        return self.__n
    def get_saldo(self):
        return self.__s

# Programa principal
class UI:
    def main():
        x = contabancaria()           
        x.set_titular (input("josé ludcledson"))
        x.set_numero ( float(input("Entre o valor do numero : ")) )
        x.set_saldo ( float(input("Entre o valor do saldo: ")) )
        print(f"=O valor da numero {x.get_numero()} e saldo {x.get_saldo()} de josé ludcledson{x.get_titular()} ")

UI.main()