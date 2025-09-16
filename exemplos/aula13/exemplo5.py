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

#Classe concreta que implementa a interface

class Carro(Veiculo):
    def ligar(self):
         return "Carro ligado!"

    def desligar(self):
        return "Carro desligado!"

    def mover(self):
        return "O carro está andando sobre rodas."

class Barco(Veiculo):
    def ligar(self):
        return "Barco ligado!"

    def desligar(self):
        return "Barco desligado!"

    def mover(self):
        return "O barco está navegando na água."

class Moto(Veiculo):
    def ligar(self):
        return "Moto Ligada!"
        
    def desligar(self):
        return "Moto desligada!"
        
    def mover(self):
        return "Moto movida!"
        
carro = Carro()
barco = Barco()
moto = Moto()

print(carro.ligar())
print(carro.desligar())
print(carro.mover())