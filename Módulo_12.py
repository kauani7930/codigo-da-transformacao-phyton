import sqlite3

# =========================
# Conexão com o banco
# =========================
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# =========================
# Criar tabela
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# =========================
# Funções CRUD
# =========================

def inserir_cliente(nome, email):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    print("Cliente adicionado com sucesso!")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    if clientes:
        print("\n Lista de Clientes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")
    else:
        print("Nenhum cliente cadastrado.")

def atualizar_email(id_cliente, novo_email):
    cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()
    print(" Email atualizado com sucesso!")

def excluir_cliente(id_cliente):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    print(" Cliente excluído com sucesso!")

# =========================
# Menu de operações
# =========================
def menu():
    while True:
        print("\n===== Sistema de Gerenciamento de Clientes =====")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar email")
        print("4 - Excluir cliente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            inserir_cliente(nome, email)

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            id_cliente = int(input("Digite o ID do cliente: "))
            novo_email = input("Digite o novo email: ")
            atualizar_email(id_cliente, novo_email)

        elif opcao == "4":
            id_cliente = int(input("Digite o ID do cliente a excluir: "))
            excluir_cliente(id_cliente)

        elif opcao == "0":
            print(" Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida, tente novamente.")

# =========================
# Rodar o sistema
# =========================
if __name__ == "__main__":
    menu()
    conexao.close()
