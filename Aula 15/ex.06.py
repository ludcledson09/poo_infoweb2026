class Service:
 def servico_inserir(descricao, valor):
   if descricao == "": raise ValueError("Descrição inválida")
   if valor < 0: raise ValueError("Valor inválido")
 
