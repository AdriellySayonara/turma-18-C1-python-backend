# views/interface.py

def exibir_menu():
    """View: Exibe o menu de opções."""
    print("\n=== Sistema de Gerenciamento de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Sair")

def obter_opcao():
    """View: Coleta a opção do usuário."""
    return input("Escolha uma opção: ")

def obter_dados_tarefa():
    """View: Coleta a descrição da nova tarefa."""
    return input("Descrição da nova tarefa: ")

def obter_id():
    """View: Coleta e valida o ID da Tarefa."""
    while True:
        try:
            return int(input("Digite o ID da Tarefa: "))
        except ValueError:
            print(" Digite um número válido.")

def exibir_tarefas(tarefas):
    """View: Apresenta a lista de tarefas."""
    if not tarefas:
        print(" Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Lista de Tarefas ---")
        for tarefa in tarefas:
            print(tarefa)

def exibir_mensagem(msg):
    """View: Exibe mensagens de feedback."""
    print(msg)