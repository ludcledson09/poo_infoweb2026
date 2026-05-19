from datetime import datetime

x=int(input("informe um numero inteiro: "))
print(x)

d=datetime.strptime(input("informe uma data: "),"%d/%m/%Y")
print(d)
print(d.strftime("%d/%m/%Y"))

#strptime - passa de string para datetime - metodo estático -chama com a classe
#strftime - passa de datetime para string - metodo de instância - chama coma uma variavel
#                                           da classe(objeto)




