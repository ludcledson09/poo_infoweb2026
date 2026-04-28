class Pais():
  def __init__(self,pais,população,area):
     self.pais=pais
     self.população=população
     self.area=area
  def calc_densidade(self):
        if self.area >0:
            return self.população/self.area
        else: return 0
pais=input('nome do pais:')
população=int(input('população:'))
area=float(input('area em km2:'))
d=Pais(pais,população,area)
densidade=d.calc_densidade()
print(f'a densidade demografica do{d.pais} é de {densidade:.2f} habm/km2')
