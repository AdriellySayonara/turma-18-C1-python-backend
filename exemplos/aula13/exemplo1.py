class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # público
        self.idade = idade    # público

p = Pessoa("Ana", 25)
print(p.nome)   # acesso direto
p.idade = 30    # modificação direta
print(p.idade)


#Protegido (um underline _)
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo   # protegido
    
    def consultar_saldo(self):
        return self._saldo

c = Conta(1000)
print(c._saldo)  # acessível, mas não recomendado
print(c.consultar_saldo())  # forma correta



#Privado (dois underlines __)

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   # privado

    def consultar_saldo(self):
        return self.__saldo

c = ContaBancaria(500)
print(c.consultar_saldo())   # acesso via método

# print(c.__saldo)  # ERRO
print(c._ContaBancaria__saldo)  # "truque", não recomendado
