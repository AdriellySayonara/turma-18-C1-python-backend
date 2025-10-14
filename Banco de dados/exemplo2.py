import sqlite3

# --- 1. SETUP DA CONEXÃO E TABELA ---
conexao = sqlite3.connect('pesquisa1.db')
cursor = conexao.cursor()

# Tenta criar a tabela com a restrição UNIQUE no nome_completo
try:
    cursor.execute("""
        CREATE TABLE Pacientes (
            paciente_id INTEGER PRIMARY KEY, 
            nome_completo TEXT NOT NULL UNIQUE, -- Garante que cada nome seja único
            data_nascimento DATE,
            diagnostico TEXT
        );
    """)
    print("Tabela 'Pacientes' criada com sucesso!")
except sqlite3.OperationalError:
    print("A tabela 'Pacientes' já existe.")

# --- 2. INSERÇÃO SEGURA DOS DADOS INICIAIS ---
# Insere os dados apenas se eles não existirem, evitando duplicação
pacientes_para_inserir = [
    ('João da Silva', '15-05-2018', 'TEA'),
    ('Maria Oliveira', '20-02-2019', 'Controle')
]

for paciente in pacientes_para_inserir:
    try:
        cursor.execute("""
            INSERT INTO Pacientes (nome_completo, data_nascimento, diagnostico)
            VALUES (?, ?, ?);
        """, paciente)
        print(f"Paciente '{paciente[0]}' inserido com sucesso.")
    except sqlite3.IntegrityError:
        # Este erro ocorre se tentarmos inserir um nome que já existe (por causa do UNIQUE)
        print(f"Paciente '{paciente[0]}' já existe no banco. Inserção ignorada.")

print("\n--- Estado da tabela ANTES da manipulação ---")
cursor.execute("SELECT * FROM Pacientes;")
for linha in cursor.fetchall():
    print(linha)

# --- 3. MANIPULAÇÃO DOS DADOS (UPDATE E DELETE) ---
print("\n--- Executando UPDATE e DELETE ---")

# Atualiza o diagnóstico do João
cursor.execute("""
    UPDATE Pacientes
    SET diagnostico = 'TEA Nível 1'
    WHERE nome_completo = 'João da Silva';
""")
print(f"{cursor.rowcount} registro atualizado.")

# Deleta a Maria
cursor.execute("""
    DELETE FROM Pacientes
    WHERE nome_completo = 'Maria Oliveira';
""")
print(f"{cursor.rowcount} registro excluído.")

# --- 4. VERIFICAÇÃO FINAL E FECHAMENTO ---
print("\n--- Estado FINAL da tabela APÓS a manipulação ---")
cursor.execute("SELECT * FROM Pacientes;")
todos_pacientes = cursor.fetchall()

for paciente in todos_pacientes:
    print(paciente)

# Salva TODAS as alterações feitas (inserts, updates, deletes)
conexao.commit()

# Fecha a conexão
conexao.close()
print("\nConexão com o banco de dados fechada.")