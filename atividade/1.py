class viagem:
    def __init__(self,destino,distancia,litros):
        self.__des = destino
        self.__dis = distancia
        self.__l = litros
    def set_destino(self,v):
        if v!="":self.__des=v
        else: raise ValueError()
    def set_distancia(self,v):
        if v>0: self.__dis =v
    def set_litros(self,v):
        if v>0: self.__l =v
        else: raise ValueError()
    def get_destino(self):
        return self.__des
    def get_distancia(self):
        return self.__dis
    def get_litros(self):
        return self.__l
    def calc_consumo(self):
        return self.__dis/self.__l

# Programa principal
class UI:
    def main():
        destino=(input("qual cidade você viajou?: "))
        distancia=( float(input("qual a distancia?:")) )
        litros =( float(input("quantos litros?:")) )
        x=viagem(destino,distancia,litros)      
        print(f"=O valor da distancia {x.get_distancia()} e quantidade de litros {x.get_litros()}")
        consumo = x.calc_consumo()
        print(f"tem consumo = {consumo}")

UI.main()
