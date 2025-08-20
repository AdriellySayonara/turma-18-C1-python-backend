# Programa que lê três números e informa o maior deles
numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))


if numero1 == numero2 or numero2 == numero3 or numero1 == numero3: 
     exit() #Encerra o programa
     
     
if numero1 > numero2 and numero1 > numero3:
     print("O primeiro número é o maior")
elif numero2 > numero1 and numero2 > numero3:
     print("O segundo número é o maior")
else: 
     print("não é o primeiro nem o segundo, então é o terceiro")
     
     
