class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome   # privado
        self.__idade = idade # privado

    # Getter
    def get_nome(self):
        return self.__nome

    # Setter
    def set_nome(self, novo_nome):
        if novo_nome.strip() != "":
            self.__nome = novo_nome
        else:
            print("Nome inválido!")

p = Pessoa("Ana", 25)
print(p.get_nome())   # Ana
p.set_nome("Maria")
print(p.get_nome())   # Maria

#---------------------------------------------------------------------------
#usando o propety 
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):   # Getter
        return self.__nome

    @nome.setter
    def nome(self, valor):   # Setter
        if valor.strip() != "":
            self.__nome = valor
        else:
            print("Nome inválido!")

p = Pessoa("Ana", 25)
print(p.nome)    # Getter -> Ana
p.nome = "Maria" # Setter
print(p.nome)    # Getter -> Maria
p.nome = ""      # Setter -> Nome inválido!
