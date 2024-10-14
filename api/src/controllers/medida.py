from flask import jsonify, request
import src.repositories.medida as repositories
import src.models.medida as models
from pydantic import ValidationError

# buscarMedidas busca todas medidas de um usuário
def buscarMedidas():
    # Pegar id do token
    id_logado = 1
    # Chamando banco de dados para buscar medidas
    medidas, erro = repositories.buscarMedidas(id_logado)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro": erro}), 500
    elif medidas != None:
        # Sucesso, buscou medidas
        return jsonify(medidas), 200
    else:
        # Sucesso, não tem medidas
        return '', 204
    
# buscarMedida busca uma medida por seu id
def buscarMedida(id):
    # Chamando banco de dados para buscar medida
    medida, erro = repositories.buscarMedida(id)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro":erro}), 500
    elif medida != None:
        # Sucesso, retornou medida
        return jsonify(medida), 200
    else:
        # Sucesso, não tem medida
        return '', 204
    
# inserirMedida cria uma nova medida de um usuário 
def inserirMedida():
    #Pegar id do token
    id_logado = 1
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando campos
    try:
        medidas = models.Medida(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Chamando banco de dados para inserir medidas
    idMedida, erro = repositories.inserirMedida(medidas.model_dump(), id_logado)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    # Sucesso, retornar id da medida inserida
    return jsonify({"id": idMedida}), 201

# atualizarMedida atualiza dados de uma medida
def atualizarMedida(id):
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando dados
    try:
        medida = models.Medida(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Chamando banco de dados para atualizar dados
    linhasAtualizadas, erro = repositories.atualizarMedida(medida.model_dump(), id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    elif linhasAtualizadas == 0:
        # Erro, nenhuma medida com esse id
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    else:
        # Sucesso, no content
        return '', 204
    
# deletarMedida deleta uma medida    
def deletarMedida(id):
    # Chamando banco de dados para deletar medida
    linhasDeletadas, erro = repositories.deletarMedida(id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    elif linhasDeletadas == 0:
        # Erro, medidad não encontrada
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    else:
        # Sucesso, retorna id da medida deletada
        return jsonify({"id":id}), 200