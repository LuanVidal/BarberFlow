import pytest
from app import create_app, db
from config import TestingConfig

@pytest.fixture
def app():
    # Cria a aplicação em modo de teste (Banco em memória)
    app = create_app(TestingConfig)
    
    with app.app_context():
        db.create_all()  # Cria as tabelas
        yield app        # Roda os testes
        db.session.remove()
        db.drop_all()    # Limpa tudo depois

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()