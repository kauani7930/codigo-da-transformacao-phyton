import json
import csv

def atividade1():
    with open("informacoes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Nome: Kau\n")
        arquivo.write("Idade: 17\n")
        arquivo.write("Curso: programação \n")

    with open("informacoes.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo TXT:")
        print(conteudo)

def atividade2():
    clientes = {
        "cliente1": {"nome": "Ana", "idade": 25},
        "cliente2": {"nome": "João", "idade": 30},
        "cliente3": {"nome": "Kau", "idade": 17}
    }

    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        print("Dicionário de clientes (JSON):")
        print(dados)

def atividade3():
    notas = [
        ["Nome", "Matemática", "Português", "Inglês"],
        ["Ana", 8, 9, 7],
        ["João", 6, 7, 8],
        ["Kau", 10, 9, 9]
    ]

    with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(notas)

    with open("notas.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        print("Notas dos alunos (CSV):")
        for linha in leitor:
            print(linha)

def menu():
    print("\nEscolha a atividade:")
    print("1 - Arquivo TXT")
    print("2 - Arquivo JSON")
    print("3 - Arquivo CSV")
    escolha = input("Digite o número da atividade: ")

    if escolha == "1":
        atividade1()
    elif escolha == "2":
        atividade2()
    elif escolha == "3":
        atividade3()
    else:
        print("Opção inválida")

if __name__ == "__main__":
    menu()
