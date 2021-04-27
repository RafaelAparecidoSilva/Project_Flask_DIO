from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0', 'nome': 'Rafael', 'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Silva', 'habilidade': ['Python', 'Django']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Erro', 'Mensagem': f'Desenvolvedor com id n° {id} não existe.'}
        except Exception:
            response = {'status': 'Erro', 'Mensagem': 'Erro desconhecido, procure o administrador da API'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        deletado = desenvolvedores.pop(id)
        return {'status': f'Desenvolvedor(a) {deletado["nome"]} deletado(a) com sucesso!!!'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')


if __name__ == '__main__':
    app.run(debug=True)
