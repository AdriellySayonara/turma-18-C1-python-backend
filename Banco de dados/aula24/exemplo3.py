
"""
Demonstração de WHERE e ORDER BY no SQLite3

"""

import sqlite3
import os

# Caminho do banco
DB_FILE = "aula24/where_orderby.db"
os.makedirs("aula24", exist_ok=True)

# Remove banco anterior
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# Conexão
conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()

# Criação e inserção de dados
cursor.executescript("""
CREATE TABLE Vendas (
    ID_Venda INTEGER PRIMARY KEY,
    Vendedor TEXT,
    Valor REAL,
    Data TEXT
);

INSERT INTO Vendas (Vendedor, Valor, Data) VALUES
('Ana', 500.00, '2025-10-01'),
('Bruno', 300.00, '2025-10-02'),
('Carla', 800.00, '2025-10-03'),
('Ana', 200.00, '2025-10-04'),
('Bruno', 700.00, '2025-10-05'),
('Daniel', 450.00, '2025-10-06');
""")
conexao.commit()
print("Tabela 'Vendas' criada e populada.\n")

# Função para exibir resultados
def mostrar_resultado(titulo, cursor):
    print("=" * 50)
    print(f"| {titulo.upper():<46} |")
    print("=" * 50)
    print(f"{'ID':<5} | {'Vendedor':<10} | {'Valor':<7} | {'Data':<10}")
    print("-" * 50)
    for linha in cursor.fetchall():
        print(f"{linha[0]:<5} | {linha[1]:<10} | {linha[2]:<7.2f} | {linha[3]:<10}")
    print("\n")

# -----------------------------
# EXEMPLOS DE WHERE
# -----------------------------

# WHERE simples (igualdade)
cursor.execute("SELECT * FROM Vendas WHERE Vendedor = 'Ana';")
mostrar_resultado("WHERE Vendedor = 'Ana'", cursor)

# WHERE com operadores (>, <, >=, <=, <>)
cursor.execute("SELECT * FROM Vendas WHERE Valor > 400;")
mostrar_resultado("WHERE Valor > 400", cursor)

cursor.execute("SELECT * FROM Vendas WHERE Valor <> 500;")
mostrar_resultado("WHERE Valor <> 500", cursor)

# WHERE com AND / OR / NOT
cursor.execute("SELECT * FROM Vendas WHERE Vendedor = 'Bruno' AND Valor > 400;")
mostrar_resultado("WHERE Bruno AND Valor > 400", cursor)

cursor.execute("SELECT * FROM Vendas WHERE Vendedor = 'Ana' OR Valor > 700;")
mostrar_resultado("WHERE Ana OR Valor > 700", cursor)

cursor.execute("SELECT * FROM Vendas WHERE NOT Vendedor = 'Carla';")
mostrar_resultado("WHERE NOT Carla", cursor)

# WHERE com IN e BETWEEN
cursor.execute("SELECT * FROM Vendas WHERE Vendedor IN ('Ana','Daniel');")
mostrar_resultado("WHERE Vendedor IN ('Ana','Daniel')", cursor)

cursor.execute("SELECT * FROM Vendas WHERE Valor BETWEEN 300 AND 700;")
mostrar_resultado("WHERE Valor BETWEEN 300 AND 700", cursor)

# WHERE com LIKE (padrões)
cursor.execute("SELECT * FROM Vendas WHERE Vendedor LIKE 'A%';")
mostrar_resultado("WHERE Vendedor LIKE 'A%'", cursor)

cursor.execute("SELECT * FROM Vendas WHERE Vendedor LIKE '%a';")
mostrar_resultado("WHERE Vendedor LIKE '%a'", cursor)

# -----------------------------
# EXEMPLOS DE ORDER BY
# -----------------------------

# Ordenar por Valor ascendente
cursor.execute("SELECT * FROM Vendas ORDER BY Valor ASC;")
mostrar_resultado("ORDER BY Valor ASC", cursor)

# Ordenar por Valor descendente
cursor.execute("SELECT * FROM Vendas ORDER BY Valor DESC;")
mostrar_resultado("ORDER BY Valor DESC", cursor)

# Ordenar por Vendedor ascendente e Valor descendente
cursor.execute("SELECT * FROM Vendas ORDER BY Vendedor ASC, Valor DESC;")
mostrar_resultado("ORDER BY Vendedor ASC, Valor DESC", cursor)

# Fechar conexão
conexao.close()
print("Demonstração concluída. Banco de dados salvo em 'aula24/where_orderby.db'.")
