import random
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

# ================= Classe Base =================
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        """Método genérico, será sobrescrito nas subclasses"""
        return 0, f"{self.nome} não sabe atacar!"

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        return f"{Fore.RED}{self.nome} tomou {dano} de dano! Vida restante: {self.vida}{Style.RESET_ALL}"

    def esta_vivo(self):
        return self.vida > 0

# ================= Subclasses =================
class Guerreiro(Personagem):
    def atacar(self):
        dano = random.randint(10, 20)
        return dano, f"{Fore.BLUE}{self.nome} ataca com espada causando {dano} de dano!{Style.RESET_ALL}"

class Mago(Personagem):
    def atacar(self):
        dano = random.randint(5, 25)
        return dano, f"{Fore.YELLOW}{self.nome} lança uma bola de fogo causando {dano} de dano!{Style.RESET_ALL}"

class Arqueiro(Personagem):
    def atacar(self):
        dano = random.randint(8, 18)
        return dano, f"{Fore.GREEN}{self.nome} dispara uma flecha causando {dano} de dano!{Style.RESET_ALL}"

# ================= Criando Personagens =================
guerreiro = Guerreiro("Aragorn", 100)
mago = Mago("Gandalf", 80)
arqueiro = Arqueiro("Legolas", 90)

personagens = [guerreiro, mago, arqueiro]

# ================= Função de batalha =================
def batalha(p1, p2):
    print(f"\n{Fore.CYAN}Batalha: {p1.nome} VS {p2.nome}{Style.RESET_ALL}")
    turn = 0
    while p1.esta_vivo() and p2.esta_vivo():
        atacante = p1 if turn % 2 == 0 else p2
        defensor = p2 if turn % 2 == 0 else p1

        dano, msg = atacante.atacar()  # Polimorfismo
        print(msg)
        print(defensor.tomar_dano(dano))

        turn += 1

    vencedor = p1 if p1.esta_vivo() else p2
    print(f"\n{Fore.LIGHTGREEN_EX}{vencedor.nome} venceu a batalha!{Style.RESET_ALL}")

# ================= Simulação =================
batalha(guerreiro, mago)
batalha(arqueiro, guerreiro)
batalha(mago, arqueiro)
