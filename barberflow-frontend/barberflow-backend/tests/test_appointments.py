from datetime import datetime

def test_create_appointment(client):
    """Teste: Cliente deve conseguir agendar um horário."""
    # Setup: Precisa existir User, Barber e Service
    client.post('/api/auth/register', json={"name": "Luan", "email": "luan@test.com", "password": "123"})
    client.post('/api/barbers/', json={"name": "Barbeiro 1", "email": "b1@test.com"})
    client.post('/api/services/', json={"name": "Corte", "price": 30, "duration": 30})

    payload = {
        "user_id": 1,
        "barber_id": 1,
        "service_id": 1,
        "date_time": "2024-12-25T14:00:00"
    }
    
    response = client.post('/api/appointments/', json=payload)
    assert response.status_code == 201
    assert response.json['status'] == "Agendado"