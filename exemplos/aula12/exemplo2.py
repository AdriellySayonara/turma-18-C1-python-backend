class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome   # atributo
        self.idade = idade # atributo
    
    def apresentar(self): # método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

#objeto em si 
pessoa1 = Pessoa("Maria", 20)
pessoa1.apresentar()

pessoa2 = Pessoa("Irene", 30)
pessoa2.apresentar()

