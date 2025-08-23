import json

clientes = {
    "1": {"nome": "Emily", "idade": 19},
    "2": {"nome": "Joyce", "idade": 21},
    "3": {"nome": "Rita", "idade": 20}
}

with open("clientes.json", "w") as f:
    json.dump(clientes, f, indent=4)

with open("clientes.json", "r") as f:
    dados = json.load(f)
    print("\n=== Clientes em JSON ===")
    print(dados)
