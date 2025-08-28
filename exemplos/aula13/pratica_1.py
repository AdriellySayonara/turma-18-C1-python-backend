#pratica de encapsulamento + getters e setters
class endereco:
    def __init__(self, rua, numero, cidade):
        self.__rua = rua
        self.__numero = numero
        self.__cidade = cidade
    
    def get_rua(self):
        return self.__rua
    
    def set_rua(self, nova_rua):
        if len(nova_rua) > 0:
            self.__rua = nova_rua
        else:
            print("Rua inválida")
    
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, novo_numero):
        if novo_numero > 0:
            self.__numero = novo_numero
        else:
            print("Número inválido")
    
    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, nova_cidade):
        if len(nova_cidade) > 0:
            self.__cidade = nova_cidade
        else:
            print("Cidade inválida")
            
# Uso
e1 = endereco("Rua A", 123, "Cidade X")
print(e1.get_rua())      # Saída: Rua A
print(e1.get_numero())   # Saída: 123  
print(e1.get_cidade())   # Saída: Cidade X
e1.set_rua("Rua B")
e1.set_numero(456)
e1.set_cidade("Cidade Y")


