from abc import ABC, abstractmethod

# Produto abstrato
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Produtos concretos
class Caminhao(Transporte):
    def entregar(self):
        return "Entrega feita por caminhão."

class Navio(Transporte):
    def entregar(self):
        return "Entrega feita por navio."

# Criador abstrato
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self):
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        resultado = transporte.entregar()
        return f"[LOGÍSTICA] {resultado}"

# Criadores concretos
class LogisticaTerrestre(Logistica):
    def criar_transporte(self):
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self):
        return Navio()

# Uso
if __name__ == "__main__":
    terrestre = LogisticaTerrestre()
    maritima = LogisticaMaritima()

    print(terrestre.planejar_entrega())
    print(maritima.planejar_entrega())
