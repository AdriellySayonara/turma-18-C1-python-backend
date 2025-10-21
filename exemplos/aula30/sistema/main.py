# main.py

from controller.produto_controller import ProdutoController

def main():
    app = ProdutoController()
    app.executar()

if __name__ == "__main__":
    main()
