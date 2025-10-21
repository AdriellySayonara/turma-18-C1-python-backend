from model.aluno import Aluno, carregar_alunos, salvar_alunos, gerar_matricula
from view import interface

class AlunoController:
    def __init__(self):
        self.alunos = carregar_alunos()

    def adicionar_aluno(self):
        nome, curso = interface.obter_dados_aluno()
        matricula = gerar_matricula(self.alunos)
        aluno = Aluno(matricula, nome, curso)
        self.alunos.append(aluno)
        salvar_alunos(self.alunos)
        interface.exibir_mensagem(f" Aluno '{nome}' cadastrado com matrícula {matricula}!")

    def listar_alunos(self):
        interface.exibir_alunos(self.alunos)

    def remover_aluno(self):
        if not self.alunos:
            interface.exibir_mensagem(" Nenhum aluno para remover.")
            return
        matricula = interface.obter_matricula()
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                salvar_alunos(self.alunos)
                interface.exibir_mensagem(f" Aluno '{aluno.nome}' removido com sucesso!")
                return
        interface.exibir_mensagem(" Aluno não encontrado.")
