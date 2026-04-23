class Retangulo:
    def __init__(self):
        self.__base = 0       
        self.__altura = 0     
    def set_base(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__base = valor
    def get_base(self):
        return self.__base   
    def get_altura(self):
        return self.__altura    
    def set_altura(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__altura = valor
    def get_area(self):
        return self.__base * self.__altura
    def diagonal(self):       
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5  # 10 pontos
  
# Programa principal
class UI:
    def main():
        x = Retangulo()           
        #x.base = float(input("Entre o valor da base: "))   
        x.set_base ( float(input("Entre o valor da base: ")) )
        #x.altura = float(input("Entre o valor da altura: "))
        x.set_altura ( float(input("Entre o valor da altura: ")) )
        print(f"O retângulo de base = {x.get_base()} e altura {x.get_altura()}")
        area = x.get_area()
        print(f"tem area = {area}")
        diagonal = x.diagonal()
        print(f"tem diagonal = {diagonal}")

UI.main()