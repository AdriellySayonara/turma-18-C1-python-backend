
import exemplo1 

criar_usuario("Ana", 25, "ana_email.com") #posicional

def soma(a, b):
    print(a + b)   # devolve o resultado

soma(5, 3)  # guardando o valor em uma variável
soma(30, 80)    



print('-'* 50)

def ola(nome):
    print(f"Olá, {nome}!")  # só executa a ação

ola("Ana")  # Olá, Ana!
x = ola("Bruno")
print(x)    # None, porque a função não retornou valor
# Função que imprime uma saudação, mas não devolve nada

print('-'* 50)

#se quiser imprimir o valor retornado, use return
def ola2(nome):
    return f"Olá, {nome}!"  # devolve a string
print(ola2("Carlos"))  # Olá, Carlos!
# Função que retorna uma saudação como string