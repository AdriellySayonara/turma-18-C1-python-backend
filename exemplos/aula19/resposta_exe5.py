def ler_linha_arquivo(nome_arquivo, num_linha):
    try:
        # Tentar abrir o arquivo em modo de leitura
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            # Tentar aceder à linha específica
            linha = linhas[num_linha - 1] # -1 porque as listas começam em 0
            print(f"A linha {num_linha} do arquivo é: '{linha.strip()}'")

    except FileNotFoundError:
        # Lidar com o caso de o arquivo não existir
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IndexError:
        # Lidar com o caso de a linha não existir
        print(f"Erro: O arquivo '{nome_arquivo}' não tem a linha {num_linha}.")
    except ValueError:
        # Lidar com entrada que não é um número para o número da linha
        print("Erro: O número da linha deve ser um número inteiro.")

# Exemplo: criar um arquivo temporário para teste
with open("exemplo.txt", "w") as f:
    f.write("Linha 1\nLinha 2\nLinha 3")

# Testes
ler_linha_arquivo("exemplo.txt", 2)
ler_linha_arquivo("arquivo_nao_existe.txt", 1)
ler_linha_arquivo("exemplo.txt", 5)
ler_linha_arquivo("exemplo.txt", "dois")