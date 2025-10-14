
"""
Demonstração de Funções de Agregação no SQLite3
"""

import sqlite3
import os

# Caminho do banco (será criado na pasta local)
DB_FILE = r"E:\turma-18-C1-python-backend\Banco de dados\aula24\exemplo2.db"

# Garante que a pasta exista
os.makedirs("aula24", exist_ok=True)

# Remove o banco anterior, se existir
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# Conexão com o banco
conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()

print("Banco de dados 'agregacao.db' criado com sucesso.\n")

# Criação e inserção de dados
cursor.executescript("""
DROP TABLE IF EXISTS Vendas;

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
('Bruno', 700.00, '2025-10-05');
""")
conexao.commit()

print("Tabela 'Vendas' criada e populada com sucesso.\n")

# -----------------------------
# FUNÇÕES DE AGREGAÇÃO
# -----------------------------

# 1️⃣ COUNT — Conta o total de registros
cursor.execute("SELECT COUNT(*) AS Total_Vendas FROM Vendas;")
print("Total de vendas:", cursor.fetchone()[0])

# 2️⃣ SUM — Soma dos valores
cursor.execute("SELECT SUM(Valor) AS Soma_Valores FROM Vendas;")
print("Soma total dos valores:", cursor.fetchone()[0])

# 3️⃣ AVG — Média dos valores
cursor.execute("SELECT AVG(Valor) AS Media_Valores FROM Vendas;")
print("Média dos valores:", cursor.fetchone()[0])

# 4️⃣ MIN — Menor valor de venda
cursor.execute("SELECT MIN(Valor) AS Menor_Valor FROM Vendas;")
print("Menor valor de venda:", cursor.fetchone()[0])

# 5️⃣ MAX — Maior valor de venda
cursor.execute("SELECT MAX(Valor) AS Maior_Valor FROM Vendas;")
print("Maior valor de venda:", cursor.fetchone()[0])

print("\n--- Agrupamento por Vendedor ---")

# Exemplo com GROUP BY — aplicando as funções por vendedor
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

# Exibe os resultados
print(f"{'Vendedor':<10} | {'Qtd':<5} | {'Soma':<8} | {'Média':<8} | {'Mínimo':<8} | {'Máximo':<8}")
print("-" * 60)
for linha in cursor.fetchall():
    print(f"{linha[0]:<10} | {linha[1]:<5} | {linha[2]:<8.2f} | {linha[3]:<8.2f} | {linha[4]:<8.2f} | {linha[5]:<8.2f}")

# Fecha conexão
conexao.close()
print("\nDemonstração concluída. Banco de dados salvo em 'aula24/exemplo2.db'.")
