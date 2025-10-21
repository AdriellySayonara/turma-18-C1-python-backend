"""class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}.")
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # chama o construtor da classe Pessoa
        self.curso = curso

    def apresentar(self):
        super().apresentar()  # usa o método da classe Pessoa
        print(f"Estou estudando {self.curso}.")

p1 = Pessoa("Tania", 25)
p1.apresentar()

a1 = Aluno("Reynan", 68 ,"Python")
a1.apresentar()