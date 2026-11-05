from abc import ABC, abstractmethod

class ClasseAbastrata(ABC):
    def __init__(self, valor):
        super().__init()
       
    @abstractmethod
    def metodoabastrato(self):
        pass