# jeito errado

class Frete:
     def calcular(self, tipo: str, peso: float):
          if tipo == 'mototaxi':
               print('ENTREGA POR MOTO TÁXI')
               return peso * 8.0
          elif tipo == 'pac':
               print('ENTREGA POR MOTO PAC')
               return peso * 2.0
          elif tipo == 'sedex':
               print('ENTREGA POR MOTO SEDEZ')
               return peso * 12.0
          else:
               print('Forma de entrega inválida')
               return 0
          
from abc import ABC, abstractmethod

class Frete(ABC):
     @abstractmethod
     def calcular(self, tipo: str, peso: float):
          pass
     
class FreteMototaxi(Frete):
     def calcular(self,  peso):
          return peso * 8.0

class FretePac(Frete):
     def calcular(self,  peso):
          return peso * 2.0

class FreteSedex(Frete):
     def calcular(self,  peso):
          return peso * 12.0
     
class Calculadora:
     def __init__(self, estrategia: Frete):
          self.estrategia = estrategia
          
if __name__ == "__main__":
     