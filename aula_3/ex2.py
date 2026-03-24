class triangulo:
    def __init__(self):
        self.b=0
        self.h=0
    def calc_area(self):
        return self.b * self.h/2

x= triangulo()
print(x.b,x.h)
x.b=float(input("informe a base do tirângulo/n"))
x.h=float(input("informe a altura do tirângulo/n"))
print(x.b,x.h)
a=x.calc_area()
print(f"a área do triângulo é{a:.2f}")

y= triangulo()
print(y.b,y.h)
x.b=float(input("informe a base do segundo tirângulo/n"))
x.h=float(input("informe a altura do tirângulo/n"))
print(y.b,y.h)
a=y.calc_area()
print(f"a área do triângulo é{a:.2f}")