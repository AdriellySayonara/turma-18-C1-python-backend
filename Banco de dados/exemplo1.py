import sqlite3


conexao = sqlite3.connect('pesquisa.db')
cursor = conexao.cursor()

# Comando para atualizar o diagnóstico do paciente com nome 'João da Silva'
cursor.execute("""
    UPDATE Pacientes
    SET diagnostico = 'TEA Nível 1'
    WHERE nome_completo = 'João da Silva';
""")

conexao.commit()

print(f"{cursor.rowcount} registro atualizado com sucesso.")

# Comando para deletar o paciente com nome 'Maria Oliveira'
cursor.execute("""
    DELETE FROM Pacientes
    WHERE nome_completo = 'Maria Oliveira';
""")

conexao.commit()

print(f"{cursor.rowcount} registro excluído com sucesso.")

conexao.close()