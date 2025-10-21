# controller/produto_controller.py

from model.produto import Produto
from view import interface

class ProdutoController:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self):
        codigo, nome, preco = interface.obter_dados_produto()
        produto = Produto(codigo, nome, preco)
        self.produtos.append(produto)
        interface.exibir_mensagem(f" Produto '{nome}' adicionado com sucesso!")

    def listar_produtos(self):
        interface.exibir_produtos(self.produtos)

    def remover_produto(self):
        if not self.produtos:
            interface.exibir_mensagem(" Nenhum produto para remover.")
            return

        codigo = int(input("Informe o código do produto para remover: "))
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                interface.exibir_mensagem(f" Produto '{produto.nome}' removido com sucesso!")
                return

        interface.exibir_mensagem(" Produto não encontrado.")

    def executar(self):
        while True:
            interface.exibir_menu()
            opcao = interface.obter_opcao()

            if opcao == "1":
                self.adicionar_produto()
            elif opcao == "2":
                self.listar_produtos()
            elif opcao == "3":
                self.remover_produto()
            elif opcao == "4":
                interface.exibir_mensagem(" Saindo do sistema...")
                break
            else:
                interface.exibir_mensagem(" Opção inválida. Tente novamente.")
