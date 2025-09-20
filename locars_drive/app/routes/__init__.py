from flask import Blueprint

# Importar blueprints dos módulos
from app.routes.index import index_bp
from app.routes.erros import erros_bp

blueprints = [
    index_bp,
    erros_bp,
]
