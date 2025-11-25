# main.py

# Importa o Controller
from controller import TarefaController

# Importa funções da View (diretamente do arquivo de interface dentro da pasta views)
from views.interface import exibir_menu, obter_opcao, exibir_mensagem

def main():
    """
    Função principal que inicia a aplicação e gerencia o loop de controle.
    """
    controller = TarefaController()

    while True:
        exibir_menu() 
        opcao = obter_opcao()
        
        if opcao == '1':
            controller.adicionar_tarefa()
        elif opcao == '2':
            controller.listar_tarefas()
        elif opcao == '3':
            controller.concluir_tarefa()
        elif opcao == '4':
            controller.remover_tarefa()
        elif opcao == '5':
            exibir_mensagem(" Saindo da aplicação. Até logo!")
            break
        else:
            exibir_mensagem(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()