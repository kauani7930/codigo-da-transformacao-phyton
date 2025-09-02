from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    usuarios.append(dados)
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!", "usuarios": usuarios})

if __name__ == '__main__':
    app.run(debug=True)
