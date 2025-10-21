# view/interface.py

def exibir_menu():
    print("\n=== Sistema de Cadastro de Produtos ===")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Sair")

def obter_opcao():
    return input("Escolha uma opção: ")

def obter_dados_produto():
    codigo = int(input("Código do produto: "))
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    return codigo, nome, preco

def exibir_produtos(produtos):
    if not produtos:
        print(" Nenhum produto cadastrado.")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in produtos:
            print(produto)

def exibir_mensagem(mensagem: str):
    print(mensagem)
