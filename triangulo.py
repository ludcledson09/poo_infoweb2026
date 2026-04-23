class triangulo:
    def __init__(self ,b ,h):
        #self._base = 0.0
        #self._altura = 0.0   
        self.set_base(b)
        self.set_altura(h)
    def set_base(self,v):
        if v>=0: self.__b = v
        else: raise ValueError()
    def set_altura(self,v):
        if v>=0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b  
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h/2
    def __str__(self):
        return f"eu sou um triangulo,minha base é {self.__b} e minha é {self.__h}"
class UI:
    def main():
        op=0
        while op!=9:
            op=UI.menu()
            if op == 1: UI.triangulo()
    def menu():
        print("1-triangulo 9-fim")
        op = int(input("informe uma opção: "))
        return op
    def triangulo():
        print("cáculo da área do triangulo")
        b = float(input("informe o valor da base: "))
        h = float(input("informe o valor da altura: "))
        x = triangulo(b,h)
        area=x.calc_area()
        print(x)
        print(f"um triangulo com base {x.get_base()} e altura {x.get_altura()} tem area={area}")
UI.main()

