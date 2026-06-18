x = {"RN" :"Natal", "PB" : "João Pessoa", "PE" : "Recife"}
x["AM"] = "Manaus"
x[5] = "Teste"# inserie a chave 5
x.pop(5)      # remove a chave 5
y = {} # dicionario vazio
x["PB"] = "J.Pessoa"
y =[1,2,3,4]
z =[1,2,3,4]
print(x)
print(*x)
print(len(x)) # número de itens
print(max(x))

for item in x.items(): print(item)
for item in x: print(item)


print(x)
print(x["RN"])

print(type(x))
print(type(y))
print(type(z))