from controller.aluno_controller import AlunoController
from view import interface

def main():
    controller = AlunoController()

    while True:
        interface.exibir_menu()
        opcao = interface.obter_opcao()

        try:
            if opcao == "1":
                controller.adicionar_aluno()
            elif opcao == "2":
                controller.listar_alunos()
            elif opcao == "3":
                controller.remover_aluno()
            elif opcao == "4":
                interface.exibir_mensagem(" Saindo do sistema...")
                break
            else:
                interface.exibir_mensagem(" Opção inválida.")
        except Exception as e:
            interface.exibir_mensagem(f" Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
