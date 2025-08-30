
class SaldoInsuficienteError(Exception):
    pass

# 1 - Calculadora com try/except
def calculadora():
    print("\n--- Calculadora ---")
    try:
        a = float(input("Digite um número: "))
        b = float(input("Digite outro número: "))
        resultado = a / b
        print("Resultado da divisão:", resultado)
    except ZeroDivisionError:
        print("Erro: não pode dividir por zero")
    except:
        print("Erro: entrada inválida")

# 2 - Simulação bancária
def banco():
    print("\n--- Banco ---")
    saldo = 100  # saldo inicial
    print("Saldo inicial:", saldo)
    try:
        valor = float(input("Quanto deseja sacar? "))
        if valor > saldo:
            raise SaldoInsuficienteError
        saldo -= valor
        print("Saque realizado. Saldo agora:", saldo)
    except SaldoInsuficienteError:
        print("Erro: saldo insuficiente")
    except:
        print("Erro: valor inválido")

# 3 - Validação de idade
def validar_idade():
    print("\n--- Cadastro de Idade ---")
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0:
            print("Erro: idade deve ser positiva")
        else:
            print("Idade registrada:", idade)
    except:
        print("Erro: digite apenas números inteiros")

# Desafio Extra - Login simples
def login():
    print("\n--- Login ---")
    usuario_correto = "kau"
    senha_correta = "1234"
    tentativas = 0
    while tentativas < 3:
        u = input("Usuário: ")
        s = input("Senha: ")
        if u == usuario_correto and s == senha_correta:
            print("Login realizado com sucesso!")
            return
        else:
            print("Credenciais inválidas")
            tentativas += 1
    print("Muitas tentativas, tente mais tarde.")

# Desafio Prático - Cadastro simples
def cadastro():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
        if idade <= 0:
            print("Idade inválida")
            return
    except:
        print("Erro: idade inválida")
        return
    email = input("E-mail: ")
    if "@" not in email:
        print("E-mail inválido")
        return
    print("Usuário cadastrado com sucesso!")
    print("Nome:", nome, "| Idade:", idade, "| E-mail:", email)

# Menu principal
def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Calculadora")
        print("2 - Banco")
        print("3 - Validar idade")
        print("4 - Login")
        print("5 - Cadastro")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1":
            calculadora()
        elif op == "2":
            banco()
        elif op == "3":
            validar_idade()
        elif op == "4":
            login()
        elif op == "5":
            cadastro()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

menu()
