from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Barber

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # LOG NO TERMINAL DO PYTHON
    print(f"--- NOVA TENTATIVA DE CADASTRO ---")
    print(f"Dados recebidos: {data}")

    if User.query.filter_by(email=data['email']).first():
        print("Erro: Email já existe!")
        return jsonify({"error": "Email já cadastrado"}), 400
        
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        is_admin=data.get('is_admin', False)
    )
    
    try:
        db.session.add(user)
        db.session.commit()
        print(f"SUCESSO: Usuário {user.name} (ID: {user.id}) salvo no banco!") # Confirmação
        return jsonify(user.to_dict()), 201
    except Exception as e:
        print(f"ERRO DE BANCO: {e}")
        return jsonify({"error": "Erro ao salvar no banco"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 1. Tenta achar na tabela de USUÁRIOS (Clientes)
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({
            "message": "Login realizado",
            "user_id": user.id,
            "name": user.name,
            "role": "client" # <--- Importante
        }), 200

    # 2. Se não achou ou senha errada, tenta na tabela de BARBEIROS
    barber = Barber.query.filter_by(email=email).first()
    # Nota: O model Barber tem o método check_password que criamos antes
    if barber and barber.check_password(password):
        return jsonify({
            "message": "Login realizado",
            "user_id": barber.id,
            "name": barber.name,
            "role": "barber" # <--- Importante
        }), 200

    # 3. Se não achou em lugar nenhum
    return jsonify({"error": "E-mail ou senha incorretos"}), 401