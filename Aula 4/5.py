class cinema:
    def __init__(self):
        self.__d = 0
        self.__h = 0
        self.__v = 0
    def set_dia(self,v):
        if v>0: self.__d =v
        else: raise ValueError()
    def set_horario(self,v):
        if v>0: self.__h =v
        else: raise ValueError()
    def set_valor(self,v):
        if v:data:segunda, terça e quinta (data:segunda,terça e quinta "r$16"):self.__v=v:
        if v:data:quarta (data:quarta "r$8"(meia entrada)):self.__v=v:
        else: raise ValueError()
    def get_dia(self):
        return self.__d
    def get_horario(self):
        return self.__h
    def get_valor(self):
        return self.__v

# Programa principal
class UI:
    def main():
        x = cinema()           
        x.set_dia (input("Entre o dia da sessão : "))
        x.set_horario( int(input("Entre o horario da sessão : ")) )
        x.set_valor( float(input("Entre o valor do sessão: ")) )
        print(f"=O valor da dia {x.get_dia()} e horario {x.get_horario()} ")

UI.main()