import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave_super_secreta'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///barberflow.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # Banco em memória para testes rápidos