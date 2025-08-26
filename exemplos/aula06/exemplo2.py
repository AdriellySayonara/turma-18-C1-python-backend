# Lista vazia para armazenar os números
numeros = []

# Usando for para pedir 5 números
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))  # pede input do usuário
    numeros.append(num)  # adiciona na lista

print("Os números digitados foram:", numeros)
