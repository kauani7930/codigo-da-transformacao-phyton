# 1) Lista de compras 
# Programa que permite adicionar, remover e visualizar itens dinamicamente

lista_compras = [] # Lista vazia no início

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        lista_compras.append(item) # Adiciona no final da lista
        print(f"{item} adicionado à lista.")

    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item) # Remove se existir
            print(f"{item} removido da lista.")
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        print("Lista de compras:", lista_compras)

    elif opcao == "4":
        print("Encerrando lista de compras...")
        break

    else:
        print("Opção inválida! Tente novamente.")

print("\n")

# ===== 2) Armazenar dados de um aluno =====
# Dicionário com nome, idade e notas

aluno = {
    "nome": input("Digite o nome do aluno: "),
    "idade": int(input("Digite a idade do aluno: ")),
    "notas": []
}

# Adiciona 3 notas
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    aluno["notas"].append(nota)

# Exibe os dados do dicionário
print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("\n")

# ===== 3) Separar pares e ímpares =====
# Percorre um conjunto de números e exibe separadamente

numeros = [int(x) for x in input("Digite números separados por espaço: ").split()]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)

print("\n")

# ===== 4) Desafio Extra – Sistema de contatos =====
# Armazena contatos em um dicionário (nome → telefone)

contatos = {}

while True:
    print("\n--- MENU DE CONTATOS ---")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar contatos")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Nome do contato: ")
        telefone = input("Número de telefone: ")
        contatos[nome] = telefone
        print("Contato adicionado.")

    elif escolha == "2":
        nome = input("Nome do contato para remover: ")
        if nome in contatos:
            del contatos[nome]
            print("Contato removido.")
        else:
            print("Contato não encontrado.")

    elif escolha == "3":
        nome = input("Nome do contato para buscar: ")
        if nome in contatos:
            print(f"{nome}: {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif escolha == "4":
        if contatos:
            print("Lista de contatos:")
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum contato cadastrado.")

    elif escolha == "5":
        print("Encerrando sistema de contatos...")
        break

    else:
        print("Opção inválida! Tente novamente.")
