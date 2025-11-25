# model/tarefa.py

import json
import os

ARQUIVO_DADOS = 'dados_tarefas.json'

class Tarefa:
    """A entidade de dados (Model)."""
    def __init__(self, id_tarefa, descricao, status="Pendente"):
        self.id = id_tarefa
        self.descricao = descricao
        self.status = status
    def __str__(self):
        return f"ID: {self.id} | Status: [{self.status}] | Descrição: {self.descricao}"
    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'status': self.status}

def carregar_tarefas():
    """Lógica de persistência: Carrega dados."""
    if not os.path.exists(ARQUIVO_DADOS) or os.path.getsize(ARQUIVO_DADOS) == 0:
        return []
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            dados = json.load(f)
            return [Tarefa(**d) for d in dados]
    except json.JSONDecodeError:
        return []

def salvar_tarefas(tarefas):
    """Lógica de persistência: Salva dados."""
    dados_para_salvar = [tarefa.to_dict() for tarefa in tarefas]
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados_para_salvar, f, indent=4)

def gerar_id(tarefas):
    """Lógica de negócio: Gera o próximo ID."""
    if not tarefas:
        return 1
    ultimo_id = max(tarefa.id for tarefa in tarefas)
    return ultimo_id + 1

def buscar_tarefa_por_id(id_tarefa, tarefas):
    """Lógica de consulta: Busca por ID."""
    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
    return None