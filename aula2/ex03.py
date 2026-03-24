print("digite quatros valores inteiros")
a= int(input())
b= int(input())
c= int(input())
d= int(input())
#testar se existe algum valor repetido
if a==b or a==c or a==d or b==c or b==d or c==d:
    print("algum valor esta repetido")
else:
    # maior valor 
     maior = a 
     if b > maior: maior = b
     if c > maior: maior = c
     if d > maior: maior = d
    # menor valor 
     menor = a 
     if b < menor: menor = b
     if c < menor: menor = c
     if d < menor: menor = d
    # soma do 2 menor com 2 maior
     soma = a + b + c + d-menor-maior
     print("menor valor",menor)
     print("maior valor",maior)
     print("soma dos outros valores",soma)

