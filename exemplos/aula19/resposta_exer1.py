def acessar_indice_lista():
    lista = [10, 20, 30, 40, 50]
    try:
        # Pedir ao utilizador o índice
        indice_str = input("Digite um número de 0 a 4: ")
        # Tentar converter para inteiro
        indice = int(indice_str)
        # Tentar aceder à lista
        item = lista[indice]
        print(f"O item no índice {indice} é {item}.")
    except ValueError:
        # Lidar com entrada que não é um número
        print("Erro: Por favor, digite um número válido.")
    except IndexError:
        # Lidar com um índice que não existe
        print("Erro: O número deve ser entre 0 e 4.")

acessar_indice_lista()