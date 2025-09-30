def pedir_numero_valido():
    while True: # Loop infinito até que a entrada seja válida.
        try:
            # Tentar converter a entrada para um número inteiro.
            numero = int(input("Digite um número inteiro: "))
            
        except ValueError:
            # Se a conversão falhar, mostrar uma mensagem de erro e continuar o loop.
            print("Entrada inválida. Por favor, digite um número inteiro.")
        
        else:
            # Se a conversão for bem-sucedida (sem erros), sair do loop.
            print("Obrigado! O número digitado é:", numero)
            break # Sair do loop 'while True'.

# Chamamos a função para testar o comportamento.
pedir_numero_valido()