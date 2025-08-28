#classe abstratas e métodos abstratos
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Carro(Veiculo):
    def ligar(self):
        print("🚗 O carro está ligado.")

class Moto(Veiculo):
    def ligar(self):
        print("🏍️ A moto está ligada.")

v1 = Carro()
v1.ligar()
