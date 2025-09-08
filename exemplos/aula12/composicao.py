

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular   # aqui guardamos o objeto Pessoa
        self.saldo = saldo

    def consultar(self):
        print(f"Conta de {self.titular.nome} | Saldo: R${self.saldo:.2f}")

# Uso
p1 = Pessoa("Ana", 25)                 # Criamos a pessoa
conta1 = ContaBancaria(p1, 1000)       # Criamos a conta ligada à pessoa
conta1.consultar()

"""
Pessoa é independente, mas quando criamos a conta, ela recebe uma Pessoa dentro dela.
self.titular = titular significa que a conta precisa de uma pessoa para existir.
Se a pessoa não existir, a conta perde o sentido.
Por isso é composição.
"""