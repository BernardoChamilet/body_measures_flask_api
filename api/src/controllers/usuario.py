from flask import jsonify, request, g
import src.repositories.usuario as repositories
import src.models.usuario as models
from flask_bcrypt import Bcrypt
from pydantic import ValidationError

bcrypt = Bcrypt()

# buscarUsuario busca dados não sensíveis de um usuário
def buscarUsuario(id):
    # Chamando banco de dados para buscar usuario
    usuario, erro = repositories.buscarUsuario(id)
    if erro != None:
        # Erro interno de banco de dados
        return jsonify({"erro": erro}), 500
    if usuario != None:
        # Sucesso, usuario encontrado
        return jsonify(usuario), 200
    # Sucesso, usuario não encontrado
    return '', 204
    
# buscarUsuario busca dados não sensíveis de um usuário logado
def buscarUsuarioLogado():
    id = g.user_id
    # Chamando banco de dados para buscar usuario
    usuario, erro = repositories.buscarUsuario(id)
    if erro != None:
        # Erro interno de banco de dados
        return jsonify({"erro": erro}), 500
    if usuario != None:
        # Sucesso, usuario encontrado
        return jsonify(usuario), 200
    # Sucesso, usuario não encontrado
    return '', 204
    
# buscarUsuarios busca dados não sensíveis de todos usuários
def buscarUsuarios():
    # Chamando banco de dados para buscar usuários
    usuarios, erro = repositories.buscarUsuarios()
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if usuarios != None:
        # Sucesso, usuarios encontrados
        return jsonify(usuarios), 200
    # Sucesso, no content
    return '', 204

# criarUsuario cria um novo usuário
def criarUsuario():
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando dados
    try:
        usuario = models.Usuario(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Encriptografando senha
    usuarioDict = usuario.model_dump()
    usuarioDict["senha"] = bcrypt.generate_password_hash(usuarioDict["senha"]).decode('utf-8')
    # Chamando banco de dados para criar usuário
    usuarioID, erro = repositories.criarUsuario(usuarioDict)
    if erro != None:
        if erro == 409:
            # Erro, usuário já existe
            return jsonify({"erro": "Usuário já existe"}), 409
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    # Sucesso, retorna id do usuário criado
    return jsonify({"id": usuarioID}), 201

# atualizarUsuario atualiza campos de um usuário exceto senha
def atualizarUsuario(id):
    # Pegando id do token para comparar com id passado
    token_id = g.user_id
    if token_id != id:
        # Erro: somente pode atualizar os próprios dados
        return jsonify({"erro":"Somente pode atualizar os próprios dados"}), 403 
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando dados
    try:
        usuario = models.Usuario(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Chamando banco de dados para atualizar dados
    linhasAtualizadas, erro = repositories.atualizarUsuario(usuario.model_dump(), id)
    if erro != None:
        if erro == 409:
            # Erro, usuário já existe
            return jsonify({"erro": "Usuário já existe"}), 409
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if linhasAtualizadas == 0:
        # Erro, nenhum usuario com esse id
        return jsonify({"erro":"Nenhum usuário com esse id encontrado"}), 404
    # Sucesso, no content
    return '', 204

# atualizarSenha atualizar a senha de um usuário
def atualizarSenha(id):
    # Pegando id do token para comparar com id passado
    token_id = g.user_id
    if token_id != id:
        # Erro: somente pode atualizar os próprios dados
        return jsonify({"erro":"Somente pode atualizar os próprios dados"}), 403
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando dados
    try:
        senhas = models.Senhas(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    # Chamando banco de dados para buscar senha do usuário
    senhaSalva, erro = repositories.buscarSenha(id)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if senhaSalva == None:
        # Erro, nenhum usuário com esse id
        return jsonify({"erro":"Nenhum usuário com esse id encontrado"}), 404
    # Vendo se senha atual digitada está correta
    senhaAtual = senhas.senha_atual
    if bcrypt.check_password_hash(senhaSalva, senhaAtual):
        senhaNova = senhas.senha_nova
        # Vendo se senha nova e salva são iguais
        if bcrypt.check_password_hash(senhaSalva, senhaNova):
            # Erro, enha nova e atuais são iguais
            return jsonify({"erro": "Nova senha não pode ser igual a senha atual"}), 400
        # Criptografando senha nova
        senhaNova = bcrypt.generate_password_hash(senhaNova).decode('utf-8')
        # Chamando banco de dados para atualizar senha
        linhasAtualizadas, erro = repositories.atualizarSenha(senhaNova, id)
        if erro != None:
            # Erro interno de servidor de banco de dados
            return jsonify({"erro": erro}), 500
        if linhasAtualizadas == 0:
            # Erro, nenhum usuário com id passado
            return jsonify({"erro":"Nenhum usuário com esse id encontrado"}), 404
        # Sucesso, no content
        return '', 204
    else:
        # Erro, senha digitada incorretas
        return jsonify({"erro":"Senha atual incorreta"}), 400


# deletarUsuario deleta um usuario    
def deletarUsuario(id):
    # Pegando id do token para comparar com id passado
    token_id = g.user_id
    if token_id != id:
        # Erro: somente pode atualizar os próprios dados
        return jsonify({"erro":"Somente pode deletar a prórpria conta"}), 403
    # Chamando banco de dados para deletar usuário
    linhasDeletadas, erro = repositories.deletarUsuario(id)
    if erro != None:
        # Erro interno de servidor de banco de dados
        return jsonify({"erro": erro}), 500
    if linhasDeletadas == 0:
        # Erro, nenhum usuário com esse id
        return jsonify({"erro":"Nenhum usuário com esse id encontrado"}), 404
    # Sucesso, retorna id do usuário apagado
    return jsonify({"id":id}), 200