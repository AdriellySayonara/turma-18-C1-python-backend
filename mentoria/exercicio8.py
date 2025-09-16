class Aluno:
     def __init__(self, nome, notas):
          self.nome = nome
          self.notas = notas
     
     def media(self):
          if len(self.notas) > 0:
               return sum(self.notas) / len(self.notas)
          return 0
     
class Escola:
     def __init__(self):
          self.alunos = []
     
     def adicionar_aluno(self, aluno):
          self.alunos.append(aluno)
     
     def media_geral(self):
          if not self.alunos:
               return 0
          soma = 0
          qtd = 0
          for aluno in self.alunos:
               soma += sum(aluno.notas)
               qtd += len(aluno.notas)
          return soma / qtd if qtd > 0 else 0

a1 = Aluno("Eduardo", [8, 9, 10])
a2 = Aluno("Vitória", [8, 9])

escola = Escola()
escola.adicionar_aluno(a1)
escola.adicionar_aluno(a2)

for aluno in escola.alunos:
     print(f"Média de {aluno.nome}: {aluno.media():.2f}")

print("Média geral da turma:", escola.media_geral())