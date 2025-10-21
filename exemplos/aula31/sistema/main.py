# main.py

from controller.produto_controller import ProdutoController

if __name__ == "__main__":
    app = ProdutoController()
    app.executar()
