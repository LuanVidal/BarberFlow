from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DevelopmentConfig

# Inicializa o banco de dados
db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa plugins
    db.init_app(app)
    CORS(app) # Libera o acesso para o Angular

    # --- REGISTRO DE BLUEPRINTS (Módulos) ---
    # Importa dentro da função para evitar "ciclo de importação"
    
    # 1. Módulo de Serviços
    from app.services_module.routes import services_bp
    app.register_blueprint(services_bp, url_prefix='/api/services')

    # 2. Módulo de Barbeiros
    from app.barbers_module.routes import barbers_bp
    app.register_blueprint(barbers_bp, url_prefix='/api/barbers')

    # 3. Módulo de Autenticação (Login/Cadastro)
    from app.auth_module.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # 4. Módulo de Agendamentos
    from app.appointments_module.routes import appointments_bp
    app.register_blueprint(appointments_bp, url_prefix='/api/appointments')

    # Cria as tabelas do banco se não existirem
    with app.app_context():
        db.create_all()

    return app