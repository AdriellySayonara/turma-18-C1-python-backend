# model/produto.py

class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"[{self.codigo}] {self.nome} - R$ {self.preco:.2f}"
