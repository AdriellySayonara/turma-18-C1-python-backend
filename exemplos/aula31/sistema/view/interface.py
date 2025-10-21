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
    nome = input("Nome do produto: ")
    while True:
        try:
            preco = float(input("Preço: "))
            return nome, preco
        except ValueError:
            print(" Preço inválido. Digite um número.")

def obter_codigo_produto():
    while True:
        try:
            codigo = int(input("Código do produto: "))
            return codigo
        except ValueError:
            print(" Código inválido. Digite um número inteiro.")

def exibir_produtos(produtos):
    if not produtos:
        print(" Nenhum produto cadastrado.")
    else:
        print("\n--- Lista de Produtos ---")
        for produto in produtos:
            print(produto)

def exibir_mensagem(msg):
    print(msg)
