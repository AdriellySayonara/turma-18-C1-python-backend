def buscar_contato():
    contatos = {
        "Ana": "91234-5678",
        "Bruno": "98765-4321",
        "Carla": "95555-4444"
    }
    try:
        # Pedir um nome ao utilizador
        nome = input("Digite o nome do contato: ")
        # Tentar obter o número do dicionário. Se a chave não existir, o erro acontece aqui.
        telefone = contatos[nome]
        print(f"O telefone de {nome} é {telefone}.")
    except KeyError:
        # Lidar com uma chave que não existe no dicionário
        print(f"Erro: O contacto '{nome}' não foi encontrado.")

buscar_contato()