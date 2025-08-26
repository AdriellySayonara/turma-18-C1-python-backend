def soma(a, b):
    return a + b  # devolve o resultado

resultado = soma(5, 3)  # guardando o valor em uma variável
print(resultado)         # 8

print(soma(2, 4) * 2)    # 12, usando diretamente em uma expressão
# Função que soma dois números e devolve o resultado

print('--------------------------------------------------')

def ola(nome):
    print(f"Olá, {nome}!")  # só executa a ação

ola("Ana")  # Olá, Ana!
x = ola("Bruno")
print(x)    # None, porque a função não retornou valor
# Função que imprime uma saudação, mas não devolve nada

print('--------------------------------------------------')

#se quiser imprimir o valor retornado, use return
def ola2(nome):
    return f"Olá, {nome}!"  # devolve a string
print(ola2("Carlos"))  # Olá, Carlos!
# Função que retorna uma saudação como string