class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        print(f"Média do {self.nome}: {media:.2f}")

# Objetos
aluno1 = Aluno("João", [7, 8, 9])
aluno2 = Aluno("Maria", [10, 9, 8])

aluno1.calcular_media()
aluno2.calcular_media()
