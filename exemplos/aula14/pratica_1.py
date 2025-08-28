""" Prática Guiada: Sistema de Contas Bancárias

Criar classe ContaBancaria (pai) com métodos: depositar, sacar, extrato.

Criar classes ContaCorrente e ContaPoupanca (filhas) com métodos próprios:

ContaPoupanca → aplicar_juros()

ContaCorrente → limite_extra()

Testar polimorfismo chamando métodos extrato() para diferentes tipos de conta. """

class ContaBancaria:
	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo

	def depositar(self, valor):
		if valor > 0:
			self.saldo += valor
			print(f"Depósito de R${valor:.2f} realizado.")
		else:
			print("Valor de depósito inválido.")

	def sacar(self, valor):
		if 0 < valor <= self.saldo:
			self.saldo -= valor
			print(f"Saque de R${valor:.2f} realizado.")
		else:
			print("Saldo insuficiente ou valor inválido.")

	def extrato(self):
		print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
	def aplicar_juros(self, taxa):
		if taxa > 0:
			juros = self.saldo * taxa
			self.saldo += juros
			print(f"Juros de R${juros:.2f} aplicados.")
		else:
			print("Taxa de juros inválida.")

class ContaCorrente(ContaBancaria):
	def __init__(self, titular, saldo=0, limite=500):
		super().__init__(titular, saldo)
		self.limite = limite

	def limite_extra(self):
		print(f"Limite extra disponível: R${self.limite:.2f}")

	def sacar(self, valor):
		if 0 < valor <= self.saldo + self.limite:
			self.saldo -= valor
			print(f"Saque de R${valor:.2f} realizado (com limite extra).")
		else:
			print("Saldo e limite insuficientes ou valor inválido.")

# Testando polimorfismo
conta1 = ContaBancaria("Ana", 1000)
conta2 = ContaPoupanca("Bruno", 2000)
conta3 = ContaCorrente("Carla", 500, 1000)

for conta in [conta1, conta2, conta3]:
	conta.extrato()

conta2.aplicar_juros(0.05)
conta2.extrato()

conta3.limite_extra()
conta3.sacar(1200)
conta3.extrato()
