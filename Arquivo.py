import csv

notas = [
    ["Nome", "Nota"],
    ["Emily", 8.7],
    ["Joyce", 7.9],
    ["Rita", 9.3]
]

with open("notas.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(notas)

with open("notas.csv", "r") as f:
    leitor = csv.reader(f)
    print("\n=== Notas dos Alunos ===")
    for linha in leitor:
        print(linha)
