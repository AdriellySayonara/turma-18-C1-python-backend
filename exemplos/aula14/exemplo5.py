# =================== Classes ===================
class Personagem:
    """Classe base com polimorfismo"""
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self):
        """Método genérico, pode ser sobrescrito pelas subclasses"""
        return f"{self.nome} tenta atacar!"

# Subclasses com ataques específicos
class Guerreiro(Personagem):
    def atacar(self):
        return f"{self.nome} ataca com espada!"

class Mago(Personagem):
    def atacar(self):
        return f"{self.nome} lança uma bola de fogo!"

class Arqueiro(Personagem):
    def atacar(self):
        return f"{self.nome} dispara uma flecha!"

# =================== Funções ===================
def tomar_dano(personagem, dano):
    """Aplica dano ao personagem"""
    personagem.vida -= dano
    if personagem.vida < 0:
        personagem.vida = 0
    return f"{personagem.nome} tomou {dano} de dano! Vida restante: {personagem.vida}"

# =================== Criando personagens ===================
guerreiro = Guerreiro("Aragorn")
mago = Mago("Gandalf")
arqueiro = Arqueiro("Legolas")



# =================== Simulação de ataques ===================
# Chamando o mesmo método 'atacar' diretamente, sem checar tipo
print(guerreiro.atacar())  # Aragorn ataca com espada!
print(mago.atacar())       # Gandalf lança uma bola de fogo!
print(arqueiro.atacar())   # Legolas dispara uma flecha!

# Exemplo de dano
print(tomar_dano(guerreiro, 20))  # Aragorn tomou 20 de dano! Vida restante: 80
print(tomar_dano(mago, 15))       # Gandalf tomou 15 de dano! Vida restante: 85
print(tomar_dano(arqueiro, 30))   # Legolas tomou 30 de dano! Vida restante: 70
