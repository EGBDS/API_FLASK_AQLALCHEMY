from models import Pessoas, Usuarios

#insere daddos na tebaela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Erick', idade=25)
    print(pessoa)
    pessoa.save()

# realiza consulta na tabela pessoa


def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Erick').first()
    print(pessoa.idade)

# altera dados na tabela pessoa


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Erick').first()
    pessoa.nome = 'João'
    pessoa.save()

# exclui dados na tabela pessoa


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Erick').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('rafael', '1234')
    insere_usuario('galleani', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta()
