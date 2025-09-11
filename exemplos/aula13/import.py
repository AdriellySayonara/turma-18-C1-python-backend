#Importar o módulo inteiro
import math
print(math.sqrt(16))  # 4.0

"""Usa nome_do_modulo.nome_da_funcao.
Evita conflito de nomes.
Desvantagem: precisa escrever o módulo toda hora."""



#Importar módulo com alias
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

"""as cria um apelido para o módulo.
Útil para módulos com nomes longos."""



#Importar apenas funções/classes específicas
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)        # 3.14159...

"""Evita escrever math.sqrt.
Bom para importar poucas funções."""


#Importar com alias de função/classe
from math import sqrt as raiz
print(raiz(36))  # 6.0

"""Dá apelido a uma função ou classe.
Útil para evitar conflito de nomes."""



#Importar tudo do módulo (não recomendado)
from math import *
print(sin(pi/2))  # 1.0

"""Traz todas funções/classes para o escopo.
Pode causar conflito de nomes.
Não é boa prática em códigos grandes."""



#Importar módulos de subpacotes
from os.path import join
caminho = join("pasta", "arquivo.txt")
print(caminho)  # pasta/arquivo.txt

"""Útil quando o módulo está dentro de pacotes.
Permite importar apenas o que você precisa."""



#Importar módulos de diretórios diferentes
import sys
sys.path.append("/caminho/para/meu/modulo")
import meu_modulo

#Necessário quando módulos não estão no mesmo diretório ou não estão instalados.



