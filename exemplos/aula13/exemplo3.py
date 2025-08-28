#encampsulamento + getters e setters
#conceito de encapsulamento: esconder detalhes internos de uma classe, expondo apenas o
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("❌ Depósito inválido")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("❌ Saque inválido")
