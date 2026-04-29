class Retangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0
    def diagonal (self):
        return (self.base ** 2 + self.altura ** 2) ** 0.5

x=Retangulo()
x.base = float(input("digite a base: "))  
x.altura = float(input("digite a altura: "))
diagonal=x.diagonal()
print(diagonal)