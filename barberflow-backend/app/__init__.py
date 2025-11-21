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

    # Registrar Blueprints Existentes
    from app.services_module.routes import services_bp
    app.register_blueprint(services_bp, url_prefix='/api/services')

    from app.barbers_module.routes import barbers_bp
    app.register_blueprint(barbers_bp, url_prefix='/api/barbers')

    # --- NOVOS REGISTROS ---
    from app.auth_module.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from app.appointments_module.routes import appointments_bp
    app.register_blueprint(appointments_bp, url_prefix='/api/appointments')
    
    return app