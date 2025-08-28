class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ensinar(self, aluno):
        print(f"{self.nome} está ensinando {aluno.nome}")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

p = Professor("Carlos")
a = Aluno("João")

p.ensinar(a)


