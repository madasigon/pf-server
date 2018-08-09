from .index import bp as index_bp
from .challenge import bp as challenge_bp

def register(app):
    app.register_blueprint(index_bp, url_prefix="/")
    app.register_blueprint(challenge_bp, url_prefix="/challenge")