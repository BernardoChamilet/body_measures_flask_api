from flask import Blueprint
import src.controllers.login as controllers

login_bp = Blueprint('login', __name__)

# Rota de login
@login_bp.route("/login", methods=('POST',))
def login():
    return controllers.login()