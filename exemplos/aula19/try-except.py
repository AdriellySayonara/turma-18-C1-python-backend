# Pedir números ao utilizador
dividendo_str = input("Digite um número para o dividendo: ")
divisor_str = input("Digite um número para o divisor: ")


try:
    # 1. Tentar converter as strings para números inteiros
    dividendo = int(dividendo_str)
    divisor = int(divisor_str)

    # 2. Tentar realizar a divisão
    resultado = dividendo / divisor

# Se um erro de valor ocorrer (por exemplo, o utilizador digita um texto)
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")

# Se o erro for uma divisão por zero
except ZeroDivisionError:
    print("Erro: Não pode dividir um número por zero.")

# Se tudo correr bem, este bloco é executado
else:
    print(f"O resultado da divisão é: {resultado}")

# Este bloco é sempre executado, no final
finally:
    print("Obrigado por usar a calculadora.")

# ====================================================================
# Tipos de Erros Comuns em Python e Suas Explicações
# ====================================================================

# SyntaxError
""" Ocorre quando o código viola as regras de escrita do Python.
O programa não é executado e o erro é detetado antes.
Exemplo: faltar um parêntesis ou dois pontos.

falta dos dois pontos (:)
if 5 > 2
     print("5 é maior")"""

# TypeError
""" Ocorre quando uma operação é aplicada a um tipo de dado incorreto.
Exemplo: tentar somar um número a uma string (e.g., 5 + "cinco").

Exemplo: tentar somar um número a um texto
resultado = 10 - "5" """

# ValueError
""" Ocorre quando o valor de um argumento está incorreto, mesmo que o tipo esteja certo.
Exemplo: tentar converter um texto que não é um número para um inteiro (e.g., int("olá")).

converter um texto que não é um número
int("dez")"""

# ZeroDivisionError
""" Ocorre quando se tenta dividir um número por zero, uma operação matematicamente impossível.
Exemplo: 10 / 0."""

# IndexError
"""
Ocorre quando se tenta aceder a um índice que não existe numa lista ou outro objeto 
sequencial.
# Exemplo: a lista só tem 3 itens, de índice 0 a 2
# minha_lista = [1, 2, 3]
# item = minha_lista[5]
"""

# KeyError
"""
Ocorre quando se tenta aceder a uma chave que não existe num dicionário.
# Exemplo: a chave 'idade' não existe no dicionário
# meu_dicionario = {"nome": "Pedro"}
# idade = meu_dicionario['idade']
"""

# FileNotFoundError
"""
Ocorre quando se tenta abrir ou manipular um arquivo que não existe no caminho 
especificado.
# Exemplo:
# with open('ficheiro_que_nao_existe.txt', 'r') as f:
#    conteudo = f.read()
"""