from flask import Blueprint, request, jsonify
from app import db
from app.models import Service

services_bp = Blueprint('services', __name__)

@services_bp.route('/', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([s.to_dict() for s in services]), 200

@services_bp.route('/', methods=['POST'])
def create_service():
    data = request.get_json()
    
    # Validação básica
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    new_service = Service(
        name=data['name'],
        price=data['price'],
        duration=data.get('duration', 30)
    )

    db.session.add(new_service)
    db.session.commit()

    return jsonify(new_service.to_dict()), 201