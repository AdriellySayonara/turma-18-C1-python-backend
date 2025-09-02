""" #variavel global
x = 10

print("Valor de x antes da funcao:", x)
print() #gera erro, pois y é uma variável local


def funcao():
     #variavel local
     x = 5
     y = 20
     print("Valor de x dentro da funcao:", x)
funcao() #A função só é executada quando chamada


print("Valor de x fora da funcao:", x)

#A variável global não é alterada pela variável local

#função somar sem retorno
def somar(a, b):
    resultado = a + b
    print("Resultado da soma é ", resultado)
somar(5, 3)



#função somar com retorno
def somar_com_retorno(a, b):
    resultado = a + b
    return resultado """
#resultado_da_soma = somar_com_retorno(52, 3)
#resultado_de_outra_soma = somar_com_retorno(10, 20)
#print("Resultado da soma com retorno é ", resultado_da_soma)

#outro exemplo
""" def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
num = int(input("Digite um número: ")) #variavel local
resultado = verificar_par_impar(num)
print(f"O número {num} é {resultado}.")

verificar_par_impar(10) #chamada da função
verificar_par_impar(2) #erro, falta argumento """


""" #somar com lista indefinida
def somar_lista(*num): #transforma em tupla
    return sum(num) 
print(somar_lista(1, 2, 3))          # Saída: 6
print(somar_lista(10, 20, 30, 40))  # Saída: 100
print(somar_lista())                 # Saída: 0
print(somar_lista(-1, 1, -2, 2))    # Saída: 0
print(somar_lista(5))                # Saída: 5 """


""" #combinar argumento como dicionario
def imprimir_info(**dic): #transforma em dicionario
    for i, valor in dic.items(): #items() retorna chave e valor
        print(f"{i}: {valor}")
imprimir_info(nome="João", idade=30, cidade="São Paulo")
imprimir_info(produto="Notebook", preco=10000.00, estoque=10)
imprimir_info() #sem argumentos """ 


#argumentos posicionais e nomeados
def criar_usuario(nome, idade, email):
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}")
criar_usuario("Ana", 25, "ana_email.com") #posicional
criar_usuario(email="carlos_email.com", nome="Carlos", idade=30)
criar_usuario("Beatriz", email="beatriz_email.com", idade=22)




