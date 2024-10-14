from flask import Blueprint
import src.controllers.usuario as controllers

# [x] buscar usuario 
# [x] buscar usuarios
# [x] criar usuario
# [x] atualizar usuario
# [ ] atualizar senha
# [x] deletar usuario

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route("/usuarios/<id>", methods=('GET',))
def buscarUsuario(id):
    return controllers.buscarUsuario(id)

@usuario_bp.route("/usuarios", methods=('GET',))
def buscarUsuarios():
    return controllers.buscarUsuarios()

@usuario_bp.route("/usuarios", methods=('POST',))
def criarUsuario():
    return controllers.criarUsuario()

@usuario_bp.route("/usuarios/<id>", methods=("PUT",))
def atualizarUsuario(id):
    return controllers.atualizarUsuario(id)

@usuario_bp.route("/usuarios/<id>/atualizar-senha", methods=("PATCH",))
def atualizarSenha(id):
    return controllers.atualizarSenha(id)

@usuario_bp.route("/usuarios/<id>", methods=('DELETE',))
def deletarUsuario(id):
    return controllers.deletarUsuario(id)   