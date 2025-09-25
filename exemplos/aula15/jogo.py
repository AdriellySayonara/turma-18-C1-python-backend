class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self):
        return f"{self.nome} ataca!"

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        return self.vida

class Guerreiro(Personagem):
    def atacar(self):
        return f"{self.nome} ataca com espada!"

class Mago(Personagem):
    def atacar(self):
        return f"{self.nome} lança uma bola de fogo!"

class Arqueiro(Personagem):
    def atacar(self):
        return f"{self.nome} dispara uma flecha!"
