class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []   # lista para guardar alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        print(f"Turma {self.nome} possui os alunos:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")

# Uso
a1 = Aluno("Lucas")
a2 = Aluno("Mariana")

turma1 = Turma("Matemática")
turma1.adicionar_aluno(a1)
turma1.adicionar_aluno(a2)

turma1.listar_alunos()

"""
Aluno existe sozinho.
Turma existe sozinha também.
Mas a Turma agrega alunos em uma lista.
Se a Turma for apagada, os Alunos continuam existindo.
"""
