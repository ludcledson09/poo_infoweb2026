from abc import ABC, abstractmethod
class DAO(ABC):
   def __init__(self, arquivo):
       self._arquivo = arquivo
       self._objetos = []
       self._abrir()