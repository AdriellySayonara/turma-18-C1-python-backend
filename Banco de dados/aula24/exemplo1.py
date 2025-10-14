"""
===============================================
DEMONSTRAÇÃO DE JOINs EM SQLite3
===============================================

Objetivo:
    - Criar um banco de dados SQLite do zero.
    - Criar e popular as tabelas 'Alunos' e 'Cursos'.
    - Demonstrar os diferentes tipos de JOIN:
      INNER JOIN, LEFT JOIN, RIGHT JOIN (simulado) e FULL OUTER JOIN (simulado).
"""

import sqlite3
import os


# -------------------------------
# CONFIGURAÇÕES INICIAIS
# -------------------------------

DB_FILE = r"E:\turma-18-C1-python-backend\Banco de dados\aula24\exemplo1.db"


def imprimir_resultado(titulo, cursor):
    """Exibe os resultados de uma consulta SQL de forma formatada."""
    print("=" * 45)
    print(f"| RESULTADO PARA: {titulo.upper():<25} |")
    print("=" * 45)

    # Nomes das colunas
    colunas = [desc[0] for desc in cursor.description]
    print(f"{colunas[0]:<15} | {colunas[1]:<15}")
    print("-" * 35)

    # Exibir linhas formatadas (substitui None por 'NULL')
    for linha in cursor.fetchall():
        aluno = str(linha[0]) if linha[0] is not None else "NULL"
        curso = str(linha[1]) if linha[1] is not None else "NULL"
        print(f"{aluno:<15} | {curso:<15}")
    print("\n")


# -------------------------------
# BLOCO PRINCIPAL
# -------------------------------

def main():
    # Remove o banco anterior, se existir
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Banco de dados anterior '{DB_FILE}' removido.\n")

    # 1️⃣ Conexão com o banco
    conexao = sqlite3.connect(DB_FILE)
    cursor = conexao.cursor()
    print(f"Banco de dados '{DB_FILE}' criado com sucesso.\n")

    # 2️⃣ Criação e inserção de dados
    sql_setup = """
    DROP TABLE IF EXISTS Alunos;
    DROP TABLE IF EXISTS Cursos;

    CREATE TABLE Alunos (
        ID_Aluno INTEGER PRIMARY KEY,
        Nome_Aluno TEXT,
        ID_Curso INTEGER
    );

    CREATE TABLE Cursos (
        ID_Curso INTEGER PRIMARY KEY,
        Nome_Curso TEXT
    );

    INSERT INTO Alunos (ID_Aluno, Nome_Aluno, ID_Curso) VALUES
        (1, 'Ana', 101),
        (2, 'Bruno', 102),
        (3, 'Carla', 101),
        (4, 'Daniel', 'NULL');

    INSERT INTO Cursos (ID_Curso, Nome_Curso) VALUES
        (101, 'SQL'),
        (102, 'Python'),
        (103, 'Java');
    """

    cursor.executescript(sql_setup)
    conexao.commit()
    print("Tabelas 'Alunos' e 'Cursos' criadas e populadas.\n")

    # 3️⃣ Consultas JOIN

    # INNER JOIN
    cursor.execute("""
        SELECT Alunos.Nome_Aluno, Cursos.Nome_Curso
        FROM Alunos
        INNER JOIN Cursos ON Alunos.ID_Curso = Cursos.ID_Curso;
    """)
    imprimir_resultado("INNER JOIN", cursor)

    # LEFT JOIN
    cursor.execute("""
        SELECT Alunos.Nome_Aluno, Cursos.Nome_Curso
        FROM Alunos
        LEFT JOIN Cursos ON Alunos.ID_Curso = Cursos.ID_Curso;
    """)
    imprimir_resultado("LEFT JOIN", cursor)

    # RIGHT JOIN (Simulado com LEFT JOIN invertido)
    cursor.execute("""
        SELECT Alunos.Nome_Aluno, Cursos.Nome_Curso
        FROM Cursos
        LEFT JOIN Alunos ON Cursos.ID_Curso = Alunos.ID_Curso;
    """)
    imprimir_resultado("RIGHT JOIN (Simulado)", cursor)

    # FULL OUTER JOIN (Simulado com UNION)
    cursor.execute("""
        SELECT Alunos.Nome_Aluno, Cursos.Nome_Curso FROM Alunos
        LEFT JOIN Cursos ON Alunos.ID_Curso = Cursos.ID_Curso
        UNION
        SELECT Alunos.Nome_Aluno, Cursos.Nome_Curso FROM Cursos
        LEFT JOIN Alunos ON Cursos.ID_Curso = Alunos.ID_Curso;
    """)
    imprimir_resultado("FULL OUTER JOIN (Simulado)", cursor)

    # 4️⃣ Encerramento
    conexao.close()
    print("Demonstração concluída. Conexão com o banco de dados encerrada.")


# -------------------------------
# EXECUÇÃO DIRETA DO SCRIPT
# -------------------------------

if __name__ == "__main__":
    main()
