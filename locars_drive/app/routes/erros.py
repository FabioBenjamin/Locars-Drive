from flask import render_template, Blueprint

erros_bp = Blueprint('erros', __name__)

@erros_bp.app_errorhandler(400)
def requisicao_invalida(error):
    return render_template('erros/400.html'), 400

@erros_bp.app_errorhandler(401)
def nao_autorizado(error):
    return render_template('erros/401.html'), 401

@erros_bp.app_errorhandler(403)
def acesso_proibido(error):
    return render_template('erros/403.html'), 403

@erros_bp.app_errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('erros/404.html'), 404

@erros_bp.app_errorhandler(500)
def erro_interno_do_servidor(error):
    return render_template('erros/500.html'), 500
