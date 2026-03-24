print("digite quatro valores inteiros")
a=int(input())
b=int(input())
c=int(input())
d=int(input())

soma_impar=0
soma_par=0
if a% 2 == 0:
    soma_par = soma_par+a
else:
       soma_impar = soma_impar+a
if b% 2 == 0:
    soma_par = soma_par+b
else:
       soma_impar = soma_impar+b
if c% 2 == 0:
    soma_par = soma_par+c
else:
       soma_impar = soma_impar+c

if d% 2 == 0:
    soma_par = soma_par+d
else:
       soma_impar = soma_impar+d

print(f'impars: (soma_impar)')
print(f'pares: (soma_par)')