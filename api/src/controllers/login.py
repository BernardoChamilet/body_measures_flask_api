from flask import jsonify, request
import src.repositories.usuario as repositories
import src.models.usuario as models
from flask_bcrypt import Bcrypt
from pydantic import ValidationError
from datetime import datetime, timedelta, timezone
import jwt
from src.config.config import secret_key

bcrypt = Bcrypt()

# login faz o login de um usuário
def login():
    # Lendo corpo da requisição
    dados = request.get_json()
    # Validando dados
    try:
        login = models.Login(**dados)
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    usuario = login.usuario
    # Chamando banco de dados para buscar senha do usuário
    senhaSalva, user_id, erro = repositories.buscarSenhaEIDPeloUser(usuario)
    if erro != None:
        # Erro interno do servidor de banco de dados
        return jsonify({"erro": erro}), 500
    elif senhaSalva == None:
        # Erro, usuário incorreto
        return jsonify({"erro":"Usuário incorreto"}), 401
    else:
        senha = login.senha
        if bcrypt.check_password_hash(senhaSalva, senha):
            # Senha correta: gerando token
            expiration = datetime.now(timezone.utc) + timedelta(hours=2)  # Expira em 2 horas
            token = jwt.encode({'user_id': user_id, 'exp': expiration}, secret_key, algorithm='HS256')
            cookie_expiration = expiration - timedelta(minutes=2)
            return jsonify({"token":token, "expiration":cookie_expiration}), 200
        else:
            # Erro, senha incorreta
            return jsonify({"erro":"Senha incorreta"}), 401


