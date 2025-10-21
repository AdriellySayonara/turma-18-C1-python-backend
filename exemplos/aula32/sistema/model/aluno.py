import json
import os

ARQUIVO = "alunos.json"

class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

    def __str__(self):
        return f"[{self.matricula}] {self.nome} - Curso: {self.curso}"

def carregar_alunos():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            return [Aluno(d["matricula"], d["nome"], d["curso"]) for d in dados]
    except (json.JSONDecodeError, KeyError):
        return []

def salvar_alunos(alunos):
    try:
        with open(ARQUIVO, "w") as f:
            json.dump([{"matricula": a.matricula, "nome": a.nome, "curso": a.curso} for a in alunos], f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar alunos: {e}")

def gerar_matricula(alunos):
    if not alunos:
        return 1
    return max(a.matricula for a in alunos) + 1
