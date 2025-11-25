from model.tarefa import Tarefa, carregar_tarefas, salvar_tarefas, gerar_id, buscar_tarefa_por_id
import views.interface as interface 

class TarefaController:
    def __init__(self):
        # Controller carrega o estado via Model
        self.tarefas = carregar_tarefas()

    # 1. Ação: Adicionar uma nova Tarefa
    def adicionar_tarefa(self):
        # ENTRADA: Controller pede dados à View
        descricao = interface.obter_dados_tarefa()
        
        # PROCESSAMENTO (Lógica de Negócio): Controller pede ID ao Model
        id_tarefa = gerar_id(self.tarefas)
        
        # CRIAÇÃO DO OBJETO Model
        nova_tarefa = Tarefa(id_tarefa, descricao)
        
        # ALTERAÇÃO DO MODEL: Salva a nova tarefa
        self.tarefas.append(nova_tarefa)
        salvar_tarefas(self.tarefas)
        
        # SAÍDA: Controller exibe mensagem via View
        interface.exibir_mensagem(f" Tarefa '{descricao}' cadastrada com ID {id_tarefa}!")

    # 2. Ação: Listar todas as Tarefas
    def listar_tarefas(self):
        # SAÍDA: Controller passa dados do Model para a View
        interface.exibir_tarefas(self.tarefas)

    # 3. Ação: Remover uma Tarefa
    def remover_tarefa(self):
        if not self.tarefas:
            interface.exibir_mensagem(" Nenhuma tarefa para remover.")
            return

        # ENTRADA: Pede ID à View
        id_remover = interface.obter_id()
        
        # PROCESSAMENTO (Busca): Controller MAGRO delega busca ao Model
        tarefa_a_remover = buscar_tarefa_por_id(id_remover, self.tarefas)

        if tarefa_a_remover:
            self.tarefas.remove(tarefa_a_remover)
            salvar_tarefas(self.tarefas)
            interface.exibir_mensagem(f" Tarefa '{tarefa_a_remover.descricao}' removida!")
        else:
            interface.exibir_mensagem(" Tarefa não encontrada.")
            
    # 4. Ação: Marcar como Concluída (Exemplo de Alteração de Estado)
    def concluir_tarefa(self):
        if not self.tarefas:
            interface.exibir_mensagem(" Nenhuma tarefa para concluir.")
            return
            
        id_concluir = interface.obter_id()
        tarefa_a_concluir = buscar_tarefa_por_id(id_concluir, self.tarefas)

        if tarefa_a_concluir:
            tarefa_a_concluir.status = "Concluída"
            salvar_tarefas(self.tarefas) # Persiste a alteração
            interface.exibir_mensagem(f" Tarefa '{tarefa_a_concluir.descricao}' marcada como CONCLUÍDA!")
        else:
            interface.exibir_mensagem(" Tarefa não encontrada.")