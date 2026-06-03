class viagem:
   def __init__(self):
      self.__id = 1
      self.__distancia = 1
      self.__tempo = 1
   def set_id(self, id):
        if id <= 0: raise ValueError("Id deve ser positivo")
        self.__id = id
   def set_distancia(self, distancia):
        if distancia <= 0: raise ValueError("Distancia deve ser positiva")
        self.__distancia = distancia
   def set_tempo(self, tempo):
        if tempo <= 0: raise ValueError("Tempo deve ser positivo")
        self.__tempo = tempo
   def get_id(self): return self.__id
   def get_distancia(self): return self.__distancia
   def get_tempo(self): return self.__tempo
   def velocidade_media(self): return self.__distancia / self.__tempo

class UI:
    viagens = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
        print("tchau!")
    def menu():
        print("1-inserir, 2-listar, 9-fim")
        return int(input("escolha uma opção: "))
    @classmethod
    def inserir(cls):
        x = viagem()
        # x.id = 1 não pode ser uma atribuição, pois id esta encapsulado
        x.set_id(int(input("Informe o id da viagem: ")))
        x.set_distancia(float(input("Informe a distancia em km:")))
        x.set_tempo(float(input("Informe o tempo em horas:")))
        cls.viagens.append(x)
    @classmethod
    def listar(cls):
       for x in cls.viagens:
        print(f"na viagem {x.get_id()}")
        print(f"foram percorridos{x.get_distancia()} km")
        print(f" em {x.get_tempo()}h")
        print(f"A velocidade media foi de {x.velocidade_media():.2f} km/h")

UI.main()