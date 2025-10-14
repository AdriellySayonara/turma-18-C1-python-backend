import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('Loja.db')
cursor = conexao.cursor()

# Criar tabela Produto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL
)
""")

# Inserir alguns produtos
cursor.executemany("""
INSERT INTO Produto (nome, preco) VALUES (?, ?)
""", [
    ('Camiseta', 50.00),
    ('Calça Jeans', 120.00),
    ('Tênis', 250.00),
    ('Boné', 40.00)
])

# Criar tabela Venda
cursor.execute("""
CREATE TABLE IF NOT EXISTS Venda (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (id_produto) REFERENCES Produto (id_produto)
)
""")

# Inserir algumas vendas
cursor.executemany("""
INSERT INTO Venda (id_produto, quantidade) VALUES (?, ?)
""", [
    (1, 3),   # 3 Camisetas
    (2, 2),   # 2 Calças Jeans
    (3, 1),   # 1 Tênis
    (1, 1),   # 1 Camiseta
    (4, 5)    # 5 Bonés
])

# Fazer o JOIN entre Produto e Venda
cursor.execute("""
SELECT Produto.nome, Venda.quantidade
FROM Venda
JOIN Produto ON Venda.id_produto = Produto.id_produto
""")

# Mostrar os resultados
for linha in cursor.fetchall():
    print(linha)

# Salvar e fechar
conexao.commit()
conexao.close()
