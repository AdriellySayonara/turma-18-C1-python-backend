"""
Demonstração de GROUP BY e HAVING no SQLite3
"""

import sqlite3
import os

# Caminho do banco
DB_FILE = "aula24/group_by_having.db"
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
('Daniel', 450.00, '2025-10-06'),
('Carla', 600.00, '2025-10-07');

""")
conexao.commit()

print("Tabela 'Vendas' criada e populada.\n")

# Função para mostrar resultados
def mostrar_resultado(titulo, cursor):
    print("=" * 70)
    print(f"| {titulo.upper():<66} |")
    print("=" * 70)
    print(f"{'Vendedor':<10} | {'Qtd':<5} | {'Soma':<8} | {'Média':<8} | {'Mínimo':<8} | {'Máximo':<8}")
    print("-" * 70)
    for linha in cursor.fetchall():
        print(f"{linha[0]:<10} | {linha[1]:<5} | {linha[2]:<8.2f} | {linha[3]:<8.2f} | {linha[4]:<8.2f} | {linha[5]:<8.2f}")
    print("\n")

# -----------------------------
# EXEMPLO DE GROUP BY
# -----------------------------
cursor.execute("""
SELECT 
    Vendedor,
    COUNT(*) AS Qtd_Vendas,
    SUM(Valor) AS Soma,
    AVG(Valor) AS Media,
    MIN(Valor) AS Minimo,
    MAX(Valor) AS Maximo
FROM Vendas
GROUP BY Vendedor;
""")
mostrar_resultado("GROUP BY Vendedor", cursor)

# -----------------------------
# EXEMPLO DE GROUP BY + HAVING
# -----------------------------
# Mostra apenas vendedores com soma das vendas maior que 1000
cursor.execute("""
SELECT 
    Vendedor,
    COUNT(*) AS Qtd_Vendas,
    SUM(Valor) AS Soma,
    AVG(Valor) AS Media,
    MIN(Valor) AS Minimo,
    MAX(Valor) AS Maximo
FROM Vendas
GROUP BY Vendedor
HAVING SUM(Valor) > 1000
ORDER BY Soma DESC;
""")
mostrar_resultado("GROUP BY Vendedor + HAVING SUM(Valor) > 1000", cursor)

# -----------------------------
# Exemplo: HAVING com AVG
# -----------------------------
# Mostra vendedores com média de vendas acima de 500
cursor.execute("""
SELECT 
    Vendedor,
    COUNT(*) AS Qtd_Vendas,
    SUM(Valor) AS Soma,
    AVG(Valor) AS Media,
    MIN(Valor) AS Minimo,
    MAX(Valor) AS Maximo
FROM Vendas
GROUP BY Vendedor
HAVING AVG(Valor) > 500
ORDER BY Media DESC;
""")
mostrar_resultado("GROUP BY Vendedor + HAVING AVG(Valor) > 500", cursor)

# Fecha conexão
conexao.close()
print("Demonstração concluída. Banco salvo em 'aula24/group_by_having.db'.")
