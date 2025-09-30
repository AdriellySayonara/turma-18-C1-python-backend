def ler_arquivo_seguro(nome_arquivo):
    try:
        # Tentar abrir o ficheiro em modo de leitura.
        # Se o arquivo não existir, um FileNotFoundError será levantado.
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

    except FileNotFoundError:
        # Capturar o erro específico para ficheiros não encontrados.
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

    finally:
        # Este bloco é sempre executado, com ou sem erro.
        # Serve para garantir que o ficheiro é fechado.
        if 'arquivo' in locals() and not arquivo.closed:
            arquivo.close()
            print("Arquivo fechado.")

# Teste com um arquivo que existe e um que não existe.
ler_arquivo_seguro("exemplo.txt")
ler_arquivo_seguro("arquivo_inexistente.txt")