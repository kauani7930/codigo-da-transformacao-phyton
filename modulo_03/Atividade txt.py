with open("dados.txt", "w") as f:
    f.write("Este é um teste de escrita em arquivo.\n")
    f.write("Segunda linha de texto.")

with open("dados.txt", "r") as f:
    conteudo = f.read()
    print("=== Conteúdo do TXT ===")
    print(conteudo)
