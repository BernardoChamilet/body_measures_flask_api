from flask import jsonify, request, g
import src.repositories.medida as repositories
import src.models.medida as models
from pydantic import ValidationError

# buscarMedidas busca todas medidas de um usuário
def buscarMedidas():
    # Pegando id do token
    id_logado = g.user_id
    # Chamando banco de dados para buscar medidas
    medidas, erro = repositories.buscarMedidas(id_logado)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if medidas != None:
        # Sucesso, buscou medidas
        return jsonify(medidas), 200
    # Sucesso, não tem medidas
    return '', 204
    
# buscarMedida busca uma medida por seu id
def buscarMedida(id):
    # Chamando banco de dados para buscar medida
    medida, erro = repositories.buscarMedida(id)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro":erro}), 500
    if medida != None:
        # Sucesso, retornou medida
        return jsonify(medida), 200
    # Sucesso, não tem medida
    return '', 204
    
# inserirMedida cria uma nova medida de um usuário 
def inserirMedida():
    # Pegando id do token
    id_logado = g.user_id
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
    # Pegando id do token
    id_logado = g.user_id
    # Chamando banco de dados para buscar o dono da medida
    dono_id, erro = repositories.buscarDono(id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if dono_id == None:
        # Erro, nenhuma medida com esse id
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    if id_logado != dono_id:
        # Erro, não autorizado a atualizar a medida
        return jsonify({"erro": "Somente pode atualizar as próprias medidas"}), 403
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
    if linhasAtualizadas == 0:
        # Erro, nenhuma medida com esse id
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    # Sucesso, no content
    return '', 204

# deletarMedida deleta uma medida    
def deletarMedida(id):
    # Pegando id do token
    id_logado = g.user_id
    # Chamando banco de dados para buscar o dono da medida
    dono_id, erro = repositories.buscarDono(id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if dono_id == None:
        # Erro, nenhuma medida com esse id
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    if id_logado != dono_id:
        # Erro, não autorizado a deletar a medida
        return jsonify({"erro": "Somente pode deletar as próprias medidas"}), 403
    # Chamando banco de dados para deletar medida
    linhasDeletadas, erro = repositories.deletarMedida(id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if linhasDeletadas == 0:
        # Erro, medidad não encontrada
        return jsonify({"erro":"Nenhuma medida com esse id encontrada"}), 404
    # Sucesso, retorna id da medida deletada
    return jsonify({"id":id}), 200