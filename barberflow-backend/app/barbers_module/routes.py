from flask import Blueprint, request, jsonify
from app import db
from app.models import Barber

barbers_bp = Blueprint('barbers', __name__)

@barbers_bp.route('/', methods=['GET'])
def get_barbers():
    # Retorna todos os barbeiros
    barbers = Barber.query.all()
    return jsonify([b.to_dict() for b in barbers]), 200

@barbers_bp.route('/', methods=['POST'])
def create_barber():
    # Cria um barbeiro novo (útil para testes)
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    if Barber.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400

    new_barber = Barber(name=data['name'], email=data['email'])
    
    # Se mandarem senha, a gente define
    if 'password' in data:
        new_barber.set_password(data['password'])
    
    db.session.add(new_barber)
    db.session.commit()

    return jsonify(new_barber.to_dict()), 201