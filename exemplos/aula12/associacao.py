class Escola:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome, escola):
        self.nome = nome
        self.escola = escola   # referência à escola

    def apresentar(self):
        print(f"Sou {self.nome} e estudo na escola {self.escola.nome}")

# Uso
escola1 = Escola("Escola Municipal")   # Criamos a escola
aluno1 = Aluno("Carlos", escola1)      # Criamos o aluno ligado à escola
aluno1.apresentar()


"""
Aluno e Escola podem existir sozinhos.
Mas um aluno pode estar associado a uma escola, e vice-versa.
Se a escola deixar de existir, o aluno ainda existe.
"""