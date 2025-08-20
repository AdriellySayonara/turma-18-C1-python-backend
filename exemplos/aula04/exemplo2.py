""" nome = input("Digite seu nome completo: ")  # Entrada de texto

if len(nome) > 30: #len(nome) retorna o número de caracteres da string
    print("Seu nome é longo, ele possui mais de 30 caracteres.")
    print(f"Seu nome possui {len(nome)} caracteres.") 
     """

nome2 = input("Digite seu nome completo: ")  # Entrada de texto

nome_sem_espacos = nome2.replace(" ", "")

if len(nome_sem_espacos) > 30: #len(nome) retorna o número de caracteres da string
    print("Seu nome é longo, ele possui mais de 30 caracteres.")
    print(f"Seu nome possui {len(nome_sem_espacos)} caracteres.") 