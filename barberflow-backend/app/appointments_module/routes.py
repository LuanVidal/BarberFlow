from flask import Blueprint, request, jsonify
from app import db
from app.models import Appointment
from datetime import datetime

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/', methods=['POST'])
def create_appointment():
    data = request.get_json()
    
    try:
        # Converte string para data
        dt = datetime.fromisoformat(data['date_time'])
        
        # Aqui poderíamos verificar se o horário já está ocupado (Lógica extra)
        
        appt = Appointment(
            user_id=data['user_id'],
            barber_id=data['barber_id'],
            service_id=data['service_id'],
            date_time=dt
        )
        
        db.session.add(appt)
        db.session.commit()
        return jsonify(appt.to_dict()), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@appointments_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_appointments(user_id):
    appts = Appointment.query.filter_by(user_id=user_id).all()
    return jsonify([a.to_dict() for a in appts]), 200