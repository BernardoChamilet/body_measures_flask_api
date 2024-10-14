from flask import Blueprint
import src.controllers.medida as controllers
from src.middlewares.auth import validarToken

medida_bp = Blueprint('medidas', __name__)

# Rota de buscar todas medidas de um usuário
@medida_bp.route("/medidas", methods=('GET',))
@validarToken
def buscarMedidas():
    return controllers.buscarMedidas()

# Rota de buscar medida pelo id
@medida_bp.route("/medidas/<id>", methods=('GET',))
@validarToken
def buscarMedida(id):
    return controllers.buscarMedida(id)

# Rota de criar medida
@medida_bp.route("/medidas", methods=('POST',))
@validarToken
def inserirMedida():
    return controllers.inserirMedida()

# Rota de atualizar medida
@medida_bp.route("/medidas/<id>", methods=('PUT',))
@validarToken
def atualizarMedida(id):
    return controllers.atualizarMedida(id)

# Rota de deletar medida
@medida_bp.route("/medidas/<id>", methods=('DELETE',))
@validarToken
def deletarMedida(id):
    return controllers.deletarMedida(id)
