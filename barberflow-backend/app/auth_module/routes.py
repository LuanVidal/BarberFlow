from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400
        
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']), # Segurança!
        is_admin=data.get('is_admin', False)
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        # Em um app real, aqui retornaríamos um Token JWT.
        # Para o trabalho acadêmico, retornar o ID do usuário basta.
        return jsonify({"message": "Login realizado", "user_id": user.id}), 200
        
    return jsonify({"error": "Credenciais inválidas"}), 401