import sqlite3


conexao = sqlite3.connect('Funcionarios.db')
cursor = conexao.cursor()

# Criar a tabela
cursor.execute("""
CREATE TABLE funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
""")

# Inserir funcionários
funcionarios = [
    ('Irene Freire', 'Gestora governamental de T.I', 50000.00),
    ('Anderson', 'Gestor governamental de T.I', 50000.00),
    ('Jose Reynan', 'Gestor governamental de T.I', 50000.00)
]

cursor.executemany('INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)', funcionarios)

# Confirmar as alterações
conexao.commit()

# Consultar os dados
cursor.execute('SELECT * FROM funcionarios')
resultados = cursor.fetchall()

for funcionario in resultados:
    print(funcionario)

# Fechar a conexão
conexao.close()
