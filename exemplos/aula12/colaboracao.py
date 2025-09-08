class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def transferir(self, valor, outra_conta):
        if self.sacar(valor):               # objeto A usa seu método
            outra_conta.depositar(valor)    # e chama método do objeto B
            print(f"Transferência de R${valor:.2f} de {self.titular} para {outra_conta.titular}")
        else:
            print("Saldo insuficiente para transferência.")

# Uso
conta1 = ContaBancaria("João", 500)
conta2 = ContaBancaria("Maria", 200)

conta1.transferir(150, conta2)
print(f"Saldo João: R${conta1.saldo:.2f}")
print(f"Saldo Maria: R${conta2.saldo:.2f}")

""" 
conta1 chama o método transferir.
Dentro do método, conta1 usa outro objeto (conta2) chamando depositar().
Aqui os dois objetos colaboram para realizar uma ação.
"""