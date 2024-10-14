from flask import Blueprint
import src.controllers.usuario as controllers
from src.middlewares.auth import validarToken

usuario_bp = Blueprint('usuarios', __name__)

# Rota de buscar usuário pelo id
@usuario_bp.route("/usuarios/<id>", methods=('GET',))
def buscarUsuario(id):
    return controllers.buscarUsuario(id)

# Rota de buscar todos usuários
@usuario_bp.route("/usuarios", methods=('GET',))
def buscarUsuarios():
    return controllers.buscarUsuarios()

# Rota de criar usuário
@usuario_bp.route("/usuarios", methods=('POST',))
def criarUsuario():
    return controllers.criarUsuario()

# Rota de atualizar dados exceto senha de usuário
@usuario_bp.route("/usuarios/<id>", methods=("PUT",))
@validarToken
def atualizarUsuario(id):
    return controllers.atualizarUsuario(id)

# Rota de atualizar senha de um usuário
@usuario_bp.route("/usuarios/<id>/atualizar-senha", methods=("PATCH",))
@validarToken
def atualizarSenha(id):
    return controllers.atualizarSenha(id)

# Rota de deletar usuário
@usuario_bp.route("/usuarios/<id>", methods=('DELETE',))
@validarToken
def deletarUsuario(id):
    return controllers.deletarUsuario(id)   