from flask import Blueprint, request, jsonify
from app import db
from app.models import Service, Settings

services_bp = Blueprint('services', __name__)

# --- CONFIGURAÇÕES GERAIS (HORÁRIOS) ---
@services_bp.route('/settings', methods=['GET'])
def get_settings():
    config = Settings.query.first()
    if not config:
        # Cria padrão se não existir
        config = Settings()
        db.session.add(config)
        db.session.commit()
    return jsonify(config.to_dict()), 200

@services_bp.route('/settings', methods=['PUT'])
def update_settings():
    data = request.get_json()
    config = Settings.query.first()
    if not config:
        config = Settings()
        db.session.add(config)
    
    config.open_time = data.get('open_time', '08:00')
    config.close_time = data.get('close_time', '18:00')
    config.lunch_start = data.get('lunch_start', '12:00')
    config.lunch_end = data.get('lunch_end', '13:00')
    
    db.session.commit()
    return jsonify(config.to_dict()), 200

# --- SERVIÇOS (JÁ EXISTIA, SÓ GARANTINDO O UPDATE) ---
@services_bp.route('/', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([s.to_dict() for s in services]), 200

@services_bp.route('/', methods=['POST'])
def create_service():
    data = request.get_json()
    new_service = Service(name=data['name'], price=data['price'], duration=data.get('duration', 30))
    db.session.add(new_service)
    db.session.commit()
    return jsonify(new_service.to_dict()), 201

# Nova rota para ATUALIZAR preço/duração
@services_bp.route('/<int:id>', methods=['PUT'])
def update_service(id):
    data = request.get_json()
    service = Service.query.get(id)
    if not service: return jsonify({"error": "Serviço não encontrado"}), 404
    
    service.price = data['price']
    service.duration = data['duration']
    db.session.commit()
    return jsonify(service.to_dict()), 200