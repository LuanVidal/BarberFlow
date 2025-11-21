from . import db
from datetime import datetime

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'duration': self.duration}

class Barber(db.Model):
    __tablename__ = 'barbers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) # Senha criptografada
    is_admin = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'is_admin': self.is_admin}

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False) # Data e Hora
    status = db.Column(db.String(20), default='Agendado') # Agendado, Cancelado, Concluido
    
    # Chaves Estrangeiras (Relacionamentos)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    barber_id = db.Column(db.Integer, db.ForeignKey('barbers.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'date_time': self.date_time.isoformat(),
            'status': self.status,
            'user_id': self.user_id,
            'barber_id': self.barber_id,
            'service_id': self.service_id
        }