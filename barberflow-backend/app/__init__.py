from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Registrar os Blueprints (Módulos)
    from app.services_module.routes import services_bp
    app.register_blueprint(services_bp, url_prefix='/api/services')

    with app.app_context():
        db.create_all() # Cria as tabelas se não existirem

    return app