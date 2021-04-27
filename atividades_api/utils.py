from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Roberta', idade=32)
    print(pessoa)
    pessoa.save()


# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    # print(pessoa.nome)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Roberta').first()
    pessoa.idade = 37
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Roberta').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    insere_usuario('rafael', '123')
    insere_usuario('roberta', '321')
    consulta_todos_usuarios()
    #insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()