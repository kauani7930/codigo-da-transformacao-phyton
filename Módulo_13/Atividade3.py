from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Função para criar tabela
def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário cadastrado no banco com sucesso!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
