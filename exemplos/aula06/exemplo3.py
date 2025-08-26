# Lista vazia para armazenar números
numeros = []

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break  # sai do loop se o usuário digitar 0
    numeros.append(num)

print("Os números digitados foram:", numeros)
