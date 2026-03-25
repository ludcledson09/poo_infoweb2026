x=[1,2,3]
y=x
y.append(4)
print(x)
print(type(x),type(y))

class triangulo:
    def __init__(self):
        self.b=0
        self.h=0
    def calc_area(self):
        return self.b * self.h/2

# x é uma referncia - armazena o endereço de um objeto
#triangulo cria um objeto (ou instancia)
x=triangulo()
print(x)
y=x
print(y)
y.b=10
print(x.b)

x=0