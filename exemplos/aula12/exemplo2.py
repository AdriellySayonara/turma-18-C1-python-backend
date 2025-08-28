class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome   # atributo
        self.idade = idade # atributo
    
    def apresentar(self): # método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Maria", 20)
p1.apresentar()
