import random

def adivinhar_numero_seguro():
    numero_secreto = random.randint(1, 10)
    print("Tente adivinhar o número secreto (entre 1 e 10).")

    while True:
        try:
            # Pedir a entrada do utilizador
            palpite_str = input("Qual é o seu palpite? ")
            # Tentar converter para inteiro
            palpite = int(palpite_str)
            
            # Se a conversão for bem-sucedida, sair do bloco de erro
            if palpite == numero_secreto:
                print("Parabéns! Acertaste!")
                break # Sair do loop
            else:
                print("Palpite errado. Tente novamente.")
        
        except ValueError:
            # Lidar com entrada que não é um número
            print("Erro: Entrada inválida. Por favor, digite um número.")

adivinhar_numero_seguro()