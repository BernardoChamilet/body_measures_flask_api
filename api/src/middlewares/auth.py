from functools import wraps
import jwt
from flask import request, jsonify, g
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
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            g.user_id = payload.get('user_id')
        except jwt.ExpiredSignatureError:
            # Token expirado
            return jsonify({'erro': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            #token inválido
            return jsonify({'erro': 'Token inválido'}), 401
        
        # Continua para a função
        return f(*args, **kwargs)
    return decorator