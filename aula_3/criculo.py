class circulo:
    def __init__(self):
        self.r=0
    def calc_area(self):
        return 3.14 * self.r**2
    def calc_circunferencia(self):
        return 2 * 3.14 * self.r
x=circulo()
print(x.r)
x.r=float(input("informe o raio do circulo\n"))
print(x.r)
a=x.calc_area()
print(f"a area do circulo é {a:.2f}")
c=x.calc_circunferencia()
print(f"a area do circunferencia é {c:.2f}")