def exibir_menu():
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Remover aluno")
    print("4. Sair")

def obter_opcao():
    return input("Escolha uma opção: ")

def obter_dados_aluno():
    nome = input("Nome do aluno: ")
    curso = input("Curso: ")
    return nome, curso

def obter_matricula():
    while True:
        try:
            return int(input("Matrícula do aluno: "))
        except ValueError:
            print(" Digite um número válido.")

def exibir_alunos(alunos):
    if not alunos:
        print(" Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for aluno in alunos:
            print(aluno)

def exibir_mensagem(msg):
    print(msg)
