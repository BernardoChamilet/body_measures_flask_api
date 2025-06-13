from flask import Flask

from src.config.config import secret_key, debug

app = Flask(__name__)

# Carregando variáveis de ambiente
app.config['DEBUG'] = bool(debug)
app.secret_key = secret_key

# Adcionando rotas
from src.routes.login import login_bp
app.register_blueprint(login_bp)

from src.routes.usuario import usuario_bp
app.register_blueprint(usuario_bp)

from src.routes.medida import medida_bp
app.register_blueprint(medida_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0")