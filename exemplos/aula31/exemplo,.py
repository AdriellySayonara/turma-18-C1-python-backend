import json

# 1. armazenamento dos dados (persertencia na memória)

PRODUTOS_EM_MEMORIA = []

PROXIMO_CODIGO = 1

# 2. entidade (o que é o código)

class Produto:
     def __init__(self, codigo, nome, preco):
          self.codigo = codigo
          self.nome = nome
          self.preco = preco
          
     def __str__(self):
          return f"[{self.codigo}] {self.nome} - R$ {self.preco:.2f}"

#3. lógica auxiliar      
def gerar_proximo_codigo():
     global PROXIMO_CODIGO
     codigo_atual = PROXIMO_CODIGO
     PROXIMO_CODIGO += 1
     return codigo_atual

#4. Funções de CRUD

def adicionar_produto(nome: str, preco: float):
     codigo = gerar_proximo_codigo()
     novo_produto = Produto(codigo, nome, preco)
     PRODUTOS_EM_MEMORIA.append(novo_produto)
     print(f"Produto '{nome}' adicionado com o código {codigo}.")

def listar_produtos():
     if not PRODUTOS_EM_MEMORIA:
          return []
     print("\n--- Lista de produtos ---")
     for produto in PRODUTOS_EM_MEMORIA:
          print(produto)
     return PRODUTOS_EM_MEMORIA

def remover_produto(codigo_para_remover: int) -> bool:
     global PRODUTOS_EM_MEMORIA
     
     nova_lista = [p for p in PRODUTOS_EM_MEMORIA if p.codigo !=codigo_para_remover]
     
     if len(nova_lista) < len(PRODUTOS_EM_MEMORIA):
          print(f"Produto com código {codigo_para_remover} removido")
          return True
     else: 
          print(f"ERRO: Código {codigo_para_remover} não encontrado")
          return False
     
if __name__ == "__main__":
     adicionar_produto("café", 30.99)
     adicionar_produto("água com gás", 5.68)
     
     listar_produtos()
     remover_produto(codigo_para_remover=1)
     
     listar_produtos()