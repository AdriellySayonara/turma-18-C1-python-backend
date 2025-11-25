from abc import ABC, abstractmethod

# Produto abstrato #definir o que todos os produtos devem fazer
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Produtos concretos #fazem o trabalho real (implementam o método 
# definido no produto abstrado)
class Caminhao(Transporte):
    def entregar(self):
        return "Entrega feita por caminhão."

class Navio(Transporte):
    def entregar(self):
        return "Entrega feita por navio."

class Teletransporte(Transporte):
    def entregar(self):
        return "Entregar feita por teletransporte intantâneo!"

# Criador abstrato /fabrica genérica declara o método de fabrica
# contém a lógica principal 
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self):
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        resultado = transporte.entregar()
        return f"[LOGÍSTICA] {resultado}"

# Criadores concretos fabricas especificas / decide o que o produto vai criar 
class LogisticaTerrestre(Logistica):
    def criar_transporte(self):
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self):
        return Navio()

class LogisticaTeletransporte(Logistica):
    def criar_transporte(self):
        return Teletransporte()

#Uso 
if __name__ == "__main__":
    terrestre = LogisticaTerrestre()
    maritima = LogisticaMaritima()
    teletransporte = LogisticaTeletransporte()

    print(terrestre.planejar_entrega())
    print(maritima.planejar_entrega())
    print(teletransporte.planejar_entrega())


"""Criar uma fábrica de meios de pagamentos: Cartão, Pix, Boleto.
Retornar objeto correto
"""