"""
Exemplo  de SQLite3 em Python 

Objetivos:
- Criar banco e tabelas SQLite
- Inserir dados
- Consultas SQL: WHERE, ORDER BY, GROUP BY, HAVING
- Funções de agregação: COUNT, SUM, AVG, MIN, MAX
- Estrutura modular, segura e fácil de ler

"""

import sqlite3  # Biblioteca padrão do Python para SQLite
import os       # Para manipulação de arquivos e pastas

# -------------------------------
# CONFIGURAÇÃO DO BANCO
# -------------------------------

# Caminho do arquivo do banco. Vamos criar dentro da pasta aula24
DB_PATH = "aula24/aula24.db"
os.makedirs("aula24", exist_ok=True)  # Garante que a pasta exista

# Se já existir banco com o mesmo nome, remove para começar do zero
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# -------------------------------
# FUNÇÕES DE BANCO
# -------------------------------

def criar_tabelas(con):
    """
    Cria a tabela Vendas no banco de dados.
    
    Argumentos:
    con -- conexão com o banco SQLite
    """
    # Usa 'with' para garantir commit automático
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS Vendas (
                ID_Venda INTEGER PRIMARY KEY,  -- Chave primária auto increment
                Vendedor TEXT NOT NULL,        -- Nome do vendedor
                Valor REAL NOT NULL,           -- Valor da venda
                Data TEXT NOT NULL             -- Data da venda (YYYY-MM-DD)
            );
        """)

def popular_tabelas(con):
    """
    Insere registros iniciais na tabela Vendas.
    
    Argumentos:
    con -- conexão com o banco SQLite
    """
    # Lista de tuplas com dados para inserir
    dados = [
        ('Ana', 500.00, '2025-10-01'),
        ('Bruno', 300.00, '2025-10-02'),
        ('Carla', 800.00, '2025-10-03'),
        ('Ana', 200.00, '2025-10-04'),
        ('Bruno', 700.00, '2025-10-05'),
        ('Daniel', 450.00, '2025-10-06'),
        ('Carla', 600.00, '2025-10-07')
    ]
    # executemany insere várias linhas de forma eficiente
    with con:
        con.executemany("INSERT INTO Vendas (Vendedor, Valor, Data) VALUES (?, ?, ?);", dados)
        # Os '?' são placeholders para evitar SQL Injection

def consultar_vendas(con, where=None, params=(), order_by=None):
    """
    Retorna registros da tabela Vendas com filtros opcionais.
    
    Argumentos:
    where -- string com filtro WHERE (ex: "Vendedor = ? AND Valor > ?")
    params -- tupla com valores para os placeholders
    order_by -- string de ordenação (ex: "Valor DESC")
    
    Retorna:
    lista de dicionários representando cada linha
    """
    query = "SELECT * FROM Vendas"
    if where:
        query += f" WHERE {where}"      # Adiciona filtro se fornecido
    if order_by:
        query += f" ORDER BY {order_by}" # Adiciona ordenação se fornecida

    # Retorna cada linha como dicionário
    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    cursor.execute(query, params)
    return [dict(row) for row in cursor.fetchall()]

def agregacao_por_vendedor(con, having=None, order_by=None):
    """
    Retorna agregações (COUNT, SUM, AVG, MIN, MAX) por vendedor.
    
    Argumentos:
    having -- string com filtro HAVING após GROUP BY (ex: "SUM(Valor) > 1000")
    order_by -- string de ordenação (ex: "Soma DESC")
    
    Retorna:
    lista de dicionários com resultados agregados
    """
    query = """
        SELECT 
            Vendedor,
            COUNT(*) AS Qtd_Vendas,
            SUM(Valor) AS Soma,
            AVG(Valor) AS Media,
            MIN(Valor) AS Minimo,
            MAX(Valor) AS Maximo
        FROM Vendas
        GROUP BY Vendedor
    """
    if having:
        query += f" HAVING {having}"   # Filtra grupos depois da agregação
    if order_by:
        query += f" ORDER BY {order_by}" # Ordena os grupos se necessário

    con.row_factory = sqlite3.Row
    cursor = con.cursor()
    cursor.execute(query)
    return [dict(row) for row in cursor.fetchall()]

# -------------------------------
# SCRIPT PRINCIPAL
# -------------------------------

with sqlite3.connect(DB_PATH) as conexao:  # Abre conexão e garante fechamento
    print("Banco de dados criado em:", os.path.abspath(DB_PATH))

    # Criação da tabela
    criar_tabelas(conexao)
    
    # Inserção dos dados iniciais
    popular_tabelas(conexao)
    print("Tabela 'Vendas' criada e populada.\n")

    # =============================
    # EXEMPLOS DE CONSULTAS
    # =============================

    # WHERE simples
    print("🔹 Vendas do vendedor Ana:")
    for row in consultar_vendas(conexao, where="Vendedor = ?", params=("Ana",)):
        print(row)
    print()

    # WHERE com operadores e ORDER BY
    print("🔹 Vendas com valor > 400, ordenadas por Valor DESC:")
    for row in consultar_vendas(conexao, where="Valor > ?", params=(400,), order_by="Valor DESC"):
        print(row)
    print()

    # GROUP BY simples
    print("🔹 Agregação por vendedor (GROUP BY):")
    for row in agregacao_por_vendedor(conexao):
        print(row)
    print()

    # GROUP BY + HAVING
    print("🔹 Vendedores com soma de vendas > 1000 (HAVING + ORDER BY Soma DESC):")
    for row in agregacao_por_vendedor(conexao, having="SUM(Valor) > 1000", order_by="Soma DESC"):
        print(row)
    print()

    # GROUP BY + HAVING com média
    print("🔹 Vendedores com média de vendas > 500:")
    for row in agregacao_por_vendedor(conexao, having="AVG(Valor) > 500", order_by="Media DESC"):
        print(row)
    print()

print("Demonstração concluída. Banco salvo em 'aula24/aula24.db'.")
