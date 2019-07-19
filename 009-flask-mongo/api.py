from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
import random

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/fbta'
mongo = PyMongo(app)

@app.route("/", methods=['POST'])
def cadastrar():
    livro = request.json
    resultado = mongo.db.livros.insert_one(livro)
    livro['id'] = str(livro['_id'])
    del livro['_id']
    return jsonify(livro)

@app.route("/<codigo>", methods=['GET'])
def recuperar(codigo):
    livro = mongo.db.livros.find_one({'_id': ObjectId(codigo)})
    livro['id'] = str(livro['_id'])
    del livro['_id']
    return jsonify(livro)

@app.route("/sorteio")
def sorteio():
    alunos = ['A', 'B', 'C']
    escolhido = random.choice(alunos)
    return jsonify(escolhido)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
