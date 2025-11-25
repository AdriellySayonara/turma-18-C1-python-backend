from abc import ABC, abstractmethod

#produto abstrato 
class Pagamento(ABC):
     @abstractmethod
     def pagar(self, valor):
          pass
     
#produto concreto
class Cartao(Pagamento):
     def pagar(self, valor):
          return f"Pagamento de R${valor:.2f} feito com Cartão."
     
class Pix(Pagamento):
     def pagar(self, valor):
          return f"Pagamento de R${valor:.2f} feito com PIX."
     
class Boleto(Pagamento):
     def pagar(self, valor):
          return f"Pagamento de R${valor:.2f} feito com Boleto."

#criador abstrato

class Fabricapagamento(ABC):
     @abstractmethod
     def criar_pagamento(self):
          pass
     def processar_pagamento(self, valor):
          pagamento = self.criar_pagamento()
          resultado = pagamento.pagar(valor)
          return f"[PROCESSAMENTO] {resultado}" 

#fabrica concreta 

class FabricaCartao(Fabricapagamento):
     def criar_pagamento(self):
          return Cartao() 
     
class FabricaPix(Fabricapagamento):
     def criar_pagamento(self):
          return Pix() 
     
class FabricaBoleto(Fabricapagamento):
     def criar_pagamento(self):
          return Boleto() 
     
#uso cliente
#main.py
if __name__ == "__main__":
     tipo = input("Escolha o meio de pagamento (cartao / pix / boleto): ").strip().lower()
     valor = float(input("Digite o valor: "))
     
     if tipo == "cartao":
          fabrica = FabricaCartao()
     elif tipo == "pix":
          fabrica = FabricaPix()
     elif tipo == "boleto":
          fabrica = FabricaBoleto()
     else:
          raise ValueError("Tipo de pagamento inválido!")
     
     print(fabrica.processar_pagamento(valor))
     