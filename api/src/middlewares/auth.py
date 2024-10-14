from functools import wraps
import jwt
from flask import request, jsonify
from src.config.config import secret_key

# Decorator para validar o token
def validarToken(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # Verifica se o token foi passado no header Authorization
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]  # Espera o formato: 'Bearer <token>'
        else:
            return jsonify({'erro': 'Token faltando'}), 401
        try:
            # Decodifica e valida o token
            _ = jwt.decode(token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # Token expirado
            return jsonify({'erro': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            #token inválido
            return jsonify({'erro': 'Token expirado'}), 401
        
        # Continua para a função
        return f(*args, **kwargs)
    return decorator