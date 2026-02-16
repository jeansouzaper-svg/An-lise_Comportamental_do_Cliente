# %%
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
""")
            
conexao.commit()
conexao.close()

print("Banco de dados e tabela verificados com sucesso!")

# %%
