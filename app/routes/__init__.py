from .auth import auth
from .homepage import homepage

def register_blueprints(app):
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(homepage, url_prefix='/homepage')
