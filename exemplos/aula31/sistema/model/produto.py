# model/produto.py
import json
import os

ARQUIVO = "produtos.json"

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"[{self.codigo}] {self.nome} - R$ {self.preco:.2f}"

# Carregar produtos do arquivo JSON
def carregar_produtos():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            return [Produto(d["codigo"], d["nome"], d["preco"]) for d in dados]
    except (json.JSONDecodeError, KeyError):
        return []

# Salvar produtos no arquivo JSON
def salvar_produtos(produtos):
    try:
        with open(ARQUIVO, "w") as f:
            json.dump([{"codigo": p.codigo, "nome": p.nome, "preco": p.preco} for p in produtos], f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar produtos: {e}")

# Gerar próximo código automaticamente
def gerar_codigo(produtos):
    if not produtos:
        return 1
    return max(p.codigo for p in produtos) + 1


