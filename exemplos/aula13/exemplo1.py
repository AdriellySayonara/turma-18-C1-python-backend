class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome     # privado
        self.__idade = idade   # privado
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print(" Nome inválido")
            
            
            
            


