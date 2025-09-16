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
        """Reduz a vida do personagem e retorna mensagem colorida."""
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        return f"{Fore.RED}{self.nome} tomou {dano} de dano! Vida restante: {self.vida}{Style.RESET_ALL}"

    def curar(self, cura):
        """Aumenta a vida do personagem e retorna mensagem colorida."""
        self.vida += cura
        return f"{Fore.GREEN}{self.nome} se curou {cura} pontos! Vida atual: {self.vida}{Style.RESET_ALL}"

    def esta_vivo(self):
        """Retorna True se o personagem ainda tiver vida."""
        return self.vida > 0

    def mostrar_status(self):
        """Mostra o status atual do personagem com cores."""
        return f"{Fore.CYAN}{self.nome} - Vida: {self.vida}, Força: {self.forca}, Agilidade: {self.agilidade}{Style.RESET_ALL}"

# ================= Subclasses ================= #classes filhas 
# Cada subclasse representa um tipo de personagem com ataques específicos
class Guerreiro(Personagem):
    def atacar(self):
        dano = self.forca * 2
        return dano, f"{Fore.BLUE}{self.nome} ataca com espada causando {dano} de dano!{Style.RESET_ALL}"

    def bloquear(self):
        """Habilidade de bloquear ataque."""
        return f"{Fore.MAGENTA}{self.nome} bloqueia o ataque!{Style.RESET_ALL}"

class Mago(Personagem):
    def atacar(self):
        dano = self.forca + 10
        return dano, f"{Fore.YELLOW}{self.nome} lança uma bola de fogo causando {dano} de dano!{Style.RESET_ALL}"

    def usar_magia(self):
        """Ataque especial do Mago."""
        dano = self.forca + 15
        return dano, f"{Fore.MAGENTA}{self.nome} usa magia poderosa causando {dano} de dano!{Style.RESET_ALL}"

class Arqueiro(Personagem):
    def atacar(self):
        dano = self.forca + 5
        return dano, f"{Fore.GREEN}{self.nome} dispara uma flecha causando {dano} de dano!{Style.RESET_ALL}"

    def ataque_critico(self):
        """Ataque crítico do Arqueiro."""
        dano = (self.forca + 5) * 2
        return dano, f"{Fore.RED}{self.nome} realiza ataque crítico causando {dano} de dano!{Style.RESET_ALL}"

# ================= Criando Personagens via Input =================
# Usuário escolhe os nomes dos personagens
nome_guerreiro = input("Digite o nome do Guerreiro: ")
nome_mago = input("Digite o nome do Mago: ")
nome_arqueiro = input("Digite o nome do Arqueiro: ")

# Criando instâncias das classes com atributos iniciais
guerreiro = Guerreiro(nome_guerreiro, 120, 15, 10)
mago = Mago(nome_mago, 80, 10, 12)
arqueiro = Arqueiro(nome_arqueiro, 90, 12, 18)

# ================= Função de Batalha =================
def batalha(p1, p2):
    """
    Simula uma batalha entre dois personagens.
    - Turno inicial aleatório.
    - Ataques com chance de erro.
    - Dano aleatório para maior imprevisibilidade.
    """
    print(f"\n{Fore.CYAN}Batalha: {p1.nome} VS {p2.nome}{Style.RESET_ALL}")
    
    turn = random.choice([0, 1])  # Escolhe aleatoriamente quem começa
    
    while p1.esta_vivo() and p2.esta_vivo():
        # Define atacante e defensor com base no turno
        atacante = p1 if turn % 2 == 0 else p2
        defensor = p2 if turn % 2 == 0 else p1

        # 10% de chance de falha no ataque
        if random.random() < 0.1:
            print(f"{Fore.MAGENTA}{atacante.nome} tentou atacar, mas errou!{Style.RESET_ALL}")
            dano = 0
            msg = ""
        else:
            # Determina ataque e dano aleatório baseado no tipo de personagem
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

        # Se houve dano, mostra mensagem e aplica ao defensor
        if dano > 0:
            print(msg)
            print(defensor.tomar_dano(dano))

        turn += 1  # Próximo turno

    # Determina e mostra o vencedor da batalha
    vencedor = p1 if p1.esta_vivo() else p2
    print(f"\n{Fore.LIGHTGREEN_EX}{vencedor.nome} venceu a batalha!{Style.RESET_ALL}")

# ================= Função para resetar vida =================
def resetar_vida(personagem):
    """
    Reseta a vida do personagem para o valor inicial,
    garantindo que todas as batalhas comecem justas.
    """
    if isinstance(personagem, Guerreiro):
        personagem.vida = 120
    elif isinstance(personagem, Mago):
        personagem.vida = 80
    elif isinstance(personagem, Arqueiro):
        personagem.vida = 90

# ================= Simulação de batalhas aleatória =================
# Lista de combates
combates = [(guerreiro, mago), (arqueiro, guerreiro), (mago, arqueiro)]
random.shuffle(combates)  # Embaralha a ordem das batalhas para maior imprevisibilidade

# Executa cada batalha, resetando a vida dos personagens antes
for p1, p2 in combates:
    resetar_vida(p1)
    resetar_vida(p2)
    batalha(p1, p2)
