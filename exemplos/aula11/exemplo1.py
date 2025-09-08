# Classe
#self referencia ao próprio objeto
class Pessoa:
    def __init__(self, nome, idade):  # construtor
        self.nome = nome            # atributo 
        self.idade = idade          # atributo

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
    # outro método com parâmetro extra
    def fazer_aniversario(self, anos):
        self.idade += anos
        print(f"{self.nome} agora tem {self.idade} anos!")

# Objeto
pessoa1 = Pessoa("Ana", 25)

# Chamando métodos
pessoa1.apresentar()           # Olá, meu nome é Ana e tenho 25 anos.
pessoa1.fazer_aniversario(1)  # Ana agora tem 26 anos
pessoa1.apresentar()           # Olá, meu nome é Ana e tenho 26 anos.
