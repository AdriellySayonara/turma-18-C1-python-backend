from colorama import Fore, Style, init
import random

# Inicializa a colorama para usar cores no terminal
init(autoreset=True)

# ================= Classe Base =================
class Personagem:
    """
    Classe base de todos os personagens.
    Contém atributos comuns como nome, vida, força e agilidade,
    e métodos para tomar dano, curar, verificar se está vivo e mostrar status.
    """
    def __init__(self, nome, vida, forca, agilidade):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.agilidade = agilidade

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        return f"{Fore.RED}{self.nome} tomou {dano} de dano! Vida restante: {self.vida}{Style.RESET_ALL}"

    def curar(self, cura):
        self.vida += cura
        return f"{Fore.GREEN}{self.nome} se curou {cura} pontos! Vida atual: {self.vida}{Style.RESET_ALL}"

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_status(self):
        return f"{Fore.CYAN}{self.nome} - Vida: {self.vida}, Força: {self.forca}, Agilidade: {self.agilidade}{Style.RESET_ALL}"

# ================= Subclasses com super() =================
class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca, agilidade, armadura):
        super().__init__(nome, vida, forca, agilidade)  # Chama o __init__ da classe base
        self.armadura = armadura  # Atributo extra da subclasse
        

    def atacar(self):
        dano = self.forca * 2
        return dano, f"{Fore.BLUE}{self.nome} ataca com espada causando {dano} de dano! Armadura: {self.armadura}{Style.RESET_ALL}"

    def bloquear(self):
        return f"{Fore.MAGENTA}{self.nome} bloqueia o ataque usando armadura {self.armadura}!{Style.RESET_ALL}"

class Mago(Personagem):
    def __init__(self, nome, vida, forca, agilidade, mana):
        super().__init__(nome, vida, forca, agilidade)
        self.mana = mana  # Atributo extra do Mago

    def atacar(self):
        dano = self.forca + 10
        return dano, f"{Fore.YELLOW}{self.nome} lança uma bola de fogo causando {dano} de dano! Mana: {self.mana}{Style.RESET_ALL}"

    def usar_magia(self):
        dano = self.forca + 15
        self.mana -= 10
        return dano, f"{Fore.MAGENTA}{self.nome} usa magia poderosa causando {dano} de dano! Mana restante: {self.mana}{Style.RESET_ALL}"

class Arqueiro(Personagem):
    def __init__(self, nome, vida, forca, agilidade, precisao):
        super().__init__(nome, vida, forca, agilidade)
        self.precisao = precisao  # Atributo extra do Arqueiro

    def atacar(self):
        dano = self.forca + 5
        return dano, f"{Fore.GREEN}{self.nome} dispara uma flecha causando {dano} de dano! Precisão: {self.precisao}{Style.RESET_ALL}"

    def ataque_critico(self):
        dano = (self.forca + 5) * 2
        return dano, f"{Fore.RED}{self.nome} realiza ataque crítico causando {dano} de dano! Precisão: {self.precisao}{Style.RESET_ALL}"

# ================= Criando Personagens via Input =================
nome_guerreiro = input("Digite o nome do Guerreiro: ")
nome_mago = input("Digite o nome do Mago: ")
nome_arqueiro = input("Digite o nome do Arqueiro: ")


# Criando instâncias com atributos extras
guerreiro = Guerreiro(nome_guerreiro, 120, 15, 10, armadura=10)
mago = Mago(nome_mago, 80, 10, 12, mana=80)
arqueiro = Arqueiro(nome_arqueiro, 90, 12, 18, precisao=120)

# ================= Função de Batalha =================
def batalha(p1, p2):
    print(f"\n{Fore.CYAN}Batalha: {p1.nome} VS {p2.nome}{Style.RESET_ALL}")
    
    turn = random.choice([0, 1])  # Quem começa aleatoriamente
    
    while p1.esta_vivo() and p2.esta_vivo():
        atacante = p1 if turn % 2 == 0 else p2
        defensor = p2 if turn % 2 == 0 else p1

        if random.random() < 0.1:
            print(f"{Fore.MAGENTA}{atacante.nome} tentou atacar, mas errou!{Style.RESET_ALL}")
            dano = 0
            msg = ""
        else:
            if isinstance(atacante, Guerreiro):
                dano_base, msg = atacante.atacar() if random.random() > 0.2 else (0, atacante.bloquear())
                dano = random.randint(max(1, dano_base - 5), dano_base + 5) if dano_base > 0 else 0
            elif isinstance(atacante, Mago):
                if random.random() > 0.3:
                    dano_base, msg = atacante.atacar()
                else:
                    dano_base, msg = atacante.usar_magia()
                dano = random.randint(max(1, dano_base - 5), dano_base + 5)
            elif isinstance(atacante, Arqueiro):
                if random.random() > 0.3:
                    dano_base, msg = atacante.atacar()
                else:
                    dano_base, msg = atacante.ataque_critico()
                dano = random.randint(max(1, dano_base - 5), dano_base + 5)

        if dano > 0:
            print(msg)
            print(defensor.tomar_dano(dano))

        turn += 1

    vencedor = p1 if p1.esta_vivo() else p2
    print(f"\n{Fore.LIGHTGREEN_EX}{vencedor.nome} venceu a batalha!{Style.RESET_ALL}")

# ================= Função para resetar vida =================
def resetar_vida(personagem):
    if isinstance(personagem, Guerreiro):
        personagem.vida = 120
    elif isinstance(personagem, Mago):
        personagem.vida = 80
    elif isinstance(personagem, Arqueiro):
        personagem.vida = 90

# ================= Simulação de batalhas aleatória =================
combates = [(guerreiro, mago), (arqueiro, guerreiro), (mago, arqueiro)]
random.shuffle(combates)

for p1, p2 in combates:
    resetar_vida(p1)
    resetar_vida(p2)
    batalha(p1, p2)
