from flask import Blueprint
import src.controllers.medida as controllers

# [x] buscar medidas de um usuario
# [x] buscar medida por medida_id
# [x] criar medida
# [x] atualizar medida
# [ ] deletar medida

medida_bp = Blueprint('medidas', __name__)
 
@medida_bp.route("/medidas", methods=('GET',))
def buscarMedidas():
    return controllers.buscarMedidas()

@medida_bp.route("/medidas/<id>", methods=('GET',))
def buscarMedida(id):
    return controllers.buscarMedida(id)

@medida_bp.route("/medidas", methods=('POST',))
def inserirMedida():
    return controllers.inserirMedida()

@medida_bp.route("/medidas/<id>", methods=('PUT',))
def atualizarMedida(id):
    return controllers.atualizarMedida(id)

@medida_bp.route("/medidas/<id>", methods=('DELETE',))
def deletarMedida(id):
    return controllers.deletarMedida(id)