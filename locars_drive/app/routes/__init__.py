from flask import Blueprint

# Importar blueprints dos módulos
from app.routes.index import index_bp

blueprints = [
    index_bp,
]
