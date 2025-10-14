import sqlite3


# 1. Conectar ao banco de dados (ele cria o arquivo se não existir)
conexao = sqlite3.connect('pesquisa.db')

# Criar um cursor: é por meio dele que executamos os comandos SQL
cursor = conexao.cursor()

# --- ETAPA CREATE ---
# 2. Executar o comando CREATE TABLE
# Usamos try/except para o script não dar erro se a tabela já existir
try:
    cursor.execute("""
        CREATE TABLE Pacientes (
            paciente_id INTEGER PRIMARY KEY,
            nome_completo TEXT NOT NULL,
            data_nascimento DATE,
            diagnostico TEXT
        );
    """)
    print("Tabela 'Pacientes' criada com sucesso!")
except sqlite3.OperationalError:
    print("A tabela 'Pacientes' já existe.")


# --- ETAPA INSERT ---
# 3. Executar o comando INSERT para adicionar dados
# IMPORTANTE: Usar '?' previne um tipo de ataque chamado SQL Injection. É a forma segura de fazer!
pacientes_para_inserir = [
    ('João da Silva', '15-05-2018', 'TEA'),
    ('Pedro Marques', '15-05-2018', 'TEA'),
    ('Ana da Costa', '15-05-2018', 'Não TEA'),
    ('Maria Oliveira', '20-02-2019', 'Não TEA')
]

# cursor.executemany() insere vários registros de uma vez
cursor.executemany("""
    INSERT INTO Pacientes (nome_completo, data_nascimento, diagnostico)
    VALUES (?, ?, ?);
""", pacientes_para_inserir)

# 4. Salvar (commit) as alterações no banco de dados
# O commit é necessário para INSERT, UPDATE e DELETE
conexao.commit()
print(f"{cursor.rowcount} pacientes inseridos com sucesso.")


# --- ETAPA SELECT ---
# 5. Executar o comando SELECT para consultar os dados
print("\nConsultando todos os pacientes:")
cursor.execute("SELECT * FROM Pacientes;")

# 6. Buscar os resultados e exibi-los
# cursor.fetchall() busca todas as linhas retornadas pela consulta
todos_pacientes = cursor.fetchall()

for paciente in todos_pacientes:
    print(paciente)


# --- FINALIZAÇÃO ---
# 7. Fechar a conexão com o banco de dados
conexao.close()
print("\nConexão com o banco de dados fechada.")

