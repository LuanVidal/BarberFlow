from flask import Blueprint, request, jsonify
from app import db
from app.models import Appointment, User, Service
from datetime import datetime

appointments_bp = Blueprint('appointments', __name__)

# --- 1. CRIAR AGENDAMENTO (Com validação de conflito) ---
@appointments_bp.route('/', methods=['POST'])
def create_appointment():
    data = request.get_json()
    
    try:
        # Validação básica
        if not data or 'barber_id' not in data or 'date_time' not in data:
            return jsonify({"error": "Dados incompletos"}), 400

        dt = datetime.fromisoformat(data['date_time'])
        
        # Verifica se já existe agendamento ativo nesse horário
        conflito = Appointment.query.filter_by(
            barber_id=data['barber_id'], 
            date_time=dt,
            status='Agendado'
        ).first()

        if conflito:
            return jsonify({"error": "Horário ocupado!"}), 409
        
        appt = Appointment(
            user_id=data['user_id'],
            barber_id=data['barber_id'],
            service_id=data['service_id'],
            date_time=dt,
            status='Agendado'
        )
        
        db.session.add(appt)
        db.session.commit()
        return jsonify(appt.to_dict()), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# --- 2. CANCELAR AGENDAMENTO ---
@appointments_bp.route('/<int:id>', methods=['DELETE'])
def cancel_appointment(id):
    appt = Appointment.query.get(id)
    if not appt:
        return jsonify({"error": "Agendamento não encontrado"}), 404
    
    db.session.delete(appt)
    db.session.commit()
    return jsonify({"message": "Cancelado com sucesso"}), 200

# --- 3. VERIFICAR HORÁRIOS OCUPADOS (Para o filtro da Home) ---
@appointments_bp.route('/taken/<int:barber_id>/<string:date>', methods=['GET'])
def get_taken_slots(barber_id, date):
    # Busca todos os agendamentos daquele dia (filtro de string parcial)
    search = f"{date}%" 
    appts = Appointment.query.filter(
        Appointment.barber_id == barber_id,
        Appointment.date_time.like(search),
        Appointment.status == 'Agendado'
    ).all()
    
    # Retorna lista de horas: ['08:00', '14:30']
    taken = [a.date_time.strftime('%H:%M') for a in appts]
    return jsonify(taken), 200

# --- 4. BUSCAR POR CLIENTE (Histórico) ---
@appointments_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_appointments(user_id):
    appts = Appointment.query.filter_by(user_id=user_id).all()
    results = []
    for a in appts:
        service = Service.query.get(a.service_id)
        # Importa Barber aqui se necessário ou usa User se for tabela unificada
        # Assumindo que Barbeiro é um User ou está na tabela Barber:
        barber = User.query.get(a.barber_id) 
        if not barber:
             # Fallback caso use tabela separada de Barber
             from app.models import Barber
             barber = Barber.query.get(a.barber_id)

        res = a.to_dict()
        res['service_name'] = service.name if service else "Serviço"
        res['barber_name'] = barber.name if barber else "Barbeiro"
        results.append(res)
    return jsonify(results), 200

# --- 5. BUSCAR POR BARBEIRO (Agenda + Faturamento) ---
@appointments_bp.route('/barber/<int:barber_id>', methods=['GET'])
def get_barber_appointments(barber_id):
    appts = Appointment.query.filter_by(barber_id=barber_id).order_by(Appointment.date_time).all()
    
    results = []
    for a in appts:
        user = User.query.get(a.user_id)
        service = Service.query.get(a.service_id)
        
        results.append({
            "id": a.id,
            "date_time": a.date_time.isoformat(),
            "status": a.status,
            "client_name": user.name if user else "Cliente Desconhecido",
            "service_name": service.name if service else "Serviço Removido",
            "service_price": service.price if service else 0.0 # <--- IMPORTANTE PARA O GRÁFICO
        })

    return jsonify(results), 200