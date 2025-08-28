#interface(contratos)
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"💸 Pagamento de R${valor} via Pix realizado.")

class CartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"💳 Pagamento de R${valor} no cartão realizado.")

# Uso
p1 = Pix()
p2 = CartaoCredito()

p1.pagar(100)
p2.pagar(250)
