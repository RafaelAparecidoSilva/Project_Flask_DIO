from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id': '0', 'nome': 'Rafael', 'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Silva', 'habilidade': ['Python', 'Django']}
]


# Retorna um desenvolvedor pelo ID; também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'Mensagem': f'Desenvolvedor com id n° {id} não existe.'}
        except Exception:
            response = {'status': 'Erro', 'Mensagem': 'Erro desconhecido, procure o administrador da API'}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Deletado com sucesso!!!'})


# Lista todos desenvolvedores e permite registrar um novo
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
