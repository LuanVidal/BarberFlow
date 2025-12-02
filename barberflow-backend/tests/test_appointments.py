def setup_database(client):
    """Função auxiliar para criar dados básicos (Barbeiro, Serviço, Cliente)"""
    # Cria Barbeiro
    client.post('/api/barbers/', json={"name": "Barbeiro Teste", "email": "b@test.com"})
    # Cria Serviço
    client.post('/api/services/', json={"name": "Corte", "price": 30, "duration": 30})
    # Cria Cliente
    client.post('/api/auth/register', json={"name": "Cliente", "email": "c@test.com", "password": "123"})

def test_create_appointment_success(client):
    """Teste: Deve criar um agendamento com sucesso"""
    setup_database(client)
    
    payload = {
        "user_id": 1,
        "barber_id": 1,
        "service_id": 1,
        "date_time": "2025-12-25T14:00:00"
    }
    response = client.post('/api/appointments/', json=payload)
    assert response.status_code == 201
    assert response.json['status'] == "Agendado"

def test_prevent_double_booking(client):
    """Teste: DEVE BLOQUEAR agendamento no mesmo horário (Conflito)"""
    setup_database(client)
    
    payload = {
        "user_id": 1,
        "barber_id": 1,
        "service_id": 1,
        "date_time": "2025-12-25T15:00:00"
    }
    
    # 1. Primeiro agendamento (Sucesso)
    resp1 = client.post('/api/appointments/', json=payload)
    assert resp1.status_code == 201
    
    # 2. Segundo agendamento IGUAL (Deve falhar)
    resp2 = client.post('/api/appointments/', json=payload)
    assert resp2.status_code == 409  # Conflict
    assert "Horário ocupado!" in resp2.json['error']

def test_cancel_appointment(client):
    """Teste: Deve cancelar um agendamento"""
    setup_database(client)
    
    # Cria
    client.post('/api/appointments/', json={
        "user_id": 1, "barber_id": 1, "service_id": 1, "date_time": "2025-12-25T16:00:00"
    })
    
    # Cancela (ID 1)
    response = client.delete('/api/appointments/1')
    assert response.status_code == 200
def test_get_taken_slots(client):
    """Teste: Deve retornar apenas os horários que estão ocupados em um dia específico."""
    setup_database(client)
    
    # 1. Agendamento para Barbeiro 1 às 08:00
    client.post('/api/appointments/', json={
        "user_id": 1, "barber_id": 1, "service_id": 1, "date_time": "2025-12-30T08:00:00"
    })
    
    # 2. Agendamento para Barbeiro 1 às 14:30
    client.post('/api/appointments/', json={
        "user_id": 1, "barber_id": 1, "service_id": 1, "date_time": "2025-12-30T14:30:00"
    })
    
    # 3. Busca a lista de horários ocupados para o Barbeiro 1 no dia 2025-12-30
    response = client.get('/api/appointments/taken/1/2025-12-30')
    
    assert response.status_code == 200
    assert "08:00" in response.json
    assert "14:30" in response.json
    assert len(response.json) == 2 # Apenas 2 horários devem estar ocupados