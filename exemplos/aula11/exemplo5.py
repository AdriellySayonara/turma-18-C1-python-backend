class ContaBancaria:
    def __init__(self, titular, saldo=0, limite=1000):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f"{self.titular} depositou R${valor}. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"{self.titular} sacou R${valor}. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente!")

# Objetos
conta1 = ContaBancaria("Ana", 1000)
conta2 = ContaBancaria("Bruno", 500)

conta1.sacar(200)
conta2.depositar(300)
