#interface(contratos)
from abc import ABC, abstractmethod

# Interface
class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

p2.pagar(250)

#Classe concreta que implementa a interface

class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")

    def mover(self):
        print("O carro está andando sobre rodas.")

class Barco(Veiculo):
    def ligar(self):
        print("Barco ligado!")

    def desligar(self):
        print("Barco desligado!")

    def mover(self):
        print("O barco está navegando na água.")
