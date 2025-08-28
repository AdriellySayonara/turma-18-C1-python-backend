# --------------------------------------------
# Simulador de Conta Bancária em Python (POO)
# --------------------------------------------

class ContaBancaria:
    # Construtor da classe (método __init__)
    def __init__(self, titular, saldo_inicial=0):
        # Atributos do objeto (cada conta criada terá esses dados)
        self.titular = titular        # Nome do dono da conta
        self.saldo = saldo_inicial    # Saldo inicial, padrão = 0

    # Método para depósito
    def depositar(self, valor):
        if valor > 0:  # Verifica se o valor é positivo
            self.saldo += valor       # Adiciona o valor ao saldo
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    # Método para saque
    def sacar(self, valor):
        if 0 < valor <= self.saldo:   # Só permite se tiver saldo suficiente
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:      # Se tentar sacar mais do que tem
            print("Saldo insuficiente para o saque.")
        else:                         # Se digitar valor negativo ou zero
            print("O valor do saque deve ser positivo.")

    # Método para consultar saldo
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    # Método para transferir valores entre contas
    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:   # Se tiver saldo suficiente
            self.sacar(valor)         # Retira da conta de origem
            conta_destino.depositar(valor)  # Adiciona na conta de destino
            print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada com sucesso.")
        elif valor > self.saldo:      # Se o valor for maior que o saldo
            print("Saldo insuficiente para a transferência.")
        else:                         # Se for zero ou negativo
            print("O valor da transferência deve ser positivo.")


# --------------------------------------------
# Testando a Conta Bancária
# --------------------------------------------

# Criando duas contas
conta1 = ContaBancaria("Ana", 1000)   # Conta da Ana começa com R$1000
conta2 = ContaBancaria("Carlos", 500) # Conta do Carlos começa com R$500

# Testando operações na conta da Ana
print("\n--- Operações na conta de Ana ---")
conta1.consultar_saldo()
conta1.depositar(500)
conta1.consultar_saldo()
conta1.sacar(200)
conta1.consultar_saldo()
conta1.sacar(2000)       # Teste de saldo insuficiente
conta1.depositar(-100)   # Teste de depósito negativo
conta1.sacar(-50)        # Teste de saque negativo

# Testando transferência de Ana para Carlos
print("\n--- Transferência ---")
conta1.transferir(300, conta2)

# Consultando saldos após a transferência
print("\n--- Saldos finais ---")
conta1.consultar_saldo()
conta2.consultar_saldo()
