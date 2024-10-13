from flask import jsonify, request
import src.repositories.medida as repositories
import src.models.medida as models

# buscarMedidas busca todas medidas de um usuário
def buscarMedidas():
    # Pegar id do token
    id_logado = 1
    medidas, erro = repositories.buscarMedidas(id_logado)
    if erro != None:
        return jsonify({"erro": erro}), 500
    elif medidas != None:
        return jsonify(medidas), 200
    else:
        return '', 204
    
# buscarMedida busca uma medida por seu id
def buscarMedida(id):
    medida, erro = repositories.buscarMedida(id)
    if erro != None:
        return jsonify({"erro":erro}), 500
    elif medida != None:
        return jsonify(medida), 200
    else:
        return '', 204
    
# inserirMedida cria uma nova medida de um usuário 
def inserirMedida():
    #Pegar id do token
    id_logado = 1
    dados = request.get_json()
    try:
        medidas = models.Medida(**dados)
    except:
        return jsonify({"erro": 'bad request'}), 400
    idMedida, erro = repositories.inserirMedida(medidas.model_dump(), id_logado)
    if erro != None:
        return jsonify({"erro": erro}), 500
    return jsonify({"id": idMedida}), 201

# atualizarMedida atualiza dados de uma medida
def atualizarMedida(id):
    dados = request.get_json()
    try:
        medida = models.Medida(**dados)
    except:
        return jsonify({"erro": 'bad request'}), 400
    linhasAtualizadas, erro = repositories.atualizarMedida(medida.model_dump(), id)
    if erro != None:
        return jsonify({"erro": erro}), 500
    elif linhasAtualizadas == 0:
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 400
    else:
        return '', 204
    
# deletarMedida deleta uma medida    
def deletarMedida(id):
    linhasDeletadas, erro = repositories.deletarMedida(id)
    if erro != None:
        return jsonify({"erro": erro}), 500
    elif linhasDeletadas == 0:
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 400
    else:
        return jsonify({"id":id}), 200