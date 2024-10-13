from flask import Flask

from src.config.config import secret_key, debug

app = Flask(__name__)

app.config['DEBUG'] = bool(debug)
app.secret_key = secret_key

from src.routes.usuario import usuario_bp
app.register_blueprint(usuario_bp)

from src.routes.medida import medida_bp
app.register_blueprint(medida_bp)

if __name__ == '__main__':
    app.run()