class viagem:
    def __init__(self):
        self.__d = 0
        self.__t = 0
    def set_distancia(self,v):
        if v>0: self.__d =v
        else: raise ValueError()
    def set_tempo(self,v):
        if v>0: self.__t =v
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_velocidade(self):
        return self.__d/self.__t

# Programa principal
class UI:
    def main():
        x = viagem()           
        x.set_distancia ( float(input("Entre o valor da distancia: ")) )
        x.set_tempo ( float(input("Entre o valor do tempo: ")) )
        print(f"=O valor da distancia {x.get_distancia()} e tempo {x.get_tempo()}")
        velocidade = x.calc_velocidade()
        print(f"tem velocidade = {velocidade}")

UI.main()